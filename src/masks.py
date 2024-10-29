from typing import Union


def get_mask_card_number(card_number: Union[int]) -> str:
    """Функция маркировки номера банковской карты"""
    str_card_number = str(card_number)
    transformed_card_number = (
        str_card_number[:4] + " " + str_card_number[4:6] + "**" + " " + "****" + " " + str_card_number[12:]
    )
    return transformed_card_number


def get_mask_account(account_number: Union[int]) -> str:
    """Функция маркировки номера банковского счета"""
    str_account_number = str(account_number)
    transformed_account_number = "**" + str_account_number[-4:]
    return transformed_account_number


#card_number = int(input("Введите номер карты: "))
#account_number = int(input("Введите номер счета: "))
#print(get_mask_card_number(card_number))
#print(get_mask_account(account_number))
