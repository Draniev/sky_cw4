from flask_sqlalchemy import SQLAlchemy
from dao.models.user import User


class UserDAO:
    def __init__(self, session: SQLAlchemy().session):
        self.session = session

    def get_one(self, uid: int) -> User | None:
        return self.session.query(User).get(uid)

    def get_all(self) -> list[User]:
        return self.session.query(User).all()

    def get_one_by_username(self, username: str) -> User | None:
        users = self.session.query(User).filter(User.username == username).all()
        if len(users) == 1:     # Будем считать что имя пользователя у нас уникально (ну а как еще...)
            return users[0]
        else:
            return None

    def create(self, user_data) -> User:
        new_user = User(**user_data)
        self.session.add(new_user)
        self.session.commit()
        return new_user

    def update(self, user: User) -> User:
        self.session.add(user)
        self.session.commit()
        return user

    def delete(self, uid: int) -> User | None:
        user = self.get_one(uid)
        if user:
            self.session.delete(user)
            self.session.commit()
            return user
        else:
            return None
