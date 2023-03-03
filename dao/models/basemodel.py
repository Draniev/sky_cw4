from sqlalchemy import Column, Integer

from setup.db import db


class BaseModel(db.Model):
    __abstract__ = True

    id = Column(Integer, autoincrement=True, primary_key=True)
