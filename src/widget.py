from src.masks import get_mask_account, get_mask_card_number

def mask_account_card(numb: str) -> str:
    """ Функция, которая обрабатывает информацию о картах и о счетах """
    name_of_card = ''
    if 'Счет' in numb:
        return 'Счет ' + get_mask_account(numb)
    else:
        number_card = numb[-16:]
        for letter in numb:
            if letter.isalpha() or letter == ' ':
                name_of_card += letter
        return name_of_card + get_mask_card_number(number_card)


def get_date(date_from_user:str) -> str:
    """
    Функция, которая принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407"
    и возвращает строку с датой в формате "ДД.ММ.ГГГГ" ("11.03.2024")
    """
    correct_date = date_from_user[8:10] + '.' + date_from_user[5:7] + '.' + date_from_user[:4]
    return correct_date


#numb = input()
#print(get_date(numb))