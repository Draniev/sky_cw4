import pytest

from dao.models.user import User
from dao.models.movie import Movie
from utils import get_hash, generate_jwt


class TestFavoritesView:
    @pytest.fixture
    def user(self, db):
        hash_pass = get_hash('Test_password')
        test_user = User(email="testemail@email.ru", password=hash_pass)
        db.session.add(test_user)
        db.session.commit()
        return test_user

    @pytest.fixture
    def movie(self, db):
        test_movie = Movie(title='Тестовый фильм',
                           description='Описание для тестового фильма')
        db.session.add(test_movie)
        db.session.commit()
        return test_movie

    @pytest.fixture
    def auth_headers(self, user):
        user_data = {"id": user.id, "email": user.email}
        tokens = generate_jwt(user_data)
        bearer = f"Bearer {tokens['access_token']}"
        headers = {"Authorization": bearer,
                   "Content-type": "application/json"}
        return headers

    def test_many_movies(self, client, movie):
        response = client.get("/movies/")
        assert response.status_code == 200
        assert len(response.json) == 1

    def test_add_favorites(self, client, user, movie, auth_headers):
        response = client.post("/favorites/movies/1", headers=auth_headers)
        assert response.status_code == 201

        response = client.get("/user/", headers=auth_headers)
        assert len(response.json['favorites']) == 1
        assert response.json['favorites'][0]['id'] == 1

        response = client.post("/favorites/movies/2", headers=auth_headers)
        assert response.status_code == 404

    def test_del_favorites(self, client, user, movie, auth_headers):
        response = client.post("/favorites/movies/1", headers=auth_headers)
        assert response.status_code == 201

        response = client.get("/user/", headers=auth_headers)
        assert len(response.json['favorites']) == 1

        response = client.delete("/favorites/movies/1", headers=auth_headers)
        assert response.status_code == 204

        response = client.get("/user/", headers=auth_headers)
        assert len(response.json['favorites']) == 0
