import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number(card_number_example: str):
    """Тест проверяет корректность маскирования стандартного 16-значного номера карты."""
    assert get_mask_card_number(card_number_example) == "1234 43** **** 8765"


def test_get_mask_account(account_number_example: str):
    assert get_mask_account(account_number_example) == "**9876"


def test_get_mask_card_number_true_length(card_number_example: str):
    """Тест проверяет, что длина замаскированного номера всегда равна 19 символам (с пробелами)."""
    result = get_mask_card_number(card_number_example)
    assert len(result) == 19


def test_get_mask_card_number_wrong_length_raises_error():
    """Тест проверяет, что при неверной длине номера карты выбрасывается ValueError."""
    with pytest.raises(ValueError):
        get_mask_card_number("12345")


def test_get_mask_account_number_wrong_length_raises_error():
    with pytest.raises(ValueError):
        get_mask_account("12345")
