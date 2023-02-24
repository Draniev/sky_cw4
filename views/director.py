from flask import request
from flask_restx import Resource, Namespace
from container import director_service, director_schema
from utils import admin_required

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    # Получение всех режисcёров
    def get(self):
        directors = director_service.get_all()
        return director_schema.dump(directors, many=True), 200

    @admin_required
    def post(self):
        director_data = request.json
        director = director_service.create(director_data)
        return "", 201


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    # Получение режисcёра по ID
    def get(self, did: int):
        director = director_service.get_one(did)
        return director_schema.dump(director), 200

    # Изменение одного
    @admin_required
    def put(self, did):
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
