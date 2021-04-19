import requests


class Accumulator:

    def __init__(self):
        self._count = 0

    @property
    def count(self):
        return self._count

    def add(self, num):
        self._count += num

