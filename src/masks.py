import logging
import os
from typing import Union

# Получаем абсолютный путь до текущей директории
current_dir = os.path.dirname(os.path.abspath(__file__))

# Создаем путь до файла логов относительно текущей директории
rel_file_path = os.path.join(current_dir, "../logs/masks.log")
abs_file_path = os.path.abspath(rel_file_path)


logger = logging.getLogger("masks")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(abs_file_path, mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: Union[int | str]) -> str:
    """Функция маркировки номера банковской карты"""
    str_card_number = str(card_number)

    if len(str_card_number) == 16 and str_card_number.isdigit():
        logger.info(f"Длина строки '{str_card_number}' равна 16 и все символы - числа")
        transformed_card_number = (
            str_card_number[:4] + " " + str_card_number[4:6] + "**" + " " + "****" + " " + str_card_number[12:]
        )
        logger.info(f"Трансформация номера банковской карты {transformed_card_number}")
        return transformed_card_number
    logger.error(f"Введены некорректные данные номера карты {str_card_number}")
    return "Введены некорректные данные номера карты "


def get_mask_account(account_number: Union[int | str]) -> str:
    """Функция маркировки номера банковского счета"""
    str_account_number = str(account_number)

    if len(str_account_number) == 20 and str_account_number.isdigit():
        logger.info(f"Длина строки {str_account_number} равна 20 и все символы - числа")
        transformed_account_number = "**" + str_account_number[-4:]
        logger.info(f"Трансформация номера банковского счета {transformed_account_number}")
        return transformed_account_number
    logger.error(f"Введены некорректные данные номера банковского счета {str_account_number}")
    return "Введены некорректные данные номера банковского счета"


# card_number = int(input("Введите номер карты: "))
# account_number = int(input("Введите номер счета: "))
# print(get_mask_card_number(card_number))
# print(get_mask_account(account_number))
