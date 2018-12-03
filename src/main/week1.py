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


def load_int_data(filepath):
    data = load_data(filepath)
    return [float(_) for _ in data]

def load_data(filepath):
    with open(filepath, 'r') as file:
        data = file.readlines()
    return data


if __name__ == '__main__':

    root = os.path.dirname(
        os.path.dirname(
            os.path.dirname(
                os.path.abspath(__file__)
            )
        )
    )

    print(day2(
        load_data('{}/inputs/day2.txt'.format(root))
        ))

