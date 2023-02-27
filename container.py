from dao.favorite import FavoritesDAO
from dao.models.director import DirectorSchema, Director
from dao.models.favorite import FavoriteSchema
from dao.models.genre import GenreSchema, Genre
from dao.models.movie import MovieSchema, Movie
from dao.models.user import UserSchema
from dao.universal_entity import UniversalDAO
from dao.user import UserDAO
from services.director import DirectorService
from services.favorite import FavoritesService
from services.genre import GenreService
from services.movie import MovieService
from services.user import UserService
from setup_db import db
from dao.movie import MovieDAO
from dao.director import DirectorDAO
from dao.genre import GenreDAO


# genre_dao = GenreDAO(db.session)
# director_dao = DirectorDAO(db.session)
movie_dao = MovieDAO(db.session)    # т.к. тут еще фильтрацию надо, то 'экспериментальный' пока брать не будем
user_dao = UserDAO(db.session)
favorites_dao = FavoritesDAO(db.session)

# Тут использую экспериментальный ДАО объект.
# Если уж нет разницы в запросах из БД,
# так что решил и два разных класса не делать
genre_dao = UniversalDAO(db.session, Genre)
director_dao = UniversalDAO(db.session, Director)
# movie_dao = UniversalDAO(db.session, Movie)

genre_service = GenreService(genre_dao)
director_service = DirectorService(director_dao)
movie_service = MovieService(movie_dao)
user_service = UserService(user_dao)
favorites_service = FavoritesService(favorites_dao)

genre_schema = GenreSchema()
director_schema = DirectorSchema()
movie_schema = MovieSchema()
user_schema = UserSchema()
favorites_schema = FavoriteSchema
