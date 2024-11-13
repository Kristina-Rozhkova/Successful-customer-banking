def filter_by_state(lists_of_dict_1: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Функция принимает список словарей и опционально значение для ключа state, возвращает новый список словарей,
    содержащий только те словари, у которых ключ state соответствует указанному значению
    """

    new_list = []
    for dictionaries in lists_of_dict_1:
        for value in dictionaries.values():
            if value == state:
                new_list.append(dictionaries)
    return new_list


def sort_by_date(lists_of_dict_2: list[dict], order: bool = True) -> list[dict]:
    """
    Функция возвращает список, отсортированный по дате
    """
    sorted_list = sorted(lists_of_dict_2, key=lambda date: date["date"], reverse=order)
    return sorted_list
