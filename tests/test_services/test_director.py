from unittest.mock import MagicMock

import pytest

from dao.director import DirectorDAO
from dao.models.director import Director
from services.director import DirectorService


@pytest.fixture()
def director_dao_mock():
    director_1 = Director(id=1, name='Квентин Тарантино')
    director_2 = Director(id=2, name='Мартин Скарсезе')
    director_3 = Director(id=3, name='Кристофер Нолан')
    directors_list = [director_1, director_2, director_3]

    director_dao = DirectorDAO(None)
    director_dao.get_one = MagicMock(return_value=director_1)
    director_dao.get_all = MagicMock(return_value=directors_list)
    director_dao.create = MagicMock(return_value=director_2)
    director_dao.update = MagicMock(return_valut=director_2)
    director_dao.delete = MagicMock(return_value=director_3)
    return director_dao


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao_mock):
        self.director_service = DirectorService(director_dao_mock)

    def test_get_one(self):
        director = self.director_service.get_one(1)
        assert director is not None
        assert director.id is not None

    def test_get_all(self):
        directors = self.director_service.get_all()
        assert len(directors) > 0

    def test_create(self):
        director_data = {'id': 1, 'name': 'Мартин'}
        director = self.director_service.create(director_data)
        assert director.id is not None

    def test_delete(self):
        director = self.director_service.delete(2)
        assert director.id is not None
