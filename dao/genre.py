from flask_sqlalchemy import SQLAlchemy
from dao.models.genre import Genre


class GenreDAO:
    def __init__(self, session: SQLAlchemy().session):
        self.session = session

    def get_one(self, gid: int):
        return self.session.query(Genre).get(gid)

    def get_all(self):
        return self.session.query(Genre).all()

    def create(self, genre_data):
        genre = Genre(**genre_data)
        self.session.add(genre)
        self.session.commit()
        return genre

    def update(self, genre: Genre):
        self.session.add(genre)
        self.session.commit()
        return genre

    def delete(self, gid: int):
        genre = self.get_one(gid)

        self.session.delete(genre)
        self.session.commit()
        return genre
