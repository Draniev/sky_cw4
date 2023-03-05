from dao.models.director import Director
from dao.director import DirectorDAO


class DirectorService:
    def __init__(self, director_dao: DirectorDAO):
        self.director_dao = director_dao

    def get_one(self, did: int) -> Director:
        return self.director_dao.get_one(did)

    def get_all(self, page: int | None = None) -> list[Director]:
        return self.director_dao.get_all(page=page)

    def create(self, director_data: dict) -> Director:
        return self.director_dao.create(director_data)

    def update(self, director_data: dict) -> Director:
        director = self.director_dao.get_one(director_data['id'])
        keys_4_update = director_data.keys()

        if 'name' in keys_4_update:
            director.name = director_data['name']

        return self.director_dao.update(director)

    def delete(self, did: int):
        return self.director_dao.delete(did)
