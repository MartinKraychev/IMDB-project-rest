# Movie Catalogue REST API with Django as Backend and JS, HTML and CSS as Frontend.
## Page lib is used for routing and Lit-Html for templating.


## To test locally: Use VS Code to run both services

### For the Backend
- Create venv
- Install dependencies from requirements.txt
- py manage.py runserver to start the API

### For the Frontend:
  - npm i to install dependencies.
  - npm start to start the server.

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
