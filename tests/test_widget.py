import pytest

from src.widget import get_date, mask_account_card


def test_mask_account_card_empty_string_raises_error():
    """Тест проверяет, что при пустой строке выдает ValueError"""
    with pytest.raises(ValueError):
        mask_account_card("")


def test_mask_account_card_wrong_length_raises_error():
    """Тест проверяет, что при неверной длине номера карты выбрасывается ValueError."""
    with pytest.raises(ValueError):
        mask_account_card("12345")


@pytest.mark.parametrize(
    "account_card,expected_mask",
    [
        # Тесты для 20-ти значных счетов
        ("12345543216789009876", "**9876"),
        ("12344321567887654321", "**4321"),
        # Тесты для 16-ти значных счетов
        ("1234432156788765", "1234 43** **** 8765"),
        ("1111222233334444", "1111 22** **** 4444"),
    ],
)
def test_mask_account_card(account_card, expected_mask):
    assert mask_account_card(account_card) == expected_mask


@pytest.mark.parametrize(
    "date_string,expected_date",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2026-12-31T02:44:53.757999", "31.12.2026"),
        # Нестандартные строки (только дата без времени, или дата с пробелом вместо T)
        ("2024-05-20", "20.05.2024"),
        ("2025-08-15 14:30:00", "15.08.2025"),
    ],
)
def test_get_date(date_string, expected_date):
    assert get_date(date_string) == expected_date


@pytest.mark.parametrize(
    "invalid_date_string",
    [
        "",  # Проверка: пустая строка (дата отсутствует)
        "   ",  # Проверка: строка из пробелов (дата отсутствует)
        "202-03-11T02:26:18",  # Проверка: сломанный год (неверная длина)
        "2024-ММ-ДДT00:00:00",  # Проверка: буквы вместо цифр в дате
    ],
)
def test_get_date_invalid_formats_raises_error(invalid_date_string):
    """Проверка, что функция корректно обрабатывает отсутствие даты и неверные форматы."""
    with pytest.raises(ValueError):
        get_date(invalid_date_string)
