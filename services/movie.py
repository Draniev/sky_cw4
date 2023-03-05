from dao.models.movie import Movie
from dao.movie import MovieDAO
# from dao.universal_entity import UniversalDAO


class MovieService:
    def __init__(self, movie_dao: MovieDAO):
        self.movie_dao = movie_dao

    def get_one(self, mid: int) -> Movie | None:
        return self.movie_dao.get_one(mid)

    def get_all(self, page: int | None = None) -> list[Movie]:
        return self.movie_dao.get_all(page=page)
        # return self.movie_dao.get_all(filter_args)

    def create(self, movie_data: dict) -> Movie:
        return self.movie_dao.create(movie_data)

    def update(self, movie_data: dict) -> Movie | None:
        movie_id = movie_data['id']
        movie = self.movie_dao.get_one(movie_id)

        if movie:
            if 'title' in movie_data.keys():
                movie.title = movie_data['title']
            if 'description' in movie_data.keys():
                movie.description = movie_data['description']
            if 'trailer' in movie_data.keys():
                movie.trailer = movie_data['trailer']
            if 'rating' in movie_data.keys():
                movie.rating = movie_data['rating']
            if 'year' in movie_data.keys():
                movie.year = movie_data['year']
            if 'genre_id' in movie_data.keys():
                movie.genre_id = movie_data['genre_id']
            if 'director_id' in movie_data.keys():
                movie.director_id = movie_data['director_id']

            return self.movie_dao.update(movie)

        else:
            return None

    def delete(self, mid: int) -> Movie | None:
        return self.movie_dao.delete(mid)
