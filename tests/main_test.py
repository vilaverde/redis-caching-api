from unittest.mock import patch
from unittest import TestCase
from app.main import app
from .support.helpers.mock_redis import MockRedis
from .support.helpers.mock_swapi import mock_requests_get


class MainTest(TestCase):

    def setUp(self):
        self.app = app.test_client()

    @patch('requests.get', mock_requests_get)
    @patch('redis.Redis.from_url', MockRedis.from_url)
    def test_movies(self):
        response = self.app.get('/starwars/movies?id=1')

        self.assertEqual(response.status_code, 200)

        rjson = response.json
        self.assertEqual(type(rjson['title']), str)
        self.assertEqual(type(rjson['id']), str)
        self.assertEqual(type(rjson['opening_crawl']), str)
        self.assertEqual(type(rjson['director']), str)
        self.assertEqual(type(rjson['producer']), str)
        self.assertEqual(type(rjson['release_date']), str)
        self.assertEqual(type(rjson['characters']), list)

        for character in rjson['characters']:
            self.assertNotRegex(character, '^https?://')

    @patch('requests.get', mock_requests_get)
    @patch('redis.Redis.from_url', MockRedis.from_url)
    def test_all_movies(self):
        response = self.app.get('/starwars/movies')

        self.assertEqual(response.status_code, 200)

        for rjson in response.json:
            self.assertEqual(type(rjson['title']), str)
            self.assertEqual(type(rjson['id']), str)
            self.assertEqual(type(rjson['opening_crawl']), str)
            self.assertEqual(type(rjson['director']), str)
            self.assertEqual(type(rjson['producer']), str)
            self.assertEqual(type(rjson['release_date']), str)
            self.assertEqual(type(rjson['characters']), list)

            for character in rjson['characters']:
                self.assertNotRegex(character, '^https?://')

    @patch('requests.get', mock_requests_get)
    @patch('redis.Redis.from_url', MockRedis.from_url)
    def test_bad_request(self):
        response = self.app.get('/starwars/movies?id=999')

        self.assertEqual(response.status_code, 400)
        self.assertNotEqual(response.json['message'], None)

    def test_not_found(self):
        response = self.app.get('/')

        self.assertEqual(response.status_code, 404)
        self.assertNotEqual(response.json['message'], None)
