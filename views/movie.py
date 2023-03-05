from flask import request
from flask_restx import Resource, Namespace
from webargs.flaskparser import parser

from container import movie_service, movie_schema
from utils import admin_required
from setup.parser import def_filter_args

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    """
    Отображает список всех фильмов и добавляет новый фильм (если вы админ, ха)
    """

    @movie_ns.doc(params={'page': 'The page number of the requested data',
                          'status': 'New or blank, display new items at top',
                          })
    def get(self):
        """
        Отображает список всех фильмов с потстраничной пагинацией.
        В задании не было, а я уже утомился, так что убрал из возможностей
        фильрацию по разным другим полям.

        В исходниках для пагинации используются возможности модуля flask_restx,
        но в документации к модулю же рекомендуется использовать что-то еще,
        например marshmallow.
        """
        args = parser.parse(def_filter_args, request, location='query')
        page = args.get('page', None)
        if args.get('status', None) == 'New':
            novelties = True
        else:
            novelties = False
        movies = movie_service.get_all(page=page, novelties=novelties)
        return movie_schema.dump(movies, many=True), 200

    # Создание нового
    @admin_required
    def post(self):
        """
        Добавление нового фильма в базу данных
        """
        movie_data = request.json
        movie_service.create(movie_data)
        return "", 201


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    """
    Обработка одного объекта фильма: отображение, обновление, удаление
    """

    def get(self, mid: int):
        """
        Отображение одного объекта фильма
        """
        movie = movie_service.get_one(mid)
        if movie:
            return movie_schema.dump(movie), 200
        else:
            return "Ошибка, ошибка, хаха", 404

    # Изменение одного
    @admin_required
    def put(self, mid):
        """
        Обновление фильма данными из запроса
        """
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
        """
        Удаление фильма с концами с сервера. Отменить невозможно, так то!
        """
        movie = movie_service.delete(mid)
        if movie:
            return "", 204
        else:
            return "Тут и так пусто", 404
