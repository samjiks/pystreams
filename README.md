# PyStreams

A library to filter out your data from your lists. Useful for streaming data and store data into storages

## Examples

'''

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
'''