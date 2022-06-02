# Movie Catalogue REST API with Django
## This is a backend project set up to work with frontend module uploaded here : https://github.com/MartinKraychev/IMDB-frontend

To test locally:
- Create venv
- Install dependencies

It contains Exdended User, Movie, Genre, Actor and Rating models. All models are implemented with soft delete.

Api root:

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
