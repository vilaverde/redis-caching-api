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


def get_formatted_film(id):
    '''
    Gets film data from SWAPI

    Parameters:
        id (int): film resource SWAPI identificator

    Returns
        Formatted SWAPI data dict
    '''
    film = get_film(id)
    people_ids = extract_swapi_ids_from_list(film['characters'])
    characters = [person['name'] for person in get_people(people_ids)]

    return format_film_data(id, film, characters)


def get_all_formatted_films():
    '''
    Gets film data from SWAPI

    Parameters:
        None

    Returns
        Formatted SWAPI data dict
    '''

    films = get_film(None).get('results')
    film_list = []
    for i in range(len(films)):
        people_ids = extract_swapi_ids_from_list(films[i]['characters'])
        characters = [person['name'] for person in get_people(people_ids)]
        film_list.append(format_film_data(i + 1, films[i], characters))

    return film_list


def format_film_data(id, film, characters):
    '''
    Formats film dict

    Parameters:
        id (str or int): film resource SWAPI identificator
        film (dict): filme resource from SWAPI
        characters ([str]): a list of character names
    '''
    return {
        'title': film['title'],
        'id': str(id),
        'opening_crawl': film['opening_crawl'],
        'director': film['director'],
        'producer': film['producer'],
        'release_date': film['release_date'],
        'characters': characters,
    }
