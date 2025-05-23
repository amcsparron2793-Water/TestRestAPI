import unittest
import json  # Use Python's built-in JSON module for consistency
from TestRestAPI.TestRestAPI import app


class TestGetApiKey(unittest.TestCase):
    def setUp(self):
        # Use the actual app from TestRestAPI
        self.app = app
        self.client = self.app.test_client()
        self.app.testing = True #.config['TESTING'] = True

    def test_get_api_key_success(self):
        # Test case: Valid credentials
        response = self.client.post('/get_api_key', json={'username': 'test', 'password': 'pass123'})
        self.assertEqual(response.status_code, 200,
                         msg="The endpoint should return status 200 for valid credentials.")
        data = json.loads(response.get_data(as_text=True))
        self.assertIn('api_key', data,
                      msg="'api_key' not found in the response.")

    def test_get_api_key_no_username(self):
        # Test case: Missing username in the payload
        response = self.client.post('/get_api_key', json={'password': 'pass123'})
        self.assertEqual(response.status_code, 400,
                         msg="The endpoint should return status 400 for missing username.")

    def test_get_api_key_no_password(self):
        # Test case: Missing password in the payload
        response = self.client.post('/get_api_key', json={'username': 'test'})
        self.assertEqual(response.status_code, 400,
                         msg="The endpoint should return status 400 for missing password.")

    def test_get_api_key_no_credentials(self):
        # Test case: Empty payload
        response = self.client.post('/get_api_key', json={})
        self.assertEqual(response.status_code, 400,
                         msg="The endpoint should return status 400 for missing credentials.")

    def test_invalid_endpoint(self):
        # test case: invalid endpoint
        response = self.client.post('/invalid_endpoint', json={'username': 'test', 'password': 'pass123'})
        self.assertEqual(response.status_code, 404,
                         msg="The endpoint should return status 404 for invalid endpoint.")


if __name__ == '__main__':
    unittest.main()
