from typing import List, Mapping

from . import errors


class Stream:
    """
    Stream of data from homogeneous lists

    Streams are built on previous functions passing data to
    lower functions connecting the lower functions to get
    refined outputs.
    """

    def __init__(self, ls):
        self._ls = ls

    @classmethod
    def of(cls, ls: List):
        """ Provide a class instance way of taking lists of data """
        return cls(ls)

    def map(self, func: Mapping):
        """ Map the data from a list of data"""
        self._ls = list(map(func, self._ls))
        return self

    def filter(self, func: Mapping):
        """Filter functions"""
        self._ls = list(filter(func, self._ls))
        return self

    def find_first(self):
        """Get the first element of the list"""
        if len(self._ls) > 1:
            self._ls = self._ls[:1]
            return self

        raise errors.EmptyListException("Find First Don't have enough elements")

    def for_each(self, func):
        """ print each element """
        for ls in self._ls:
            func(ls)

    def collect(self, func):
        """ Collect and output the lists """
        func(self._ls)
        return self._ls
