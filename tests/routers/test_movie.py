from main import app
from fastapi import status
from fastapi.testclient import TestClient
from routers.movie import movie_router


def test_get_movies_returns_list():
    app.include_router(movie_router)
    with TestClient(app) as client:
        response = client.get("/movies")
        assert response.status_code == status.HTTP_200_OK
        assert isinstance(response.json(), list)


def test_get_movies_returns_correct_fields():
    app.include_router(movie_router)
    with TestClient(app) as client:
        response = client.get("/movies")
        assert response.status_code == status.HTTP_200_OK
        for movie in response.json():
            assert all(
                field in movie
                for field in ["id", "title", "overview", "year", "rating", "category"]
            )
