import re
from collections import Counter


def find_description(list_of_dicts: list, find_str: str) -> list:
    """Поиск информации по описанию банковских операций"""
    list_of_description = []
    for some_dict in list_of_dicts:
        find_operation = re.search(find_str, some_dict['description'])
        if find_operation:
            list_of_description.append(some_dict)

    return list_of_description


def count_category_of_transactions(list_of_dicts: list, category_list: list) -> dict:
    """Подсчет встречающихся категорий операций из заданного списка"""
    list_transactions = []
    for some_dict in list_of_dicts:
        if some_dict['description'] in category_list:
            list_transactions.append(some_dict['description'])
    counted = Counter(list_transactions)
    return counted


# if __name__ == '__main__':
#     operations = [
#       {
#         "id": 782295999,
#         "state": "EXECUTED",
#         "date": "2019-09-11T17:30:34.445824",
#         "operationAmount": {
#           "amount": "54280.01",
#           "currency": {
#             "name": "евро",
#             "code": "EUR"
#           }
#         },
#         "description": "Перевод со счета на счет",
#         "from": "Счет 24763316288121894080",
#         "to": "Счет 96291777776753236930"
#       },
#       {
#         "id": 441945886,
#         "state": "EXECUTED",
#         "date": "2019-08-26T10:50:58.294041",
#         "operationAmount": {
#           "amount": "31957.58",
#           "currency": {
#             "name": "руб.",
#             "code": "RUB"
#           }
#         },
#         "description": "Перевод организации",
#         "from": "Maestro 1596837868705199",
#         "to": "Счет 64686473678894779589"
#       },
#       {
#         "id": 41428829,
#         "state": "EXECUTED",
#         "date": "2019-07-03T18:35:29.512364",
#         "operationAmount": {
#           "amount": "8221.37",
#           "currency": {
#             "name": "USD",
#             "code": "USD"
#           }
#         },
#         "description": "Перевод организации",
#         "from": "MasterCard 7158300734726758",
#         "to": "Счет 35383033474447895560"
#       },
#       {
#         "id": 939719570,
#         "state": "EXECUTED",
#         "date": "2018-06-30T02:08:58.425572",
#         "operationAmount": {
#           "amount": "9824.07",
#           "currency": {
#             "name": "USD",
#             "code": "USD"
#           }
#         },
#         "description": "Перевод организации",
#         "from": "Счет 75106830613657916952",
#         "to": "Счет 11776614605963066702"
#       }
#     ]
#     print(find_description(operations, "ПеревоL"))
#
#     list_of_category = ["Перевод организации", "Перевод со счета на счет", "Открытие вклада",
#                         "Перевод с карты на карту", "Перевод с карты на счет", "Перевод со счета на карту", ]
#
#     print(count_category_of_transactions(operations, list_of_category))
