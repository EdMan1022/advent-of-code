def day1(data):
    return sum([int(_) for _ in data])


def day2(data):
    return None


def load_data(filepath):
    with open(filepath, 'r') as file:
        data = file.readlines()
    return data


if __name__ == '__main__':
    print(day1(load_data('inputs/day1.txt')))
