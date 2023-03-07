import pytest

from config import TestingConfig
from app import create_app, register_extensions
from setup.db import db as database


@pytest.fixture()
def two_plus_two_data():
    return 2, 2


@pytest.fixture
def app():
    app = create_app(TestingConfig)
    register_extensions(app)
    with app.app_context():
        yield app


@pytest.fixture
def db(app):
    # database.init_app(app)  # Не очень понятно зачем второй раз делать ИНИТ
    database.drop_all()     # Главное не включить с основной БД :)
    database.create_all()
    database.session.commit()

    yield database

    database.session.close()


@pytest.fixture
def client(app, db):
    with app.test_client() as client:
        yield client
