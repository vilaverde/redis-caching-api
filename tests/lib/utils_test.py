from unittest.mock import patch
from unittest import TestCase
from app.lib.errors import BadRequestError
from app.lib.utils import extract_swapi_id, extract_swapi_ids_from_list, \
                          compose_url, redis_data_fetcher
from ..support.helpers.mock_redis import MockRedis
from ..support.helpers.mock_swapi import mock_requests_get
from os import environ


# instance to keep MockRedis alive after request
redis_instance = MockRedis()


class UtilsTest(TestCase):

    def test_extract_swapi_id(self):
        swapi_url = 'https://swapi.dev/api/starwars/people/123'
        extracted_id = extract_swapi_id(swapi_url)

        self.assertEqual(extracted_id, '123')

    def test_extract_swapi_ids_from_list(self):
        swapi_url_list = [
            'https://swapi.dev/api/starwars/people/111',
            'https://swapi.dev/api/starwars/people/222',
        ]
        extracted_ids = extract_swapi_ids_from_list(swapi_url_list)

        self.assertEqual(extracted_ids, ['111', '222'])

    def test_compose_url(self):
        base_url = environ['SWAPI_URL']
        expected_url = base_url + '/starwars/films/1'
        composed = compose_url('starwars', 'films', '1')

        self.assertEqual(composed, expected_url)

    @patch('requests.get', mock_requests_get)
    @patch('redis.Redis.from_url', MockRedis.from_url)
    def test_redis_data_fetcher_new(self):
        url = 'https://swapi.dev/api/people/1'
        json_response = redis_data_fetcher(url)

        self.assertEqual(type(json_response), dict)

    @patch('requests.get', mock_requests_get)
    @patch('redis.Redis.from_url', redis_instance.fake_from_url)
    def test_redis_data_fetcher_cached(self):
        url = 'https://swapi.dev/api/people/1'
        redis_data_fetcher(url)
        json_response = redis_data_fetcher(url)

        self.assertEqual(type(json_response), dict)

    @patch('requests.get', mock_requests_get)
    @patch('redis.Redis.from_url', MockRedis.from_url)
    def test_redis_data_fail(self):
        url = 'https://swapi.dev/api/films/999'

        with self.assertRaises(BadRequestError):
            redis_data_fetcher(url)
