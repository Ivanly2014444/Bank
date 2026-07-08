import pytest


@pytest.fixture
def card_number_example() -> str:
    """Фикстура, возвращающая тестовый номер карты."""
    return "1234432156788765"


@pytest.fixture
def account_number_example() -> str:
    """Фикстура, возвращающая тестовый номер счета."""
    return "12345543216789009876"
