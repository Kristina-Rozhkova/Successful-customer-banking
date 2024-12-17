import json
import logging
import os


# Получаем абсолютный путь до текущей директории
current_dir = os.path.dirname(os.path.abspath(__file__))

# Создаем путь до файла логов относительно текущей директории
rel_file_path = os.path.join(current_dir, "../logs/masks.log")
abs_file_path = os.path.abspath(rel_file_path)


logger = logging.getLogger("utils")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(abs_file_path, mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


json_path = r"..\data\operations2.json"


def get_financial_transactions(json_path: str) -> dict | list:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(json_path, "r", encoding="utf-8") as file:
            json_file = json.load(file)
            logger.info(f"Чтение файла {json_path} и преобразование его в Python-объект")
            # если файл содержит список данных
            if isinstance(json_file, list):
                logger.info(f"Файл {json_path} содержит список данных, вывод данных в консоль")
                return json_file
            else:
                logger.error(f"Файл {json_path} содержит не список данных")
                raise ValueError
    except FileNotFoundError as ex:
        logger.error(f"Возникла ошибка: {ex}, возврат пустого списка")
        return []
    except ValueError:
        logger.error("Возникла ошибка ValueError, возврат пустого списка")
        return []
    except Exception as ex:
        logger.error(f"Возникла ошибка: {ex}, возврат пустого списка")
        return []


print(get_financial_transactions(json_path))
