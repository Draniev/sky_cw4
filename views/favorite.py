from flask import request
from flask_restx import Resource, Namespace

from container import favorites_service, movie_service
from utils import check_auth

favorite_ns = Namespace('favorites')


@favorites_ns.route('/movies/<int:mid>')
class FavoritesCreateDelete(Resource):
    def post(self, mid: int):
        """
        Добавление фильма в список любимых для текущего пользователя
        :param mid:
        :return:
        """
        current_user = check_auth(request.headers)
        movie = movie_service.get_one(mid)
        if movie:
            favorites_service.create_by_user_movie(current_user['id'], mid)
            return "", 201
        else:
            return "Такой фильм отсутствует", 404

    def delete(self, mid: int):
        """
        Удаление фильма из списка любимых у текущего пользователя
        :param mid:
        :return:
        """
        current_user = check_auth(request.headers)
        item = favorites_service.delete_by_user_movie(current_user['id'], mid)
        if item:
            return "", 204
        else:
            return "Запись для удаления не найдена", 404
