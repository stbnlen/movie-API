from fastapi import APIRouter, Depends, Path, Query, status
from fastapi.responses import JSONResponse
from typing import List
from config.database import Session
from models.movie import Movie as MovieModel
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from services.movie import MovieService
from schemas.movie import Movie

movie_router = APIRouter()


@movie_router.get(
    "/movies",
    tags=["movies"],
    response_model=List[Movie],
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(JWTBearer())],
)
def get_movies() -> List[Movie]:
    db = Session()
    result = MovieService(db).get_movies()
    return JSONResponse(
        status_code=status.HTTP_200_OK, content=jsonable_encoder(result)
    )


@movie_router.get("/movies/{id}", tags=["movies"], response_model=Movie)
def get_movie(id: int = Path(ge=1, le=2000)) -> Movie:
    db = Session()
    result = MovieService(db).get_movie(id)
    if not result:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND, content={"message": "No encontrado"}
        )
    return JSONResponse(
        status_code=status.HTTP_200_OK, content=jsonable_encoder(result)
    )


@movie_router.get("/movies/", tags=["movies"], response_model=List[Movie])
def get_movies_by_category(
    category: str = Query(min_length=5, max_length=15)
) -> List[Movie]:
    db = Session()
    result = MovieService(db).get_movies_by_category(category)
    if not result:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND, content={"message": "No encontrado"}
        )
    return JSONResponse(
        status_code=status.HTTP_200_OK, content=jsonable_encoder(result)
    )


@movie_router.post(
    "/movies", tags=["movies"], response_model=dict, status_code=status.HTTP_201_CREATED
)
def create_movie(movie: Movie) -> dict:
    db = Session()
    MovieService(db).create_movie(movie)
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={"message": "Se ha registrado la película"},
    )


@movie_router.put(
    "/movies/{id}", tags=["movies"], response_model=dict, status_code=status.HTTP_200_OK
)
def update_movie(id: int, movie: Movie) -> dict:
    db = Session()
    result = MovieService(db).get_movie(id)
    if not result:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND, content={"message": "No encontrado"}
        )
    MovieService(db).update_movie(id, movie)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"message": "Se ha modificado la película"},
    )


@movie_router.delete(
    "/movies/{id}", tags=["movies"], response_model=dict, status_code=status.HTTP_200_OK
)
def delete_movie(id: int) -> dict:
    db = Session()
    result = MovieService(db).get_movie(id)
    if not result:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND, content={"message": "No encontrado"}
        )
    MovieService(db).delete_movie(id)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"message": "Se ha eliminado la película"},
    )
