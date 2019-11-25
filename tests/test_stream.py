import sys

import pytest

import streams


def test_filter_stream():
    list_of_data = [1, 2, 3, 5, 7]
    actuals = streams.Stream.of(list_of_data).filter(lambda x: x > 5).collect(print)
    assert actuals == [7]


def test_map_stream():
    list_of_data = [1, 2, 3, 5, 7]
    actuals = streams.Stream.of(list_of_data).map(lambda x: x * 5).collect(print)
    assert actuals == [5, 10, 15, 25, 35]


def test_map_filter_stream():
    list_of_data = [1, 2, 3, 5, 7]
    actuals = streams.Stream.of(list_of_data).map(lambda x: x * 5). \
                        filter(lambda x: x > 25).collect(print)
    assert actuals == [35]

def test_sink_stream(capsys):
    list_of_data = [1, 2, 3, 5, 7]
    def pretty_print(ls) -> str:
        return f"Pretty Print: {ls}"

    captured = capsys.readouterr()

    actuals = streams.Stream.of(list_of_data).map(lambda x: x * 5). \
                        filter(lambda x: x > 25).collect(pretty_print)
                    
    assert actuals == [35]

def test_find_first_stream(capsys):
    list_of_data = [1, 2, 3, 5, 7]

    actuals = streams.Stream.of(list_of_data).map(lambda x: x * 5).find_first(). \
                            collect(print)
    assert actuals == [5]


def test_find_first_stream_with_empty_list(capsys):
    list_of_data = []

    with pytest.raises(streams.EmptyListException):
        actuals = streams.Stream.of(list_of_data).map(lambda x: x * 5).find_first(). \
                                collect(print)
        assert actuals == [5]


def test_stream_for_each(capsys):
    list_of_data = [4, 5, 6, 1335]
    actuals = streams.Stream.of(list_of_data).map(lambda x: x * 5). \
                            for_each(print)
    captured = capsys.readouterr()
    assert captured.out == "20\n25\n30\n6675\n"


def test_stream_sorted(capsys):
    list_of_data = [23, 2, 1, 44]
    actuals = streams.Stream.of(list_of_data).sort(). \
                            for_each(print)
    captured = capsys.readouterr()
    assert captured.out == "1\n2\n23\n44\n"


def test_average_for_each(capsys):
    list_of_data = [23, 2, 1, 44]
    actuals = streams.Stream.of(list_of_data).average(). \
                            for_each(print)
    captured = capsys.readouterr()
    assert captured.out == "17.5\n"


  
