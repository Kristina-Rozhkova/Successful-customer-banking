from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_executed(list_of_dicts, test_filter_executed):
    assert filter_by_state(list_of_dicts, "EXECUTED") == test_filter_executed


def test_filter_by_state_canceled(list_of_dicts, test_filter_canceled):
    assert filter_by_state(list_of_dicts, "CANCELED") == test_filter_canceled


def test_sort_by_date(list_of_dicts, date_sort):
    assert sort_by_date(list_of_dicts) == date_sort


def test_filter_by_date_continue():
    list_of_dicts = [
        {
            "id": 939719570,
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 594226727,
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        }
    ]

    assert filter_by_state(list_of_dicts) == []
