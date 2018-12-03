from itertools import cycle, starmap, compress
import os

from src.main.utils import load_data, load_int_data


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


def day2(data):

    counts = {
        1: 0,
        2: 0,
        3: 0
    }

    for id_string in data:
        sub_counts = {
            1: False,
            2: False,
            3: False
        }
        char_set = set(id_string)
        for character in char_set:
            sub_counts[id_string.count(character)] = True

        for key, value in sub_counts.items():
            if value:
                counts[key] += 1

    return counts[2] * counts[3]


def _compare_func(a, b):
    return a == b


def _compare_string(a_string, b_string):
    trues = starmap(_compare_func, zip(a_string, b_string))
    return list(compress(a_string, trues))


def day2_part2(data):

    compare_length = len(data[0])

    for index, a_id in enumerate(data):
        sub_data = data[(index + 1):]

        for b_id in sub_data:
            compare_output = _compare_string(a_id, b_id)
            if len(compare_output) >= compare_length - 1:
                return ''.join(compare_output)


if __name__ == '__main__':

    root = os.path.dirname(
        os.path.dirname(
            os.path.dirname(
                os.path.dirname(
                    os.path.abspath(__file__)
                )
            )
        )
    )

    print(day2_part2(
        load_data('{}/inputs/day2.txt'.format(root))
    ))
