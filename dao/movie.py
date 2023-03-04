from dao.base_dao import BaseDAO
from dao.models.movie import Movie


class MovieDAO(BaseDAO[Movie]):
    __model__ = Movie

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
