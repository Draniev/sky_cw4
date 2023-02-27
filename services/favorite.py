from dao.favorite import FavoritesDAO


class FavoritesService:
    def __init__(self, favorites_dao: FavoritesDAO):
        self.favorites_dao = favorites_dao

    def create_by_user_movie(self, user_id, movie_id):
        self.favorites_dao.create_by_user_movie(user_id, movie_id)

    def delete_by_user_movie(self, user_id, movie_id):
        self.favorites_dao.delete_by_user_movie(user_id, movie_id)
    