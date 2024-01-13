import json
from datetime import datetime

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


def sorted_by_date(data):
    """Сотрирует по дате"""
    sorted_list = sorted(data, key=lambda x: x['date'], reverse=True)
    return sorted_list


def modify_date(data):
    """Форматирует дату"""
    for i in data:
        format_date = datetime.fromisoformat(i['date'])
        i['date'] = f'{format_date.day}.{format_date.month}.{format_date.year}'
    return data


def modify_bill(bill):
    """Форматирует реквизиты отправителя и получателя"""
    for i in bill:
        i['to'] = f"Счет **{i['to'][-4:]}"
        if not i.get('from'):
            continue
        if "Счет" in i['from']:
            i['from'] = f"Счет **{i['from'][-4:]}"
        else:
            i['from'] = f"{i['from'][:-17]} {i['from'][-16:-12]} {i['from'][-12:-10]}** **** {i['from'][-4:]}"
    return bill



