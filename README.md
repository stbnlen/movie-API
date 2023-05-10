# FastAPI Movie CRUD Application

This is a simple CRUD (Create, Read, Update, Delete) application for movies using FastAPI. The application allows users to perform CRUD operations on a movie database. Users can create new movies, retrieve existing movies, update movie details, and delete movies from the database.

## Installation

To install the required packages, run the following command in your terminal:

```
pip install -r requirements.txt
```
This will install all the necessary dependencies for running the application.

## Running the Application

To run the application, navigate to the project directory and run the following command in your terminal:

```
uvicorn main:app --reload
```

This will start the FastAPI server, and the application will be available at http://localhost:8000.

## API Endpoints

The following endpoints are available in the application:

- GET /movies: Returns a list of all movies in the database.
- GET /movies/{movie_id}: Returns details for a specific movie.
- POST /movies: Creates a new movie in the database.
- PUT /movies/{movie_id}: Updates details for a specific movie.
- DELETE /movies/{movie_id}: Deletes a specific movie from the database.
- POST /login: Authenticates a user and returns a token for accessing protected endpoints.