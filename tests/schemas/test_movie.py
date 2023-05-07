import pytest
from pydantic import ValidationError
from schemas.movie import Movie


def test_movie_valid():
    movie = Movie(
        title="Avengers",
        overview="Earth's Mightiest Heroes must come together and learn to fight as a team if they are going to stop the mischievous Loki and his alien army from enslaving humanity.",
        year=2012,
        rating=8.0,
        category="Action",
    )
    assert movie.title == "Avengers"
    assert (
        movie.overview
        == "Earth's Mightiest Heroes must come together and learn to fight as a team if they are going to stop the mischievous Loki and his alien army from enslaving humanity."
    )
    assert movie.year == 2012
    assert movie.rating == 8.0
    assert movie.category == "Action"


def test_movie_invalid_title():
    with pytest.raises(ValidationError):
        Movie(
            title="abc",
            overview="This is a long overview for a movie.",
            year=2022,
            rating=6.5,
            category="Sci-Fi",
        )


def test_movie_invalid_rating():
    with pytest.raises(ValidationError):
        Movie(
            title="The Dark Knight",
            overview="When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.",
            year=2008,
            rating=20.0,
            category="Action",
        )
