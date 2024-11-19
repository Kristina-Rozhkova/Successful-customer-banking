from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(numb: str) -> str:
    """Функция, которая обрабатывает информацию о картах и о счетах"""
    name_of_card = ""
    number_card = ""
    if numb == "":
        raise ValueError("Не введены данные номера карты или счета")
    elif "Счет" in numb:
        number_card = numb[5:]
        if len(number_card) == 20:
            return "Счет " + get_mask_account(number_card)
        elif len(number_card) != 20:
            raise ValueError("Неверная длина номера счета")
    else:
        for letter in numb:
            if letter.isalpha() or letter == " ":
                name_of_card += letter
            if letter.isdigit():
                number_card += letter
        if len(number_card) == 16:
            return name_of_card + get_mask_card_number(number_card)
        elif len(number_card) != 16:
            raise ValueError("Неверная длина номера карты")


def get_date(date_from_user: str) -> str:
    """
    Функция, которая принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407"
    и возвращает строку с датой в формате "ДД.ММ.ГГГГ" ("11.03.2024")
    """
    if len(date_from_user) == 0:
        raise ValueError("Данные о дате отсутствуют")

    correct_date = date_from_user[8:10] + "." + date_from_user[5:7] + "." + date_from_user[:4]
    return correct_date


# numb = input()
# print(get_date(numb))
