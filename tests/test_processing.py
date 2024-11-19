from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_executed(list_of_dicts, test_filter_executed):
    assert filter_by_state(list_of_dicts, "EXECUTED") == test_filter_executed


def test_filter_by_state_canceled(list_of_dicts, test_filter_canceled):
    assert filter_by_state(list_of_dicts, "CANCELED") == test_filter_canceled


def test_sort_by_date(list_of_dicts, date_sort):
    assert sort_by_date(list_of_dicts) == date_sort
