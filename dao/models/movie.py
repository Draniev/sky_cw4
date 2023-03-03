from dao.models.basemodel import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import backref, relationship
from marshmallow import Schema, fields


class Movie(BaseModel):
    __tablename__ = 'movie'
    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    description = Column(String(255))
    trailer = Column(String(255))
    year = Column(Integer)
    rating = Column(Integer)
    genre_id = Column(Integer, ForeignKey('genre.id'))
    director_id = Column(Integer, ForeignKey('director.id'))
    genre = relationship('Genre',
                         foreign_keys=[genre_id],
                         backref=backref('movie')
                         )
    director = relationship('Director',
                            foreign_keys=[director_id],
                            backref=backref('movie')
                            )

    users_who_selected_favorite = relationship('User', secondary='favorite')


class MovieSchema(Schema):
    id = fields.Integer()
    title = fields.String()
    description = fields.String()
    trailer = fields.String()
    year = fields.Integer()
    rating = fields.Integer()
    genre_id = fields.Integer()
    director_id = fields.Integer()
    genre = fields.Nested('GenreSchema')
    director = fields.Nested('DirectorSchema')
