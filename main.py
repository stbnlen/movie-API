from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from config.database import engine, Base
from middlewares.error_handler import ErrorHandler
from routers.movie import movie_router
from routers.user import user_router

app = FastAPI()
app.title = "Movie API"
app.version = "0.0.1"

app.add_middleware(ErrorHandler)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(movie_router)
app.include_router(user_router)

Base.metadata.create_all(bind=engine)


@app.get(
    "/",
    tags=["home"],
    description="Returns the home page with a 'Hello world' message.",
)
def home() -> HTMLResponse:
    """
    Returns the home page with a "Hello world" message.
    """
    return HTMLResponse(content="<h1>Hello world</h1>")
