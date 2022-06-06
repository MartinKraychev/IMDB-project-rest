from rest_framework.test import APITestCase

from Movies.movie.models import Genre


class GenreTests(APITestCase):
    def setUp(self):
        Genre.objects.create(name='Fantasy')
        Genre.objects.create(name='Action')

    def test_get_api_return_correct_items(self):
        url = 'http://127.0.0.1:8000/api-movies/genre/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.json(), [{'id': 1, 'name': 'Fantasy'}, {'id': 2, 'name': 'Action'}])
