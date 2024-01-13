import json

def open_file(file_name):
    """Функция открытия файла"""
    with open(file_name) as file:
        f = json.load(file)
    return f


def filter_list(data):
    """Фильтрует список"""

    new_data = []
    for item in data:
        if item == {}:
            continue
        elif item['state'] == 'EXECUTED':
            new_data.append(item)
    return new_data




