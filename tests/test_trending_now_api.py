import unittest
import requests
from config import Config
from tests.test_mock_data import MockData

class TestTrendingNowMicroServices(unittest.TestCase):
    
    def test_trending_now(self):
        trending_now_api_endpoint = '{}{}'.format(
            Config.BASE_URL, MockData.mock_trending_now_endpoint)
        response = requests.get(trending_now_api_endpoint,
                                headers=MockData.mock_request_headers)
        self.assertEqual(response.status_code, 200)