import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "numb, expected",
    [
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
    ],
)
def test_mask_account_card(numb, expected):
    assert mask_account_card(numb) == expected


def test_mask_account_card_length_of_card(length_card):
    with pytest.raises(ValueError) as exc_info:
        mask_account_card(length_card)

    assert str(exc_info.value) == "Неверная длина номера карты"


def test_mask_account_card_length_of_account(length_account):
    with pytest.raises(ValueError) as exc_info:
        mask_account_card(length_account)

    assert str(exc_info.value) == "Неверная длина номера счета"


def test_mask_account_card_without_data(without_data_for_mask):
    with pytest.raises(ValueError) as exc_info:
        mask_account_card(without_data_for_mask)

    assert str(exc_info.value) == "Не введены данные номера карты или счета"


@pytest.mark.parametrize(
    "datas, expected_data",
    [("2024-03-11T02:26:18.671407", "11.03.2024"), ("2024-09-20T09:40:30.399677", "20.09.2024")],
)
def test_get_date(datas, expected_data):
    assert get_date(datas) == expected_data


def test_get_date_missing_data(get_date_invalid):
    with pytest.raises(ValueError) as exc_info:
        get_date(get_date_invalid)

        assert str(exc_info.value) == "Данные о дате отсутствуют"
