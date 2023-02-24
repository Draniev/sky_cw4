from flask import request
from flask_restx import Resource, Namespace

from container import user_service, user_schema
from utils import admin_required

user_ns = Namespace('users')


@user_ns.route('/')
class UsersView(Resource):
    # Пока зарезеревируем, может сделаем отображение всех для админа
    def get(self):
        users = user_service.get_all()
        return user_schema.dump(users, many=True), 200

    # Создание нового пользователя
    def post(self):
        user_data = request.json
        user = user_service.create(user_data)
        return "", 201


@user_ns.route('/<int:uid>')
class UserView(Resource):
    # Отображение данных о пользователе. Для админа
    @admin_required
    def get(self, uid: int):
        user = user_service.get_one(uid)
        if user:
            return user_schema.dump(user), 200
        else:
            return "Ошибочка, нет никого", 404

    # Обновление данных о пользователе (для админа или для себя лично)
    @admin_required
    def put(self, uid: int):
        user_data = request.json
        user_data['id'] = uid
        user = user_service.update(user_data)
        if user:
            return "", 201
        else:
            return "Отсутствует пользователь для обновления", 404

    # Удаление пользователя. Только для админа
    @admin_required
    def delete(self, uid: int):
        user = user_service.delete(uid)
        if user:
            return "", 204
        else:
            return "Пользователь отсутствует", 404

