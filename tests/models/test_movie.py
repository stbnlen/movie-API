from models.movie import Movie
from sqlalchemy import Integer, String, Float


def test_movie_instance_creation():
    movie = Movie(
        title="The Shawshank Redemption",
        overview="Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
        year=1994,
        rating=9.3,
        category="Drama",
    )

    assert isinstance(movie, Movie)


def test_movie_instance_attributes():
    movie = Movie(
        title="The Shawshank Redemption",
        overview="Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
        year=1994,
        rating=9.3,
        category="Drama",
    )

    assert movie.title == "The Shawshank Redemption"
    assert (
        movie.overview
        == "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency."
    )
    assert movie.year == 1994
    assert movie.rating == 9.3
    assert movie.category == "Drama"


def test_movie_table_schema():
    assert Movie.__tablename__ == "movies"

    assert isinstance(Movie.id.type, Integer)
    assert Movie.id.primary_key

    assert isinstance(Movie.title.type, String)

    assert isinstance(Movie.overview.type, String)

    assert isinstance(Movie.year.type, Integer)

    assert isinstance(Movie.rating.type, Float)

    assert isinstance(Movie.category.type, String)
