from dao.base_dao import BaseDAO
from dao.models.favorite import Favorite
from dao.models.movie import Movie
from dao.models.user import User


class FavoritesDAO(BaseDAO[Favorite]):
    __model__ = Favorite

    def get_by_user(self, uid: int) -> list[Favorite]:
        favorites = self.session.query(Favorite) \
            .filter(Favorite.user_id == uid) \
            .all()
        return favorites

    def get_by_movie(self, mid: int) -> list[Favorite]:
        favorites = self.session.query(Favorite) \
            .filter(Favorite.movie_id == mid) \
            .all()
        return favorites

    def get_by_id(self, fid: int) -> Favorite | None:
        return self.session.query(Favorite).get(fid)

    def delete_by_id(self, fid: int) -> Favorite | None:
        item = self.get_by_id(fid)
        if item:
            self.session.delete(item)
            self.session.commit()
            return item
        else:
            return None

    def get_by_user_movie(self,
                          user_id: int,
                          movie_id: int) -> Favorite | None:
        smtm = self.session.query(Favorite)\
            .filter(Favorite.user_id == user_id)\
            .filter(Favorite.movie_id == movie_id)
        items = smtm.all()

        if len(items) == 1:
            return items[0]
        else:
            return None

    def delete_by_user_movie(self,
                             user_id: int,
                             movie_id: int) -> Favorite | None:
        item = self.get_by_user_movie(user_id, movie_id)

        if item:
            self.session.delete(item)
            self.session.commit()
            return item
        else:
            return None

    def create_by_user_movie(self,
                             user_id: int,
                             movie_id: int) -> Favorite | None:
        # Проверяем наличие аналогичной записи, если еще нет, то создаём
        item = self.get_by_user_movie(user_id, movie_id)
        if item:
            return None
        else:
            new_item = Favorite(user_id=user_id, movie_id=movie_id)
            self.session.add(new_item)
            self.session.commit()
            return new_item

    def add_movie_to_curr_user(self, user: User, movie: Movie):
        user.favorites.append(movie)
        self.session.commit()
        return user
