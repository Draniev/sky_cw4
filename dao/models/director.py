from dao.models.basemodel import BaseModel
from sqlalchemy import Column, String
from marshmallow import Schema, fields


class Director(BaseModel):
    __tablename__ = 'director'
    name = Column(String(255))


class DirectorSchema(Schema):
    id = fields.Integer()
    name = fields.String()
