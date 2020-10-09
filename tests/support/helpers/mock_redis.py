#!/usr/bin/python3

class MockRedis():

    @classmethod
    def from_url(cls, arg):
        return cls()

    def __init__(self):
        self.data = {}

    def get(self, key):
        return self.data.get(key)

    def set(self, key, value):
        self.data[key] = value
        return True
