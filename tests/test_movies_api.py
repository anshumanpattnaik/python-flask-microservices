import unittest
import requests
from config import Config
from tests.test_mock_data import MockData

class TestMoviesMicroServices(unittest.TestCase):

    def test_add_movie(self):
        add_movie_api_endpoint = '{}{}'.format(
            Config.BASE_URL, MockData.mock_add_movie_endpoint)
        response = requests.post(add_movie_api_endpoint,
                                 headers=MockData.mock_request_headers,
                                 json=MockData.mock_movie_data)
        self.assertEqual(response.status_code, 201)

    def test_fetch_movies(self):
        fetch_movies_api_endpoint = '{}{}'.format(
            Config.BASE_URL, MockData.mock_fetch_movies_endpoint)
        response = requests.get(fetch_movies_api_endpoint,
                                headers=MockData.mock_request_headers)
        self.assertEqual(response.status_code, 200)

    def test_search_movie(self):
        search_movie_api_endpoint = '{}{}'.format(
            Config.BASE_URL, MockData.mock_search_movie_endpoint)
        response = requests.get(search_movie_api_endpoint,
                                headers=MockData.mock_request_headers)
        self.assertEqual(response.status_code, 200)

    def test_delete_movie(self):
        delete_movie_api_endpoint = '{}{}'.format(
            Config.BASE_URL, MockData.mock_delete_movie_endpoint)
        response = requests.delete(delete_movie_api_endpoint,
                                headers=MockData.mock_request_headers)
        self.assertEqual(response.status_code, 200)

    def test_favourite_movies(self):
        favourite_movie_api_endpoint = '{}{}'.format(
            Config.BASE_URL, MockData.mock_favourite_movies_endpoint)
        response = requests.get(favourite_movie_api_endpoint,
                                headers=MockData.mock_request_headers)
        self.assertEqual(response.status_code, 200)

    def test_add_to_favourite(self):
        add_to_favourite_movie_api_endpoint = '{}{}'.format(
            Config.BASE_URL, MockData.mock_add_to_favourite_movie_endpoint)
        response = requests.put(add_to_favourite_movie_api_endpoint,
                                headers=MockData.mock_request_headers,
                                json=MockData.mock_favourite_data)
        self.assertEqual(response.status_code, 200)