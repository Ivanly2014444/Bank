import pytest

from generator import (
    card_number_generator,
    filter_by_currency,
    transaction_descriptions,
)


def test_filter_by_currency(test_transactions):
    """Проверяет фильтрацию транзакций по валюте USD в верхнем регистре."""
    result = filter_by_currency(test_transactions, "USD")

    # Проверяем, что в списке ровно 3 транзакции (для USD)
    assert len(result) == 3
    # Проверяем, что id соответсвует действительному
    assert result[0]["id"] == 939719570
    assert result[1]["id"] == 142264268
    assert result[2]["id"] == 895315941


def test_filter_by_currency_lowercase(test_transactions):
    """Проверяет регистронезависимость фильтра при передаче валюты в нижнем регистре."""
    result = filter_by_currency(test_transactions, "usd")
    assert len(result) == 3


def test_filter_by_currency_empty(test_transactions):
    """Проверяет, что функция возвращает пустой список при отсутствии совпадений по валюте."""
    result = filter_by_currency(test_transactions, "RRR")
    assert result == []


@pytest.mark.parametrize(
    "incoming_data, expected_descriptions",
    [
        (
            [
                {
                    "id": 594226727,
                    "description": "Перевод организации",
                },  # 1. Проверка по id
                {"id": 142264268, "description": "Перевод со счета на счет"},
            ],
            ["Перевод организации", "Перевод со счета на счет"],
        ),
        ([], []),  # 2. Проверка на пустой список
    ],
)
def test_transaction_descriptions(incoming_data, expected_descriptions):
    """Проверяет извлечение текстовых описаний из переданного списка транзакций."""
    result = list(transaction_descriptions(incoming_data))
    assert result == expected_descriptions


@pytest.mark.parametrize(
    "start, end, expected",
    [
        (
            1111222233334444,
            1111222233334446,
            ["1111 2222 3333 4444", "1111 2222 3333 4445", "1111 2222 3333 4446"],
        ),
        (9999999999999999, 9999999999999999, ["9999 9999 9999 9999"]),
    ],
)
def test_card_generator_success(start, end, expected):
    """Проверяет корректность генерации и форматирования номеров карт в заданном диапазоне."""
    assert list(card_number_generator(start, end)) == expected


def test_card_generator_value_error():
    """Проверяет выброс исключения ValueError, если переданный номер карты превышает 16 знаков."""
    with pytest.raises(ValueError):
        list(card_number_generator(10000000000000000, 10000000000000001))
