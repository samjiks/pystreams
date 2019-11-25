from streams import Stream

if __name__ == "__main__":
    list_of_data = [5, 6, 190, 5, 7]
    actuals = Stream.of(list_of_data).filter(lambda x: x > 5).collect(print)
    assert actuals == [7]
