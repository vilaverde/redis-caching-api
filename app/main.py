#!/usr/bin/python3

import os
from flask import Flask, jsonify, request
from .lib.swapi import get_formatted_film, get_all_formatted_films
from .lib.errors import BadRequestError


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])


@app.route('/starwars/movies', methods=['GET'])
def movies():
    movie_id = request.args.get('id')
    if not movie_id:
        return jsonify(get_all_formatted_films()), 200
    try:
        return jsonify(get_formatted_film(movie_id)), 200
    except BadRequestError as err:
        return jsonify({"message": err.message}), 400


@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"message": "Invalid URL"}), 404
