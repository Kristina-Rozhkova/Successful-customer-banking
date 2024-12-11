import json
from unittest.mock import mock_open, patch

from src.utils import get_financial_transactions


def test_get_financial_transactions_success():
    # успешное открытие файла и работу функции
    with patch('os.path.exists', return_value=True):
        with patch('builtins.open',
                   mock_open(read_data=json.dumps([{'amount': 500, 'currency': 'USD'}]))) as mock_open_file:
            result = get_financial_transactions('json_path')
            assert result == json.loads(json.dumps([{'amount': 500, 'currency': 'USD'}]))
            mock_open_file.assert_called_once_with('json_path', 'r', encoding='utf-8')


def test_get_financial_transactions_not_found():
    # результат функции при ненайденном пути
    with patch('os.path.exists', return_value=False):
        result = get_financial_transactions('json_path')
        assert result == json.loads(json.dumps([]))


def test_get_financial_transactions_clear():
    # результат функции, если файл пустой
    with patch('os.path.exists', return_value=True):
        with patch('builtins.open', mock_open(read_data=json.dumps([]))) as mock_open_file:
            result = get_financial_transactions('json_path')
            assert result == json.loads(json.dumps([]))
            mock_open_file.assert_called_once_with('json_path', 'r', encoding='utf-8')


def test_get_financial_transactions_not_list():
    # результат функции, если файл содержит не список
    with patch('os.path.exists', return_value=True):
        with patch('builtins.open',
                   mock_open(read_data=json.dumps({'amount': 500, 'currency': 'USD'}))) as mock_open_file:
            result = get_financial_transactions('json_path')
            assert result == json.loads(json.dumps([]))
            mock_open_file.assert_called_once_with('json_path', 'r', encoding='utf-8')
