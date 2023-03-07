from flask import Flask
from flask_cors import CORS
#
from setup.api import api
from config import Config
from setup.db import db

# Импорт нэймспейсов из вьюшек
from views.favorite import favorite_ns
from views.genre import genre_ns
from views.movie import movie_ns
from views.director import director_ns
from views.user import user_ns, users_ns
from views.auth import auth_ns


def create_app(config_object: Config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_object)
    return app


# функция подключения расширений (Flask-SQLAlchemy, Flask-RESTx, ...)
def register_extensions(app: Flask):
    CORS(app=app)
    db.init_app(app)
    api.init_app(app)
    api.add_namespace(movie_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(director_ns)
    api.add_namespace(users_ns)
    api.add_namespace(user_ns)
    api.add_namespace(auth_ns)
    api.add_namespace(favorite_ns)


# def create_data(app, db):
#     with app.app_context():
#         db.create_all()
#
#         # создать несколько сущностей чтобы добавить их в БД
#         u1 = User(username="test_user", password="there must be a hash")
#         with db.session.begin():
#             db.session.add_all([u1])


if __name__ == '__main__':
    app = create_app(Config())
    register_extensions(app)
    # create_data(app, db)
    # with app.app_context():
    #     db.create_all()
    app.run(host="localhost", port=5000, debug=True)
