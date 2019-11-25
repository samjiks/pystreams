  [![Build Status](https://travis-ci.org/samjiks/pystreams.svg?branch=master)](https://travis-ci.org/samjiks/pystreams)

# PyStreams

A library to filter out your data from your lists. Useful for streaming data and store data into storages. An Idea from Java8 Streams.

## Examples



    import streams

    # Filter data
    list_of_data = [1, 2, 3, 5, 7]
    actuals = streams.Stream.of(list_of_data).filter(lambda x: x > 5).collect(print)
    assert actuals == [7]


    # Map data
    list_of_data = [1, 2, 3, 5, 7]
    actuals = streams.Stream.of(list_of_data).map(lambda x: x * 5).collect(print)
    assert actuals == [5, 10, 15, 25, 35]


    # map and filter data
    list_of_data = [1, 2, 3, 5, 7]
    actuals = streams.Stream.of(list_of_data).map(lambda x: x * 5). \
                        filter(lambda x: x > 25).collect(print)
    assert actuals == [35]

    # find first
    list_of_data = [1, 2, 3, 5, 7]
    actuals = streams.Stream.of(list_of_data).map(lambda x: x * 5).find_first(). \
                            collect(print)
    assert actuals == [5]

    # using for_each 
    list_of_data = [4, 5, 6, 1335]
    actuals = streams.Stream.of(list_of_data).map(lambda x: x * 5). \
                            for_each(print)    
    Output:
    
    20
    25
    30
    6675

