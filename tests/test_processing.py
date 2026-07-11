
from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_default(input_data):
    """Проверка фильтрации со статусом по умолчанию (EXECUTED)."""
    result = filter_by_state(input_data)
    assert len(result) == 4
    assert result[0]["id"] == 414288290
    assert result[1]["id"] == 939719570
    assert result[2]["id"] == 414288292
    assert result[3]["id"] == 939719572

def test_filter_by_state_canceled(input_data):
    """Проверка фильтрации со статусом CANCELED."""
    result = filter_by_state(input_data, "CANCELED")
    assert len(result) == 2
    assert result[0]["id"] == 594226727
    assert result[1]["id"] == 615064591

def test_filter_by_state_empty_input():
    """Проверка работы фильтра с пустым входящим списком"""
    assert filter_by_state([], "EXECUTED") == []

def test_sort_by_date_descending(input_data):
    """Проверка сортировки по дате по убыванию (descending=True)."""

    current_list_first = []

    result_first = sort_by_date(input_data)

    for item in result_first:

        current_list_first.append(item["id"])

    assert current_list_first == [414288292, 414288290, 615064591, 594226727, 939719572, 939719570]


def test_sort_by_date_ascending(input_data):
    """Проверка сортировки по дате по возрастанию (descending=False)."""
    current_list_second = []

    result_second = sort_by_date(input_data, descending=False)

    for item in result_second:

        current_list_second.append(item["id"])


    assert current_list_second  == [939719570, 939719572, 594226727, 615064591, 414288290, 414288292]

