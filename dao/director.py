from flask_sqlalchemy import SQLAlchemy
from dao.models.director import Director


class DirectorDAO:
    def __init__(self, session: SQLAlchemy().session):
        self.session = session

    def get_one(self, did):
        return self.session.guery(Director).get(did)

    def get_all(self):
        return self.session.query(Director).all()

    def create(self, director_data):
        director = Director(**director_data)
        self.session.add(director)
        self.session.commit()
        return director

    def update(self, director: Director):
        self.session.add(director)
        self.session.commit()
        return director

    def delete(self, did):
        director = self.get_one(did)

        self.session.delete(director)
        self.session.commit()
        return director
