from typing import Dict, List


def filter_by_state(list_of_dicts: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """
    Функция принимает список словарей и опционально значение для ключа state, возвращает новый список словарей,
    содержащий только те словари, у которых ключ state соответствует указанному значению
    """

    new_list = []
    for dictionaries in list_of_dicts:
        if state == dictionaries["state"]:
            new_list.append(dictionaries)
    return new_list


def sort_by_date(list_of_dicts: List[Dict], order: bool = True) -> List[Dict]:
    """
    Функция возвращает список, отсортированный по дате
    """
    sorted_list = sorted(list_of_dicts, key=lambda date: date["date"], reverse=order)
    return sorted_list
