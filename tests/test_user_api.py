import unittest
import requests
from config import Config
from tests.test_mock_data import MockData

class TestUserMicroServices(unittest.TestCase):

    def test_sign_up(self):
        sign_up_api_endpoint = '{}{}'.format(Config.BASE_URL, Config.SIGN_UP)
        response = requests.post(sign_up_api_endpoint,
                                 json=MockData.mock_user_data)
        self.assertEqual(response.status_code, 201)

    def test_sign_in(self):
        sign_in_api_endpoint = '{}{}'.format(Config.BASE_URL, Config.SIGN_IN)
        response = requests.post(sign_in_api_endpoint,
                                 json=MockData.mock_sign_in_data)
        self.assertEqual(response.status_code, 200)

    def test_profile(self):
        profile_api_endpoint = '{}{}'.format(
            Config.BASE_URL, MockData.mock_profile_endpoint)
        response = requests.get(profile_api_endpoint,
                                headers=MockData.mock_request_headers)
        self.assertEqual(response.status_code, 200)

    def test_update_profile(self):
        update_profile_api_endpoint = '{}{}'.format(
            Config.BASE_URL, MockData.mock_update_profile_endpoint)

        response = requests.put(update_profile_api_endpoint,
                                headers=MockData.mock_request_headers, json=MockData.mock_update_user_data)
        self.assertEqual(response.status_code, 200)

    def test_change_password(self):
        change_password_api_endpoint = '{}{}'.format(
            Config.BASE_URL, MockData.mock_change_password_endpoint)

        response = requests.put(change_password_api_endpoint,
                                headers=MockData.mock_request_headers, json=MockData.mock_change_password_data)
        self.assertEqual(response.status_code, 200)

    def test_delete_account(self):
        delete_account_api_endpoint = '{}{}'.format(
            Config.BASE_URL, MockData.mock_delete_account_endpoint)

        response = requests.delete(delete_account_api_endpoint,
                                   headers=MockData.mock_request_headers)
        self.assertEqual(response.status_code, 200)