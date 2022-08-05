# Movie Catalogue REST API with Django.
It works together with the following frontend: https://github.com/MartinKraychev/movies-frontend.

It contains Exdended User, Movie, Genre, Actor and Rating models. All models are implemented with soft delete.

Django-filter is used for searching.

The API is deployed in Heroku.

## To test locally:

Clone the project
  ```bash
  git clone https://github.com/MartinKraychev/Movie-Catalogue-REST.git
```
  Go to the project directory
```bash
  cd Movies
```
Install dependencies
```bash
  pip install -r requirements.txt
```
Start the server
```bash
  py manage.py runserver
```

## Environment Variables
You need the following env variables if you want to test it locally:

`DEBUG=True`

`APP_ENVIRONMENT=Development`

`DJANGO_ALLOWED_HOSTS="localhost 127.0.0.1"`

`SECRET_KEY={secret_key}`

`SQL_ENGINE=django.db.backends.postgresql`

`SQL_DATABASE={db_name}`

`SQL_USER={db_user}`

`SQL_PASSWORD={db_password}`

`SQL_HOST={db_host}`

`SQL_PORT=5432`



#### Api root:
#### The deployed url is https://django-movies-rest.herokuapp.com and for local testing use http://127.0.0.1:8000


- Auth:

  ```http
    POST  {url}/api-auth/register/
  ```
  
  ```http
    POST  {url}/api-auth/login/
  ```
  
  ```http
    POST, GET  {url}/api-auth/logout/
  ```
  
- Movies:
  
  ```http
    GET, POST  {url}/api-movies/movies/
  ```
   
  ```http 
    GET, PUT, DELETE {url}/api-movies/movies/{id}/
  ```
   
  ```http
    GET for search {url}/api-movies/movies/?{field}={fieldValue}/
  ```
  
- Actors:
 
  ```http
    GET {url}/api-movies/actors/
  ```
  
- Genre:

  ```http
    GET {url}/api-movies/genre/
  ```
  
- Rating:

  ```http
    POST {url}/api-movies/rating/
  ```
