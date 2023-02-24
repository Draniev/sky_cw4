from unittest.mock import MagicMock

import pytest

from dao.genre import GenreDAO
from dao.models.genre import Genre
from services.genre import GenreService


@pytest.fixture()
def genre_dao_mock():
    genre_1 = Genre(id=1, name='Ужас')
    genre_2 = Genre(id=2, name='Комедия')
    genre_3 = Genre(id=3, name='Трагедия')
    genres_list = [genre_1, genre_2, genre_3]

    genre_dao = GenreDAO(None)
    genre_dao.get_one = MagicMock(return_value=genre_1)
    genre_dao.get_all = MagicMock(return_value=genres_list)
    genre_dao.create = MagicMock(return_value=genre_2)
    genre_dao.update = MagicMock(return_valut=genre_2)
    genre_dao.delete = MagicMock(return_value=genre_3)
    return genre_dao


class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao_mock):
        self.genre_service = GenreService(genre_dao_mock)

    def test_get_one(self):
        genre = self.genre_service.get_one(1)
        assert genre is not None
        assert genre.id is not None

    def test_get_all(self):
        genres = self.genre_service.get_all()
        assert len(genres) > 0

    def test_create(self):
        genre_data = {'id': 1, 'name': 'Кошмар'}
        genre = self.genre_service.create(genre_data)
        assert genre.id is not None

    def test_delete(self):
        genre = self.genre_service.delete(2)
        assert genre.id is not None
