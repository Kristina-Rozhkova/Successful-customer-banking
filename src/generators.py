from typing import Dict, Generator, Iterator, List, Union

transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]


def filter_by_currency(
    some_transactions: List[Dict], currency_code: str = "USD"
) -> Union[Iterator[Dict], str]:
    """Функция принимает на вход список словарей, представляющих транзакции"""

    if some_transactions == []:
        return "Список транзакций пуст"
    if currency_code not in ["USD", "RUB"]:
        return "Код валюты не найден. Пожалуйста, введите одну из имеющихся: USD или RUB"

    for transaction in some_transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency_code:
            yield transaction

    return iter([])

# для проверки работы функции
# currency_code = str(input())
# usd_transactions = filter_by_currency(transactions, currency_code)
# for _ in range(3):
#     print(next(usd_transactions))


def transaction_descriptions(transaction: List[Dict]) -> Union[Generator[Dict, None, None], str]:
    """
    Функция-генератор, который принимает список словарей с транзакциями
    и возвращает описание каждой операции по очереди
    """

    if transaction == []:
        return "Список транзакций пуст"
    for description in transaction:
        yield description["description"]
    # возвращаем пустой генератор для удовлетворения mypy в случае когда возвращается строка,
    # чтобы не возникала ошибка "error: Missing return statement"
    return iter([])


# для проверки работы функции
# descriptions = transaction_descriptions(transactions)
# for _ in range(5):
#     print(next(descriptions))


def card_number_generator(start: int, end: int) -> Union[Generator[Dict, None, None], str]:
    """
    Функция-генератор, который выдает номера банковских карт
    в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты.
    """

    for number in range(start, end + 1):
        card_number = f"{number:016}"
        formatted_card_number = " ".join(card_number[i: i + 4] for i in range(0, len(card_number), 4))
        yield formatted_card_number
    # возвращаем пустой генератор для удовлетворения mypy в случае когда возвращается строка,
    # чтобы не возникала ошибка "error: Missing return statement"
    return iter([])


# для проверки работы функции
# for card_number in card_number_generator(1, 5):
#    print(card_number)
