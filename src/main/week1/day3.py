import numpy as np

def day3_parser(data):

    output = []

    for _ in data:
        _split = _.split(' ')

        _split[0] = _split[0].replace('#', '')
        _split[2] = _split[2].replace(':', '')

        output.append(
            {
                "id": _split[0],
                "left_start": int(_split[2].split(',')[0]),
                'top_start': int(_split[2].split(',')[1]),
                'width': int(_split[3].split('x')[0]),
                'height': int(_split[3].split('x')[1])
            }
        )

    return output


def find_overlap(data, total_n=1000):

    total_array = np.zeros([total_n, total_n])
    overlap_total = 0

    for claim in data:

        total_array[
            claim['top_start']: (claim['top_start'] + claim['height']),
            claim['left_start']: (claim['left_start'] + claim['width'])
        ] += 1.

        sub_claim = total_array[
            claim['top_start']: (claim['top_start'] + claim['height']),
            claim['left_start']: (claim['left_start'] + claim['width'])
        ]

        overlap_total += sub_claim[sub_claim == 2].sum() / 2

    return overlap_total, total_array


def find_no_overlap(parsed_data, total_data):

    for claim in parsed_data:

        if (total_data[
            claim['top_start']: (claim['top_start'] + claim['height']),
            claim['left_start']: (claim['left_start'] + claim['width'])
        ] == 1).all():
            return claim['id']
