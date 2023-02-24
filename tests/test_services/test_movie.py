from unittest.mock import MagicMock

import pytest

from dao.models.movie import Movie
from dao.movie import MovieDAO
from services.movie import MovieService


@pytest.fixture()
def movie_dao_mock():
    movie_1 = Movie(id=1, title='Фильм номер 1')
    movie_2 = Movie(id=2, title='Фильм номер 2')
    movie_3 = Movie(id=3, title='Фильм номер 3')
    movies_list = [movie_1, movie_2, movie_3]

    movie_dao = MovieDAO(None)
    movie_dao.get_one = MagicMock(return_value=movie_1)
    movie_dao.get_all = MagicMock(return_value=movies_list)
    movie_dao.create = MagicMock(return_value=movie_2)
    movie_dao.update = MagicMock(return_valut=movie_2)
    movie_dao.delete = MagicMock(return_value=movie_3)
    return movie_dao


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao_mock):
        self.movie_service = MovieService(movie_dao_mock)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)
        assert movie is not None
        assert movie.id is not None

    def test_get_all(self):
        movies = self.movie_service.get_all(None)
        assert len(movies) > 0

    def test_create(self):
        movie_data = {'id': 1, 'title': 'тестовый фильм'}
        movie = self.movie_service.create(movie_data)
        assert movie.id is not None

    def test_delete(self):
        movie = self.movie_service.delete(2)
        assert movie.id is not None
