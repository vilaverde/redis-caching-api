#!/usr/bin/python3

import re
import os


def extract_swapi_id(url):
    '''
    Extracts id of SWAPI URL

    Parameters:
        url (str): target url

    Returns
      first matched string group
    '''
    return re.search('(?<=\\/)\\d+(?=\\/$|$)', url).group(0)


def extract_swapi_ids_from_list(url_list):
    '''
    Extracts ids of list of SWAPI URL

    Parameters:
        url ([str]): list of target urls

    Returns
      first matched string group
    '''
    return [extract_swapi_id(url) for url in url_list]


def compose_url(*args):
    '''
    Build URL that starts with SWAPI_URL and ends with slash-separated
    parameters

    Parameters:
        args (tuple of str): tuple of strings to be concatenated

    Returns
      string object containing built url
    '''
    swapi_url = os.environ['SWAPI_URL']
    return '/'.join(list((swapi_url,) + args))
