from fastapi import APIRouter, Depends, Path, Query, status
from fastapi.responses import JSONResponse
from typing import List
from config.database import Session
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from services.movie import MovieService
from schemas.movie import Movie

movie_router = APIRouter()


def get_db() -> None:
    db = Session()
    try:
        yield db
    finally:
        db.close()


def get_movie_service(db: Session = Depends(get_db)) -> MovieService:
    return MovieService(db)


@movie_router.get(
    "/movies",
    tags=["movies"],
    response_model=List[Movie],
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_movie_service)],
)
def get_movies(movie_service: MovieService = Depends(get_movie_service)) -> List[Movie]:
    result = movie_service.get_movies()
    return JSONResponse(
        status_code=status.HTTP_200_OK, content=jsonable_encoder(result)
    )


@movie_router.get(
    "/movies/{id}",
    tags=["movies"],
    response_model=Movie,
    dependencies=[Depends(get_movie_service)],
)
def get_movie(
    movie_service: MovieService = Depends(get_movie_service),
    id: int = Path(ge=1, le=2000),
) -> Movie:
    result = movie_service.get_movie(id)
    if not result:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND, content={"message": "No encontrado"}
        )
    return JSONResponse(
        status_code=status.HTTP_200_OK, content=jsonable_encoder(result)
    )


@movie_router.get(
    "/movies/",
    tags=["movies"],
    response_model=List[Movie],
    dependencies=[Depends(get_movie_service)],
)
def get_movies_by_category(
    category: str = Query(min_length=5, max_length=15),
    movie_service: MovieService = Depends(get_movie_service),
) -> List[Movie]:
    result = movie_service.get_movies_by_category(category)
    if not result:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND, content={"message": "No encontrado"}
        )
    return JSONResponse(
        status_code=status.HTTP_200_OK, content=jsonable_encoder(result)
    )


@movie_router.post(
    "/movies",
    tags=["movies"],
    response_model=dict,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(get_movie_service)],
)
def create_movie(
    movie: Movie, movie_service: MovieService = Depends(get_movie_service)
) -> dict:
    movie_service.create_movie(movie)
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={"message": "Se ha registrado la película"},
    )


@movie_router.put(
    "/movies/{id}",
    tags=["movies"],
    response_model=dict,
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_movie_service)],
)
def update_movie(
    id: int, movie: Movie, movie_service: MovieService = Depends(get_movie_service)
) -> dict:
    result = movie_service.get_movie(id)
    if not result:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND, content={"message": "No encontrado"}
        )
    movie_service.update_movie(id, movie)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"message": "Se ha modificado la película"},
    )


@movie_router.delete(
    "/movies/{id}",
    tags=["movies"],
    response_model=dict,
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_movie_service), Depends(JWTBearer())],
)
def delete_movie(
    id: int, movie_service: MovieService = Depends(get_movie_service)
) -> dict:
    db = Session()
    result = movie_service.get_movie(id)
    if not result:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND, content={"message": "No encontrado"}
        )
    movie_service.delete_movie(id)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"message": "Se ha eliminado la película"},
    )
