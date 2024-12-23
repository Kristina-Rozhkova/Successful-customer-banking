from src.find_information import find_description
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.reading_csv_and_excel import csv_reader, excel_reader
from src.utils import get_financial_transactions
from src.widget import get_date, mask_account_card


def say_hello() -> str:
    """Выбор пункта меню"""
    print('''
    Привет! Добро пожаловать в программу работы с банковскими транзакциями. 
    Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла
    ''')

    user_input = int(input())
    if user_input == 1:
        print('Для обработки выбран JSON-файл.')
        return 'Для обработки выбран JSON-файл.'
    elif user_input == 2:
        print('Для обработки выбран CSV-файл.')
        return 'Для обработки выбран CSV-файл.'
    elif user_input == 3:
        print('Для обработки выбран XLSX-файл.')
        return 'Для обработки выбран XLSX-файл.'
    else:
        raise ValueError("Введены некорректные данные. Попробуйте снова")



def choice_state(point: str) -> list:
    """Выбор статуса для фильтрации"""
    while True:
        print('''
        Введите статус, по которому необходимо выполнить фильтрацию. 
        Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
        ''')
        user_input = input().upper()

        if user_input not in ['EXECUTED', 'CANCELED', 'PENDING']:
            print(f'Статус операции {user_input} недоступен.')
        else:
            print(f'Операции отфильтрованы по статусу {user_input}')
            if 'JSON' in point:
                list_for_user = get_financial_transactions('data/operations.json')
                filtered = filter_by_state(list_for_user, user_input)
                return filtered
            elif 'CSV' in point:
                list_for_user = csv_reader('data/transactions.csv')
                filtered = filter_by_state(list_for_user, user_input)
                return filtered
            elif 'XLSX' in point:
                list_for_user = excel_reader('data/transactions_excel.xlsx')
                filtered = filter_by_state(list_for_user, user_input)
                return filtered


def date_choice(list_for_sort: list) -> list:
    """Вывод отфильтрованных списков по дате по возрастанию/убыванию"""
    if not list_for_sort:
        return []

    answers_date = []
    print('Отсортировать операции по дате? Да/Нет')
    date_filter = input().lower()
    answers_date.append(date_filter)

    if date_filter == 'да':
        print('Отсортировать по возрастанию или по убыванию?')
        user_order = input().lower()
        answers_date.append(user_order)

    if answers_date[0] == 'да' and 'по возрастанию' in answers_date:
        date_sorted = sort_by_date(list_for_sort, False)
        return date_sorted

    elif answers_date[0] == 'да' and 'по убыванию' in answers_date:
        date_sorted = sort_by_date(list_for_sort)
        return date_sorted

    else:
        return list_for_sort


def code_choice(list_for_sort: list) -> list:
    """Вывод отфильтрованных списков по коду транзакций"""
    if not list_for_sort:
        return []

    print('Выводить только рублевые тразакции? Да/Нет')

    user_code = input().lower()
    if user_code == 'да':
        code_sorted = filter_by_currency(list_for_sort, 'RUB')
        list_code_sorted = list(code_sorted)
        return list_code_sorted
    else:
        return list_for_sort


def description_choice(list_for_sort: list) -> list:
    """Вывод отфильтрованных списков по заданному слову описания"""
    if not list_for_sort:
        return []

    print('Отфильтровать список транзакций по определенному слову в описании? Да/Нет')

    user_description = input().lower()
    if user_description == 'да':
        print('Введите слово для поиска')
        user_word = input()

        sorted_description = find_description(list_for_sort, user_word)
        return sorted_description
    else:
        return list_for_sort


def main(list_for_answer: list) -> str:
    """Вывод ответа на основе отфильтрованного списка"""
    if not list_for_answer:
        return 'Не найдено ни одной транзакции, подходящей под ваши условия фильтрации'

    print('Распечатываю итоговый список транзакций...')

    print(f'Всего банковских операций в выборке: {len(list_for_answer)}')

    for dicts in list_for_answer:
        date = get_date(dicts['date'])
        print(date, dicts['description'])

        to_account_number = mask_account_card(dicts['to'])
        if 'from' in dicts:
            str_dict = str(dicts['from'])
            if str_dict != 'nan':
                from_account_number = mask_account_card(str(dicts['from']))
                print(f'{to_account_number} -> {from_account_number}')
            else:
                print(to_account_number)
        else:
            print(to_account_number)

        if 'operationAmount' in dicts:
            amount = float(dicts['operationAmount']['amount'])
            name = dicts['operationAmount']['currency']['name']
        else:
            amount = dicts['amount']
            name = dicts['currency_name']
        print(f'Сумма: {int(amount)} {name}')

        print(' ')
    return ''


if __name__ == '__main__':
    print(main(description_choice(code_choice(date_choice(choice_state(say_hello()))))))

