from flask_sqlalchemy import SQLAlchemy


class UniversalDAO:
    def __init__(self, session: SQLAlchemy().session, entity_model: SQLAlchemy().Model):
        self.session = session
        self.entity_model = entity_model

    def get_one(self, uid: int):
        return self.session.query(self.entity_model).get(uid)

    def get_all(self):
        return self.session.query(self.entity_model).all()

    def create(self, entity_data):
        entity = self.entity_model(**entity_data)
        self.session.add(entity)
        self.session.commit()
        return entity

    def update(self, entity: SQLAlchemy().Model):
        self.session.add(entity)
        self.session.commit()
        return entity

    def delete(self, uid):
        entity = self.get_one(uid)

        self.session.delete(entity)
        self.session.commit()
        return entity
