# from dao.models.movie import MovieSchema
# from dao.models.user import UserSchema
from setup_db import db
from marshmallow import Schema, fields


class Favorites(db.Model):
    __tablename__ = 'favorites'
    user_id = db.Column(db.String(255), db.ForeignKey('user.id'))
    movie_id = db.Column(db.String(255), db.ForeignKey('movie.id'))

    users = db.relationship('User', foreign_keys=[user_id])
    movies = db.relationship('Movie', foreign_keys=[movie_id])


class FavoritesSchema(Schema):
    user_id = fields.Integer()
    movie_id = fields.Integer()

    users = fields.Nested('UserSchema', only=('id', 'email'), many=True)
    movies = fields.Nested('MovieSchema', many=True)
