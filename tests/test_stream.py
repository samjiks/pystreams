
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
