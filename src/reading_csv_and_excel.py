import pandas as pd


def csv_reader(csv_path: str) -> list:
    """Вывод данных из CSV-файла"""

    try:
        csv_reading = pd.read_csv(csv_path, sep=';')
        return csv_reading.to_dict(orient='records')

    except FileNotFoundError:
        return []

    except Exception:
        return []


# print(csv_reader('../data/transactions.csv'))


def excel_reader(excel_path: str) -> list:
    """Вывод данных из excel-файла"""

    try:
        excel_reading = pd.read_excel(excel_path, engine='openpyxl')
        return excel_reading.to_dict(orient='records')

    except FileNotFoundError:
        return []

    except Exception:
        return []


# print(excel_reader('../data/transactions_excel.xlsx'))
