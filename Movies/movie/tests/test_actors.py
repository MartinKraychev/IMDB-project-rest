from rest_framework.test import APITestCase

from Movies.movie.models import Actor


class ActorsTests(APITestCase):
    def setUp(self):
        Actor.objects.create(first_name='Tom', last_name='Hanks')
        Actor.objects.create(first_name='Vin', last_name='Diezel')

    def test_get_api_return_correct_items(self):
        url = 'http://127.0.0.1:8000/api-movies/actors/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.json(),
                         [{'id': 1, 'first_name': 'Tom', 'last_name': 'Hanks', 'full_name': 'Tom Hanks'},
                          {'id': 2, 'first_name': 'Vin', 'last_name': 'Diezel', 'full_name': 'Vin Diezel'}])
