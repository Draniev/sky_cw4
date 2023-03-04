from typing import TypeVar, Generic

from flask_sqlalchemy import SQLAlchemy
from dao.models.basemodel import BaseModel


T = TypeVar('T', bound=BaseModel)


class BaseDAO(Generic[T]):
    __model__ = T

    def __init__(self, session: SQLAlchemy().session):
        self.session = session

    def get_one(self, uid: int) -> T | None:
        return self.session.query(self.__model__).get(uid)

    def get_all(self, page: int | None = None) -> list[T] | None:
        return self.session.query(self.__model__).all()

    def create(self, entity_data: dict) -> T:
        entity = self.__model__(**entity_data)
        self.session.add(entity)
        self.session.commit()
        return entity

    def update(self, entity: T) -> T:
        self.session.add(entity)
        self.session.commit()
        return entity

    def delete(self, uid) -> T:
        entity = self.get_one(uid)

        self.session.delete(entity)
        self.session.commit()
        return entity
