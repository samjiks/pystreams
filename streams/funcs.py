import streams as streams

from .utils import map_list, filter_list, sum_list


@streams.Stream.register_func()
def map(self: streams.Stream, func) -> streams.Stream:
    """ Map the data from a list of data"""
    if isinstance(self._ls, list):
        self._ls = map_list(func, self._ls)
    return self


@streams.Stream.register_func()
def filter(self, func):
    """Filter functions"""
    self._ls = filter_list(func, self._ls)
    return self


@streams.Stream.register_func()
def limit(self, max):
    self._ls = self._ls[:max]
    return self


@streams.Stream.register_func()
def sum(self):
    self._ls = sum_list(self._ls)
    return self


@streams.Stream.register_func()
def reset(self):
    self._ls = list()
    return self


@streams.Stream.register_func()
def generate(self, element, times):
    self._ls += [element] * times
    return self
