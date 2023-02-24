from setup_db import db
from marshmallow import fields, Schema


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    role = db.Column(db.String(255))


class UserSchema(Schema):
    id = fields.Integer()
    username = fields.String()
    password = fields.String()
    role = fields.String()
    