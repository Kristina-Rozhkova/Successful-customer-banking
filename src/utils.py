import json

json_path = r"..\data\operations.json"


def get_financial_transactions(json_path: str) -> dict | list:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(json_path, 'r', encoding='utf-8') as file:
            json_file = json.load(file)
            # если файл содержит список данных
            if isinstance(json_file, list):
                return json_file
            else:
                raise ValueError
    except FileNotFoundError:
        return []
    except ValueError:
        return []
    except Exception:
        return []


print(get_financial_transactions(json_path))
