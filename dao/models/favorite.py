# from dao.models.movie import MovieSchema
# from dao.models.user import UserSchema
from sqlalchemy.orm import backref

from setup_db import db
from marshmallow import Schema, fields


class Favorite(db.Model):
    __tablename__ = 'favorite'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(255), db.ForeignKey('user.id'))
    movie_id = db.Column(db.String(255), db.ForeignKey('movie.id'))

    user = db.relationship('User', foreign_keys=[user_id], backref=backref("favorite", cascade="all, delete-orphan"))
    movie = db.relationship('Movie', foreign_keys=[movie_id], backref=backref("favorite", cascade="all, delete-orphan"))


class FavoriteSchema(Schema):
    id = fields.Integer()
    user_id = fields.Integer()
    movie_id = fields.Integer()

    user = fields.Nested('UserSchema', only=('id', 'email'))
    movie = fields.Nested('MovieSchema')
