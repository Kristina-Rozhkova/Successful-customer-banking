from unittest.mock import patch

import pandas as pd

from src.reading_csv_and_excel import csv_reader, excel_reader


def test_csv_reader_success():
    mock_data = pd.DataFrame({
        'id': [650703, 3598919],
        'state': ['EXECUTED', 'EXECUTED'],
        'amount': [16210, 29740],
        'currency_name': ['Sol', 'Peso'],
        'currency_code': ['PEN', 'COP']
    })

    with patch('pandas.read_csv', return_value=mock_data) as mock_read_csv:
        result = csv_reader('test.csv')
        assert result == mock_data.to_dict(orient='records')
        mock_read_csv.assert_called_once_with('test.csv')


def test_csv_reader_not_found_error():
    # результат функции при ненайденном пути
    with patch('os.path.exists', return_value=False) as mock_read_csv:
        result = csv_reader('test.csv')
        assert result == []
        mock_read_csv.assert_not_called()


def test_csv_reader_exception():
    # результат функции при пустом файле
    with patch('pandas.read_csv', return_value='') as mock_read_csv:
        result = csv_reader('test.csv')
        assert result == []
        mock_read_csv.assert_called_once_with('test.csv')


def test_excel_reader_success():
    mock_data = pd.DataFrame({
        'id': [650703, 3598919],
        'state': ['EXECUTED', 'EXECUTED'],
        'amount': [16210, 29740],
        'currency_name': ['Sol', 'Peso'],
        'currency_code': ['PEN', 'COP']
    })

    with patch('pandas.read_excel', return_value=mock_data) as mock_read_excel:
        result = excel_reader('test.excel')
        assert result == mock_data.to_dict(orient='records')
        mock_read_excel.assert_called_once_with('test.excel')


def test_excel_reader_not_found_error():
    with patch('os.path.exists', return_value=False) as mock_read_excel:
        result = excel_reader('test.excel')
        assert result == []
        mock_read_excel.assert_not_called()


def test_excel_reader_exseption():
    with patch('pandas.read_excel', return_value='') as mock_read_excel:
        result = excel_reader('test.excel')
        assert result == []
        mock_read_excel.assert_called_once_with('test.excel')
