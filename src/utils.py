import json
import os

json_path = r"..\data\operations.json"


def get_financial_transactions(json_path: str) -> list:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    # если путь к файлу существует
    try:
        if os.path.exists(json_path):
            # если файл содержит данные
            if json_path:
                with open(json_path, 'r', encoding='utf-8') as file:
                    json_file = json.load(file)
                    # если файл содержит список данных
                    if isinstance(json_file, list):
                        return json_file
    except FileNotFoundError:
        return []
    except Exception:
        return []


print(get_financial_transactions(json_path))
