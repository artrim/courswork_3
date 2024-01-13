from config import OPERATIONS
from function import *


file = open_file(OPERATIONS) # Все операции
filter_list = filter_list(file)
sorted_date = sorted_by_date(filter_list)
modify_date(sorted_date)
modify_bill(sorted_date)
first_five_operation = sorted_date[:5]


for i in first_five_operation:
    print(f"{i['date']} {i['description']}")
    if i['description'] == 'Открытие вклада':
        print(f"{i['to']}")
    else:
        print(f"{i['from']} -> {i['to']}")
    print(f"{i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}\n")