from flask import request
from flask_restx import Resource, Namespace

from container import user_service, user_schema
from utils import auth_required, check_auth

users_ns = Namespace('users')
user_ns = Namespace('user')


@users_ns.route('/')
class UsersView(Resource):
    def get(self):
        """
        Список всех пользователей системы. Доступ без авторизации (почему бы и нет)
        :return:
        """
        users = user_service.get_all()
        return user_schema.dump(users, many=True), 200


@users_ns.route('/<int:uid>')
class UserViewByID(Resource):
    # Отображение данных о пользователе. Для админа
    @auth_required
    def get(self, uid: int):
        """
        Вывод данных по пользователю с ID == uid.
        :param uid: id пользователя
        :return: Объект User в json формате
        """
        user = user_service.get_one(uid)
        if user:
            return user_schema.dump(user), 200
        else:
            return "Ошибочка, нет никого", 404

    @auth_required
    def put(self, uid: int):
        """
        Обновление данных пользователя с ID == uid.
        :param uid: id пользователя
        :return: "", 201
        """
        user_data = request.json
        user_data['id'] = uid
        user = user_service.update(user_data)
        if user:
            return "", 201
        else:
            return "Отсутствует пользователь для обновления", 404

    @auth_required
    def delete(self, uid: int):
        """
        Удаление пользователя с ID == uid
        """
        user = user_service.delete(uid)
        if user:
            return "", 204
        else:
            return "Пользователь отсутствует", 404


@user_ns.route('/')
class UserView(Resource):
    def get(self):
        """
        Вывод информации (личной страницы) о текущем пользователе
        :return:
        """

        current_user = check_auth(request.headers)
        user = user_service.get_one(current_user.get('id'))
        return user_schema.dump(user), 200

    def patch(self):
        """
        Обновление данных текущего пользователя (имя, фамилия, почта, жанр)
        :return:
        """

        current_user = check_auth(request.headers)
        fields_4_update = request.json
        fields_4_update[id] = current_user.id
        user = user_service.update(fields_4_update)
        if user:
            return "", 201
        else:
            return "Что-то пошло не так", 400


@user_ns.route('/password')
class UserChangePassword(Resource):
    def put(self):
        """
        Обновление пароля пользователя.
        Ожидает password_1 и password_2 в параметрах запроса.
        :return: "", 201
        """
        current_user = check_auth(request.headers)
        old_password = request.json.get('password_1')
        new_password = request.json.get('password_2')
        user = user_service.update_password(
            current_user.get('id'), old_password, new_password)
        return "", 201
