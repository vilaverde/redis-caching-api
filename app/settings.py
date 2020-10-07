#!/usr/bin/python3

class default(object):
    DEBUG = False
    TESTING = False


class production(default):
    pass


class development(default):
    DEVELOPMENT = True
    DEBUG = True


class testing(default):
    TESTING = True
