from dao.models.basemodel import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from marshmallow import fields, Schema


class User(BaseModel):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True)
    password = Column(String(255))
    # role = Column(String(255))
    name = Column(String(255))
    surname = Column(String(255))

    favorite_genre_id = Column(Integer, ForeignKey('genre.id'))
    favorite_genre = relationship('Genre', foreign_keys=[favorite_genre_id])

    favorites = relationship('Movie', secondary='favorite')


class UserSchema(Schema):
    id = fields.Integer()
    email = fields.Email()
    password = fields.String(load_only=True)
    # role = fields.String()
    name = fields.String()
    surname = fields.String()
    favorite_genre_id = fields.Integer()
    favorite_genre = fields.Nested('GenreSchema', only=('id', 'name'))

    favorites = fields.Nested('FavoriteSchema', many=True)
