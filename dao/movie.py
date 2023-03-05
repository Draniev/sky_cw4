from dao.base_dao import BaseDAO
from dao.models.movie import Movie
from constants import ITEMS_PER_PAGE
from flask_sqlalchemy import BaseQuery


class MovieDAO(BaseDAO[Movie]):
    __model__ = Movie

    def get_all(self,
                page: int | None = None,
                novelties: bool = False) -> list[Movie]:

        stmt: BaseQuery = self.session.query(self.__model__)
        if novelties:
            stmt = stmt.order_by(self.__model__.year.desc())

        if page:
            try:
                # return stmt.paginate(page=1, max_per_page=2).items
                return stmt.paginate(page=page, per_page=ITEMS_PER_PAGE).items
            except Exception:
                return []

        return stmt.all()

    # def get_all(self, filter_args: dict | None) -> list[Movie]:
    #     match filter_args:
    #         case {'director_id': director_id, 'genre_id': genre_id}:
    #             movies = self.session.query(Movie) \
    #                 .filter(Movie.director_id == director_id) \
    #                 .filter(Movie.genre_id == genre_id) \
    #                 .all()
    #         case {'director_id': director_id}:
    #             movies = self.session.query(Movie).filter(Movie.director_id == director_id).all()
    #         case {'genre_id': genre_id}:
    #             movies = self.session.query(Movie).filter(Movie.genre_id == genre_id).all()
    #         case {'year': year}:
    #             movies = self.session.query(Movie).filter(Movie.year == year).all()
    #         case _:
    #             movies = self.session.query(Movie).all()
    # return movies
