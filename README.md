# Movie Catalogue REST API with Django.
## It works together with the following frontend: https://github.com/MartinKraychev/movies-frontend. The API is deployed in Heroku.

## To test locally:
  - Create venv
  - Install dependencies from requirements.txt
  - py manage.py runserver to start the API


### It contains Exdended User, Movie, Genre, Actor and Rating models. All models are implemented with soft delete.

#### Api root:
#### The deployed url is https://django-movies-rest.herokuapp.com and for locally testing use http://127.0.0.1:8000


- Auth:

  POST  -> {url}/api-auth/register/

  POST  -> {url}/api-auth/login/

  POST, GET  -> {url}/api-auth/logout/

- Movies:

   GET, POST -> {url}/api-movies/movies/
   
   GET, PUT, DELETE -> {url}/api-movies/movies/{id}/
  
   GET for search -> {url}/api-movies/movies/?{field}={fieldValue}/
  
 - Actors:
 
   GET -> {url}/api-movies/actors/
  
- Genre:

  GET -> {url}/api-movies/genre/
 
- Rating:

  POST -> {url}/api-movies/rating/
