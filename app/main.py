#!/usr/bin/python3

import os
from flask import Flask, jsonify, request
from .lib.swapi import get_formatted_film

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])


@app.route('/starwars/movies', methods=['GET'])
def movies():
    return jsonify(get_formatted_film(request.args.get('id')))


@app.errorhandler(404)
def page_not_found(e):
    return jsonify({}), 404
