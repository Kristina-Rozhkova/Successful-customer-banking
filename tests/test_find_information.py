from collections import Counter

from src.find_information import count_category_of_transactions, find_description


def test_find_description(transaction, find_str, transfer_of_organization):
    assert find_description(transaction, find_str) == transfer_of_organization


def test_find_description_clear_str(transaction):
    assert find_description(transaction, 'Отправка') == []


def test_find_description_clear_transaction(find_str):
    assert find_description([], find_str) == []


def test_count_category_of_transactions(transaction, category, count_category):
    assert count_category_of_transactions(transaction, category) == count_category


def test_count_category_of_transactions_clear(category):
    assert count_category_of_transactions([], category) == Counter()
