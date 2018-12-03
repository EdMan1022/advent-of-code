from itertools import cycle
import os


def day0(data):
    return sum(data)


def day1(data):

    cached_sums = set([0])
    _sum = 0

    for value in cycle(data):

        _sum = value + _sum

        if _sum in cached_sums:
            return _sum
    
        cached_sums.add(_sum)


def load_data(filepath):
    with open(filepath, 'r') as file:
        data = file.readlines()
    return [float(_) for _ in data]


if __name__ == '__main__':

    root = os.path.dirname(
        os.path.dirname(
            os.path.dirname(
                os.path.abspath(__file__)
            )
        )
    )

    print(day1(
        load_data('{}/inputs/day1.txt'.format(root))
        ))

