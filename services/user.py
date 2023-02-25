from dao.models.user import User
from dao.user import UserDAO
from utils import get_hash


class UserService:
    def __init__(self, user_dao: UserDAO):
        self.user_dao = user_dao

    def get_one(self, uid: int) -> User | None:
        return self.user_dao.get_one(uid)

    def get_all(self) -> list[User]:
        return self.user_dao.get_all()

    def get_by_email(self, email: str) -> User | None:
        return self.user_dao.get_one_by_email(email)

    def create(self, user_data: dict) -> User:
        # На вход получаем пароль в открытом виде, но сохраняем хэш
        user_data['password'] = get_hash(user_data['password'])
        return self.user_dao.create(user_data)

    def update(self, user_data: dict) -> User | None:
        user_id = user_data['id']
        user = self.user_dao.get_one(user_id)
        keys_4_update = user_data.keys()

        if user:
            if 'email' in keys_4_update:
                user.email = user_data['email']
            if 'name' in keys_4_update:
                user.name = user_data['name']
            if 'surname' in keys_4_update:
                user.surname = user_data['surname']
            if 'favorite_genre_id' in keys_4_update:
                user.favorite_genre_id = user_data['favorite_genre_id']
            # По ТЗ менять пароль требуется отдельной
            # процедурой с передачей обоих паролей
            # if 'password' in keys_4_update:
            #     # На вход получаем пароль в открытом виде, но сохраняем хэш
            #     user.password = get_hash(user_data['password'])
            # if 'role' in keys_4_update:
            #     user.role = user_data['role']

            return self.user_dao.update(user)

        else:
            return None

    def update_password(self, uid: int, old_password: str, new_password: str) -> User | None:
        """
        Меняет старый пароль на новый у пользователя с id = uid
        :param uid: ID пользователя, у которого меняем пароли
        :param old_password: старый пароль пользователя
        :param new_password: новый пароль пользователя
        :return:
        """
        user = self.user_dao.get_one(uid)
        if user:
            if user.password == get_hash(old_password):
                user.password = get_hash(new_password)
                return self.user_dao.update(user)
            else:
                return None
        else:
            return None

    def delete(self, uid: int) -> User | None:
        return self.user_dao.delete(uid)
