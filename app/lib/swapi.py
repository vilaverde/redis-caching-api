#!/usr/bin/python3

from .utils import compose_url, extract_swapi_ids_from_list, redis_data_fetcher


def get_film(id):
    '''
    Gets film data from SWAPI

    Parameters:
        id (str): film resource SWAPI identificator

    Returns
      SWAPI data dict
    '''
    url = compose_url('films', id)
    return redis_data_fetcher(url)


def get_person(id):
    '''
    Gets person data from SWAPI

    Parameters:
        id (str): film resource SWAPI identificator

    Returns
      SWAPI data dict
    '''
    url = compose_url('people', id)
    return redis_data_fetcher(url)


def get_people(ids):
    '''
    Gets multiple person data from SWAPI

    Parameters:
        id ([str]): list of film resource SWAPI identificator

    Returns
      List of SWAPI data dict
    '''
    return [get_person(id) for id in ids]


def get_formatted_film(id, characters_name=True):
    '''
    Gets film data from SWAPI

    Parameters:
        id (int): film resource SWAPI identificator
        characters_name (boolean): include list of character names instead of
                                   resource url

    Returns
      Formatted SWAPI data dict
    '''

    film = get_film(id)
    people_ids = extract_swapi_ids_from_list(film['characters'])
    characters = [person['name'] for person in get_people(people_ids)]

    return {
        'title': film['title'],
        'id': id,
        'opening_crawl': film['opening_crawl'],
        'director': film['director'],
        'producer': film['producer'],
        'release_date': film['release_date'],
        'characters': characters,
    }
