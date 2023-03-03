from dao.models.basemodel import BaseModel
from marshmallow import Schema, fields
from sqlalchemy import Column, Integer, String


class Genre(BaseModel):
    __tablename__ = 'genre'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))


class GenreSchema(Schema):
    id = fields.Integer()
    name = fields.String()
