from rest_framework.test import APITestCase

from Movies.user_auth.models import CustomUser


class AuthTests(APITestCase):
    def setUp(self):
        """
        Create account
        """
        url = 'http://127.0.0.1:8000/api-auth/register/'
        data = {'username': 'martin', 'password': '123'}
        self.client.post(url, data, format='json')

    def test_created_account(self):
        self.assertEqual(CustomUser.objects.count(), 1)
        self.assertEqual(CustomUser.objects.get().username, 'martin')

    def test_duplicate_account_returns_error(self):
        url = 'http://127.0.0.1:8000/api-auth/register/'
        data = {'username': 'martin', 'password': '123'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 400)

    def test_login_with_valid_credentials(self):
        url = 'http://127.0.0.1:8000/api-auth/login/'
        data = {'username': 'martin', 'password': '123'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('token' in response.data)

    def test_login_with_invalid_credentials(self):
        url = 'http://127.0.0.1:8000/api-auth/login/'
        data = {'username': 'martin', 'password': '1234'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertFalse('token' in response.data)

    def test_logout_delete_token_(self):
        url = 'http://127.0.0.1:8000/api-auth/login/'
        data = {'username': 'martin', 'password': '123'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('token' in response.data)
        token = response.data['token']

        url = 'http://127.0.0.1:8000/api-auth/logout/'
        response = self.client.post(url, HTTP_AUTHORIZATION=f'Token {token}')
        self.assertEqual(response.status_code, 200)
        self.assertFalse('token' in response.data)
