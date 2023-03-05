from flask import request
from flask_restx import Resource, Namespace
from container import director_service, director_schema
from utils import admin_required
from webargs.flaskparser import parser
from setup.parser import def_filter_args

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    """
    Эндпоинт для работы с объектом Режисёра.
    Отображение всех режисёров и создание новых.
    """

    @director_ns.doc(params={'page': 'The page number of the requested data'})
    def get(self):
        """
        Отображение всех режисёров. Постранично при наличии параметра
        page в запросе.
        """
        args = parser.parse(def_filter_args, request, location='query')
        page = args.get('page', None)
        directors = director_service.get_all(page=page)
        return director_schema.dump(directors, many=True), 200

    @admin_required
    def post(self):
        """Добавление нового режиссера в базу данных"""
        director_data = request.json
        director_service.create(director_data)
        return "", 201


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    # Получение режисcёра по ID
    def get(self, did: int):
        """Отображение данных конкретного режиссера"""
        director = director_service.get_one(did)
        return director_schema.dump(director), 200

    # Изменение одного
    @admin_required
    def put(self, did):
        """
        Обновление данных для режисера с ID
        """
        director_data = request.json
        director_data['id'] = did
        director = director_service.update(director_data)
        if director:
            return "", 200
        else:
            return "Нечего тут обновлять!", 404

    # Удаление
    @admin_required
    def delete(self, did):
        director = director_service.delete(did)
        if director:
            return "", 204
        else:
            return "Тут и так пусто", 404
