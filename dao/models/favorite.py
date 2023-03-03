from dao.models.basemodel import BaseModel

from sqlalchemy.orm import backref, relationship
from sqlalchemy import Column, String, ForeignKey

from marshmallow import Schema, fields


class Favorite(BaseModel):
    __tablename__ = 'favorite'
    user_id = Column(String(255), ForeignKey('user.id'))
    movie_id = Column(String(255), ForeignKey('movie.id'))

    user = relationship('User',
                        foreign_keys=[user_id],
                        backref=backref(
                            "favorite", cascade="all, delete-orphan")
                        )
    movie = relationship('Movie',
                         foreign_keys=[movie_id],
                         backref=backref(
                             "favorite", cascade="all, delete-orphan")
                         )


class FavoriteSchema(Schema):
    id = fields.Integer()
    user_id = fields.Integer()
    movie_id = fields.Integer()

    user = fields.Nested('UserSchema', only=('id', 'email'))
    movie = fields.Nested('MovieSchema')
