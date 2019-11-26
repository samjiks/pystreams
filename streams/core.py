import functools
from typing import List

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

    def find_first(self):
        """Get the first element of the list"""
        if len(self._ls) > 1:
            self._ls = self._ls[:1]
            return self

        raise errors.EmptyListException("Find First Don't have enough elements")

    def for_each(self, func):
        """ print each element """
        if isinstance(self._ls, list):
            for ls in self._ls:
                func(ls)
        else:
            func(self._ls)
        return self

    def sort(self):
        """ print each element """
        self._ls = sorted(self._ls)
        return self

    def average(self):
        """ Get the average of the list"""
        self._ls = sum(self._ls) / len(self._ls)
        return self

    def collect(self, func):
        """ Collect and output the lists """
        func(self._ls)
        return self._ls

    @classmethod
    def register_func(cls):
        """
        Register an external function to add more streams module
        
        >>> @streams.Stream.register_func()
        >>> def filter(self, func):
        >>>     self._ls = filter_list(func, self._ls)
        >>>     return self

        """
        def wrapper(func):
            @functools.wraps(func)
            def func_wrapper(*args, **kwargs):
                return func(*args, **kwargs)
            setattr(cls, func.__name__, func_wrapper)
        return wrapper
