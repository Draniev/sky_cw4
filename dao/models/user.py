# from dao.models.genre import GenreSchema
from setup_db import db
from marshmallow import fields, Schema


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255))
    password = db.Column(db.String(255))
    # role = db.Column(db.String(255))
    name = db.Column(db.String(255))
    surname = db.Column(db.String(255))
    favorite_genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'))
    favorite_genre = db.relationship('Genre', foreign_keys=[favorite_genre_id])


class UserSchema(Schema):
    id = fields.Integer()
    email = fields.String()
    password = fields.String()
    # role = fields.String()
    name = fields.String()
    surname = fields.String()
    favorite_genre_id = fields.Integer()
    favorite_genre = fields.Nested('GenreSchema', only=('id', 'name'))
