from dao.favorite import FavoritesDAO
from dao.models.movie import Movie
from dao.models.user import User


class FavoritesService:
    def __init__(self, favorites_dao: FavoritesDAO):
        self.favorites_dao = favorites_dao

    def create_by_user_movie(self, user_id, movie_id):
        return self.favorites_dao.create_by_user_movie(user_id, movie_id)

    def delete_by_user_movie(self, user_id, movie_id):
        return self.favorites_dao.delete_by_user_movie(user_id, movie_id)

    def add_to_curr_user(self, user: User, movie: Movie):
        return self.favorites_dao.add_movie_to_curr_user(user, movie)