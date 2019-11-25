
import streams


if __name__ == "__main__":
    list_of_data = [4, 5, 6, 1335]
    actuals = streams.Stream.of(list_of_data).map(lambda x: x * 5). \
                            for_each(print)
