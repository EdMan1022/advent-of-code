def load_int_data(filepath):
    data = load_data(filepath)
    return [float(_) for _ in data]


def load_data(filepath):
    with open(filepath, 'r') as file:
        data = file.readlines()
    return data
