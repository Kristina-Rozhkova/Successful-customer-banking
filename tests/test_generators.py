from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency_usd(transaction, usd_filtered):
    result_of_filter_by_currency_usd = filter_by_currency(transaction, "USD")
    assert list(result_of_filter_by_currency_usd) == usd_filtered


def test_filter_by_currency_rub(transaction, rub_filtered):
    assert list(filter_by_currency(transaction, "RUB")) == rub_filtered


def test_filter_by_currency_incorrect(transaction):
    result = filter_by_currency(transaction, "юани")
    assert next(result) == "Код валюты не найден. Пожалуйста, введите одну из имеющихся: USD или RUB"


def test_filter_by_currency_with_clear_transaction(clear_transaction):
    result_of_clear_transaction = filter_by_currency(clear_transaction, "USD")
    assert next(result_of_clear_transaction) == "Список транзакций пуст"


def test_filter_by_currency_with_currency_code():
    transactions = [
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "amount": "43318.34",
            "currency_code": "USD",
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "amount": "67314.70",
            "currency_code": "RUB",
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        },
    ]

    result = filter_by_currency(transactions, 'RUB')

    assert next(result) == {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "amount": "67314.70",
        "currency_code": "RUB",
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657"
    }


def test_transaction_descriptions(transaction, usd_filtered, rub_filtered):
    assert list(transaction_descriptions(transaction)) == [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]

    assert list(transaction_descriptions(usd_filtered)) == [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
    ]

    assert list(transaction_descriptions(rub_filtered)) == ["Перевод со счета на счет", "Перевод организации"]


def test_transaction_descriptions_with_clear_list(clear_transaction):
    result_of_transaction_descriptions = transaction_descriptions(clear_transaction)
    assert next(result_of_transaction_descriptions) == "Список транзакций пуст"


def test_card_number_generator(card_numbers_from_one_to_five):
    assert list(card_number_generator(1, 5)) == card_numbers_from_one_to_five
