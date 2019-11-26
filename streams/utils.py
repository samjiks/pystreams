from typing import List

import streams


def map_list(func: streams.Stream, ls: List) -> List:
    return list(map(func, ls))


def filter_list(func: streams.Stream, ls: List) -> List:
    return list(filter(func, ls))


def is_list(ls: List) -> bool:
    return isinstance(ls, list)
