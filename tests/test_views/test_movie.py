import pytest

from dao.models.movie import Movie


class TestMoviesView:

    @pytest.fixture
    def movie(self, db):
        test_movie = Movie(title='Тестовый фильм',
                           description='Описание для тестового фильма')
        db.session.add(test_movie)
        db.session.commit()
        return test_movie

    def test_many(self, client, movie):
        response = client.get("/movies/")
        assert response.status_code == 200
        assert len(response.json) == 1

    def test_one(self, client, movie):
        response = client.get("/movies/1")
        assert response.status_code == 200
        assert response.json['title'] == 'Тестовый фильм'

        response = client.get("/movies/2")
        assert response.status_code == 404
