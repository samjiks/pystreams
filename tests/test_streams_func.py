import streams

def test_register_func():
    list_of_data = [1, 2, 3, 5, 7]
    actuals = streams.Stream.of(list_of_data). \
        filter(lambda x: x > 4).collect(print)
    assert actuals == [5, 7]

def test_register_func_sum():
    list_of_data = [1, 2, 3, 5, 7]
    actuals = streams.Stream.of(list_of_data). \
        sum().collect(print)
    assert actuals == 18

def test_register_func_sum_with_string():
    list_of_data = [1, 2, 3, 5, "7"]
    actuals = streams.Stream.of(list_of_data). \
        sum().collect(print)
    assert actuals == 11
