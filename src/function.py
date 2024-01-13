import json

def open_file(file_name):
    """Функция открытия файла"""
    with open(file_name) as file:
        f = json.load(file)
    return f