#!/usr/bin/python3

import os
import json
from .mock_response import MockResponse


def dict_key(filename):
    no_ext_filename = filename[:filename.index('.')]
    return '/'.join([os.environ['SWAPI_URL']] + no_ext_filename.split('_'))


def load_fixtures_dict():
    dirpath = './tests/support/fixtures/swapi/'

    fixtures_dict = {}
    for filename in os.listdir(dirpath):
        with open(dirpath + filename, 'r') as file:
            content = file.read()

        key = dict_key(filename)
        fixtures_dict[key] = json.loads(content)

    return fixtures_dict


def mock_requests_get(*args, **kwargs):
    fixtures_dict = load_fixtures_dict()
    if args[0] in fixtures_dict.keys():
        return MockResponse(fixtures_dict[args[0]], 200)

    return MockResponse(None, 404)
