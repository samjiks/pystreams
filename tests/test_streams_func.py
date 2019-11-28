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

def test_register_func_generate():
    list_of_data = [1, 2, 3, 5, 7]
    actuals = streams.Stream.of(list_of_data). \
        generate(element="element", times=10).collect(print)
    assert actuals == [1, 2, 3, 5, 7, 'element', 'element', 'element', 'element', 'element', 'element', 'element', 'element', 'element', 'element']

def test_register_func_reset_generate():
    list_of_data = [1, 2, 3, 5, 7]
    actuals = streams.Stream.of(list_of_data).reset(). \
        generate(element=int("1"), times=4).collect(print)
    assert actuals == [1, 1, 1, 1]

def test_register_func_reset_generate_sum():
    list_of_data = [1, 2, 3, 5, 7]
    actuals = streams.Stream.of(list_of_data).reset(). \
        generate(element=int("1"), times=4).sum().collect(print)
    assert actuals == 4
