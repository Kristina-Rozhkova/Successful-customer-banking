from unittest.mock import patch

import pytest

from src.external_api import get_transaction_amount


@patch('requests.request')
def test_get_transaction_amount_usd(mock_request):
    transactions_for_external_api = [{
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {
            "amount": "8221.37",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560"
    }]

    mock_request.return_value.json.return_value = {'success': True,
                                                   'query': {'from': 'USD', 'to': 'RUB', 'amount': 8221.37},
                                                   'info': {'timestamp': 1733913543, 'rate': 103.500991},
                                                   'date': '2024-12-11', 'result': 850919.942378}
    assert get_transaction_amount(transactions_for_external_api) == 850919.942378


def test_get_transaction_amount_rub():
    transactions_for_external_api = [{
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {
            "amount": "8221.37",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560"
    }]
    assert get_transaction_amount(transactions_for_external_api) == 8221.37


def test_get_transaction_amount_with_error():
    transactions_for_external_api = [{
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {
            "amount": "8221.37",
            "currency": {
                "name": "CAD",
                "code": "CAD"
            }
        },
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560"
    }]
    with pytest.raises(ValueError) as ex_info:
        get_transaction_amount(transactions_for_external_api)

    assert str(ex_info.value) == "The currency didn't convert. Use one of this currency: RUB/USD/EUR."
