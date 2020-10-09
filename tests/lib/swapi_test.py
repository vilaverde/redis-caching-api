from unittest.mock import patch
from unittest import TestCase
from app.lib.swapi import get_film, get_person, get_people, get_formatted_film
from ..support.helpers.mock_redis import MockRedis
from ..support.helpers.mock_swapi import mock_requests_get


class SwapiTest(TestCase):

    @patch('requests.get', mock_requests_get)
    @patch('redis.Redis.from_url', MockRedis.from_url)
    def test_get_film(self):
        rjson = get_film('1')

        self.assertEqual(type(rjson['title']), str)
        self.assertEqual(type(rjson['opening_crawl']), str)
        self.assertEqual(type(rjson['director']), str)
        self.assertEqual(type(rjson['producer']), str)
        self.assertEqual(type(rjson['release_date']), str)
        self.assertEqual(type(rjson['characters']), list)

        for character in rjson['characters']:
            self.assertRegex(character, '^https?://')

    @patch('requests.get', mock_requests_get)
    @patch('redis.Redis.from_url', MockRedis.from_url)
    def test_get_person(self):
        rjson = get_person('1')

        self.assertEqual(type(rjson['name']), str)
        self.assertEqual(type(rjson['height']), str)
        self.assertEqual(type(rjson['mass']), str)
        self.assertEqual(type(rjson['hair_color']), str)
        self.assertEqual(type(rjson['skin_color']), str)
        self.assertEqual(type(rjson['eye_color']), str)
        self.assertEqual(type(rjson['birth_year']), str)
        self.assertEqual(type(rjson['gender']), str)
        self.assertEqual(type(rjson['homeworld']), str)
        self.assertEqual(type(rjson['films']), list)
        self.assertEqual(type(rjson['species']), list)
        self.assertEqual(type(rjson['vehicles']), list)
        self.assertEqual(type(rjson['starships']), list)
        self.assertEqual(type(rjson['created']), str)
        self.assertEqual(type(rjson['edited']), str)
        self.assertEqual(type(rjson['url']), str)

    @patch('requests.get', mock_requests_get)
    @patch('redis.Redis.from_url', MockRedis.from_url)
    def test_get_people(self):
        json_list = get_people(['1', '2'])

        for rjson in json_list:
            self.assertEqual(type(rjson['name']), str)
            self.assertEqual(type(rjson['height']), str)
            self.assertEqual(type(rjson['mass']), str)
            self.assertEqual(type(rjson['hair_color']), str)
            self.assertEqual(type(rjson['skin_color']), str)
            self.assertEqual(type(rjson['eye_color']), str)
            self.assertEqual(type(rjson['birth_year']), str)
            self.assertEqual(type(rjson['gender']), str)
            self.assertEqual(type(rjson['homeworld']), str)
            self.assertEqual(type(rjson['films']), list)
            self.assertEqual(type(rjson['species']), list)
            self.assertEqual(type(rjson['vehicles']), list)
            self.assertEqual(type(rjson['starships']), list)
            self.assertEqual(type(rjson['created']), str)
            self.assertEqual(type(rjson['edited']), str)
            self.assertEqual(type(rjson['url']), str)

    @patch('requests.get', mock_requests_get)
    @patch('redis.Redis.from_url', MockRedis.from_url)
    def test_get_formatted_film(self):
        rjson = get_formatted_film('1')

        self.assertEqual(type(rjson['title']), str)
        self.assertEqual(type(rjson['id']), str)
        self.assertEqual(type(rjson['opening_crawl']), str)
        self.assertEqual(type(rjson['director']), str)
        self.assertEqual(type(rjson['producer']), str)
        self.assertEqual(type(rjson['release_date']), str)
        self.assertEqual(type(rjson['characters']), list)

        for character in rjson['characters']:
            self.assertNotRegex(character, '^https?://')
