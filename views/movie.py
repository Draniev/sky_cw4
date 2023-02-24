from flask import request
from flask_restx import Resource, Namespace

from container import movie_service, movie_schema
from utils import admin_required

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    # Получение всех
    def get(self):
        filter_args = request.args.to_dict()
        movies = movie_service.get_all(filter_args)
        return movie_schema.dump(movies, many=True), 200

    # Создание нового
    @admin_required
    def post(self):
        movie_data = request.json
        movie = movie_service.create(movie_data)
        return "", 201


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    # Получение одного
    def get(self, mid: int):
        movie = movie_service.get_one(mid)
        if movie:
            return movie_schema.dump(movie), 200
        else:
            return "Ошибка, ошибка, хаха", 404

    # Изменение одного
    @admin_required
    def put(self, mid):
        movie_data = request.json
        movie_data['id'] = mid
        movie = movie_service.update(movie_data)
        if movie:
            return "", 200
        else:
            return "Нечего тут обновлять!", 404

    # Удаление
    @admin_required
    def delete(self, mid):
        movie = movie_service.delete(mid)
        if movie:
            return "", 204
        else:
            return "Тут и так пусто", 404
