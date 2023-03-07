import pytest

from dao.models.user import User
from utils import get_hash, generate_jwt


class TestUsersView:
    @pytest.fixture
    def user(self, db):
        hash_pass = get_hash('Test_password')
        test_user = User(email="testemail@email.ru", password=hash_pass)
        db.session.add(test_user)
        db.session.commit()
        return test_user

    @pytest.fixture
    def auth_headers(self, user):
        user_data = {"id": user.id, "email": user.email}
        tokens = generate_jwt(user_data)
        bearer = f"Bearer {tokens['access_token']}"
        headers = {"Authorization": bearer,
                   "Content-type": "application/json"}
        return headers

    def test_many(self, client, user):
        response = client.get("/users/")
        assert response.status_code == 200
        assert len(response.json) == 1

    def test_user_homepage(self, client, user, auth_headers):
        response = client.get("/user/")
        assert response.status_code == 401

        response = client.get("/user/", headers=auth_headers)
        assert response.status_code == 200
        assert response.json['email'] == 'testemail@email.ru'

    def test_user_update(self, client, user, auth_headers):
        response = client.patch("/user/")
        assert response.status_code == 401

        new_user_data = '{"name": "New Test User"}'
        response = client.patch("/user/",
                                headers=auth_headers,
                                data=new_user_data)

        assert response.status_code == 201

        response = client.get("/user/", headers=auth_headers)
        assert response.json['name'] == 'New Test User'

    def test_user_change_password(self, client, user, auth_headers):

        new_user_pass = '{"password_1": "Test_password",\
                          "password_2": "new_password"}'
        response = client.put("/user/password",
                              headers=auth_headers,
                              data=new_user_pass)
        assert response.status_code == 201
        # Тут бы хорошо проверить что пароли поменялись, но как попасть
        # В объект пользователя без подтягивания еще ДАО в этот тест...
        assert user.password == get_hash("Test_password")
