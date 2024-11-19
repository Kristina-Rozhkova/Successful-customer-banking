from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number(card_number):
    assert get_mask_card_number("7000792289606361") == card_number

    assert get_mask_card_number("") == "Введены некорректные данные номера карты"

    assert get_mask_card_number("985264") == "Введены некорректные данные номера карты"

    assert get_mask_card_number("70007w2289o06p61") == "Введены некорректные данные номера карты"


def test_get_mask_account(account_number):
    assert get_mask_account("73654108430135874305") == account_number

    assert get_mask_account("") == "Введены некорректные данные номера банковского счета"

    assert get_mask_account("7365410843") == "Введены некорректные данные номера банковского счета"

    assert get_mask_account("73654108p30135m74305") == "Введены некорректные данные номера банковского счета"
