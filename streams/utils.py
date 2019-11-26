from typing import List

import streams


def map_list(func: streams.Stream, ls: List) -> List:
    """util to help map function from a list"""
    return list(map(func, ls))


def filter_list(func: streams.Stream, ls: List) -> List:
    """util to help filter function from a list"""
    return list(filter(func, ls))


def sum_list(ls: List) -> List:
    """util to help filter function from a list"""
    return sum([element for element in ls if isinstance(element, int)])


def is_list(ls: List) -> bool:
    """ check if it is a list """
    return isinstance(ls, list)
