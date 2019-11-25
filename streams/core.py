from typing import List, Mapping


class Stream:
    """
    Stream of data from hetergeneous lists
    """

    def __init__(self, ls):
        self._ls = ls

    @classmethod
    def of(cls, ls: List):
        return cls(ls)

    def map(self, func: Mapping):
        self._ls = list(map(func, self._ls))
        return self

    def filter(self, func: Mapping):
        self._ls = list(filter(func, self._ls))
        return self

    def collect(self, func):
        func(self._ls)
        return self._ls
