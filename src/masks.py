from typing import Union


def get_mask_card_number(card_number: Union[int | str]) -> str:
    """Функция маркировки номера банковской карты"""
    str_card_number = str(card_number)

    if len(str_card_number) == 16 and str_card_number.isdigit():
        transformed_card_number = (
            str_card_number[:4] + " " + str_card_number[4:6] + "**" + " " + "****" + " " + str_card_number[12:]
        )
        return transformed_card_number
    return "Введены некорректные данные номера карты"


def get_mask_account(account_number: Union[int | str]) -> str:
    """Функция маркировки номера банковского счета"""
    str_account_number = str(account_number)

    if len(str_account_number) == 20 and str_account_number.isdigit():
        transformed_account_number = "**" + str_account_number[-4:]
        return transformed_account_number

    return "Введены некорректные данные номера банковского счета"


# card_number = int(input("Введите номер карты: "))
# account_number = int(input("Введите номер счета: "))
# print(get_mask_card_number(card_number))
# print(get_mask_account(account_number))
