from rest_framework.test import APITestCase

from Movies.movie.models import Genre, Actor, Movie
from Movies.user_auth.models import CustomUser


class MovieTests(APITestCase):
    @classmethod
    def setUpClass(cls):
        super(MovieTests, cls).setUpClass()
        # Create related instances
        actor = Actor.objects.create(first_name='Tom', last_name='Hanks')
        genre = Genre.objects.create(name='Fantasy')
        user = CustomUser.objects.create_user(username='martin', password='123')
        movie = Movie.objects.create(
            name='Movie',
            date='2022-06-03',
            genre=genre,
            poster="https://www.youtube.com/watch?v=iszwuX1AK6A",
            trailer="https://www.youtube.com/watch?",
            user=user
        )

        movie.actors.add(actor)

    def tearDown(self):
        CustomUser.objects.all().delete()
        Movie.objects.all().delete()

    def test_post_movie_data(self):
        login_data = {'username': 'martin', 'password': '123'}

        # Login and get token
        login_url = 'http://127.0.0.1:8000/api-auth/login/'
        response = self.client.post(login_url, login_data, format='json')
        token = response.data['token']
        url = 'http://127.0.0.1:8000/api-movies/movies/'

        data = {
            'name': 'Movie3',
            'date': '2022-06-03',
            'actors': [1, ],
            'genre': 1,
            'poster': "https://www.youtube.com/watch?v=iszwuX1AK6A",
            'trailer': "https://www.youtube.com/watch?",
        }

        # Create movie
        response = self.client.post(url, data, format='json', HTTP_AUTHORIZATION=f'Token {token}')
        print(response)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {'name': 'Movie3', 'date': '2022-06-03',
                                           'actors': [1], 'genre': 1,
                                           'poster': 'https://www.youtube.com/watch?v=iszwuX1AK6A',
                                           'trailer': 'https://www.youtube.com/watch?'})

    def test_get_movie_data(self):
        login_data = {'username': 'martin', 'password': '123'}

        # Login and get token
        login_url = 'http://127.0.0.1:8000/api-auth/login/'
        self.client.post(login_url, login_data, format='json')

        url = 'http://127.0.0.1:8000/api-movies/movies/'

        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [{'id': 1, 'name': 'Movie',
                                            'actors': [{'id': 1, 'first_name': 'Tom',
                                                        'last_name': 'Hanks', 'full_name': 'Tom Hanks'}],
                                            'genre': {'id': 1, 'name': 'Fantasy'},
                                            'poster': 'https://www.youtube.com/watch?v=iszwuX1AK6A'}])

    def test_get_movie_data_by_id(self):
        login_data = {'username': 'martin', 'password': '123'}

        # Login and get token
        login_url = 'http://127.0.0.1:8000/api-auth/login/'
        self.client.post(login_url, login_data, format='json')

        url = 'http://127.0.0.1:8000/api-movies/movies/'

        url_with_id = 'http://127.0.0.1:8000/api-movies/movies/1/'
        response = self.client.get(url_with_id, format='json')
        self.assertEqual(response.json(), {'id': 1, 'name': 'Movie',
                                           'actors': [{'id': 1, 'first_name': 'Tom', 'last_name': 'Hanks',
                                                       'full_name': 'Tom Hanks'}],
                                           'genre': {'id': 1, 'name': 'Fantasy'},
                                           'poster': 'https://www.youtube.com/watch?v=iszwuX1AK6A',
                                           'trailer': 'https://www.youtube.com/watch?',
                                           'user': {'id': 1, 'username': 'martin'}, 'average_rating': 0,
                                           'date': '2022-06-03', 'is_rated': None})
        self.assertEqual(response.status_code, 200)

    def test_delete_movie_data_by_id(self):
        login_data = {'username': 'martin', 'password': '123'}

        # Login and get token
        login_url = 'http://127.0.0.1:8000/api-auth/login/'
        response = self.client.post(login_url, login_data, format='json')
        token = response.data['token']

        url = 'http://127.0.0.1:8000/api-movies/movies/'
        data = {
            'name': 'Movie2',
            'date': '2022-06-03',
            'actors': [1, ],
            'genre': 1,
            'poster': "https://www.youtube.com/watch?v=iszwuX1AK6A",
            'trailer': "https://www.youtube.com/watch?",
        }

        # Create movie
        self.client.post(url, data, format='json', HTTP_AUTHORIZATION=f'Token {token}')
        url_with_id = 'http://127.0.0.1:8000/api-movies/movies/2/'
        response = self.client.delete(url_with_id, format='json', HTTP_AUTHORIZATION=f'Token {token}')
        self.assertEqual(response.status_code, 204)
        res = self.client.get(url_with_id, format='json', HTTP_AUTHORIZATION=f'Token {token}')
        self.assertEqual(res.status_code, 404)

    def test_update_movie_data_by_id(self):
        login_data = {'username': 'martin', 'password': '123'}

        # Login and get token
        login_url = 'http://127.0.0.1:8000/api-auth/login/'
        response = self.client.post(login_url, login_data, format='json')
        token = response.data['token']

        url_with_id = 'http://127.0.0.1:8000/api-movies/movies/1/'
        data = {
            'name': 'Movie2',
        }
        response = self.client.patch(url_with_id, data, format='json', HTTP_AUTHORIZATION=f'Token {token}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'name': 'Movie2', 'date': '2022-06-03',
                                           'actors': [1], 'genre': 1,
                                           'poster': 'https://www.youtube.com/watch?v=iszwuX1AK6A',
                                           'trailer': 'https://www.youtube.com/watch?'})
