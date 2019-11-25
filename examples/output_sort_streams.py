import streams

if __name__ == "__main__":
    list_of_data = [5, 6, 190, 5, 7]
    result = streams.Stream.of(list_of_data).sort().for_each(print)
