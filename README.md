# Movie Catalogue REST API with Django.
## It works together with the following frontend: https://github.com/MartinKraychev/movies-frontend
## To test locally:
  - Create venv
  - Install dependencies from requirements.txt
  - py manage.py runserver to start the API


### It contains Exdended User, Movie, Genre, Actor and Rating models. All models are implemented with soft delete.

#### Api root:

- Auth:

  POST  -> http://127.0.0.1:8000/api-auth/register/

  POST  -> http://127.0.0.1:8000/api-auth/login/

  POST, GET  -> http://127.0.0.1:8000/api-auth/logout/

- Movies:

   GET, POST -> http://127.0.0.1:8000/api-movies/movies
   
   GET, PUT, DELETE -> http://127.0.0.1:8000/api-movies/movies/{id}
  
  
 - Actors:
 
   GET -> http://127.0.0.1:8000/api-movies/actors
  
- Genre:

  GET -> http://127.0.0.1:8000/api-movies/genre
 
- Rating:

  POST -> http://127.0.0.1:8000/api-movies/rating
