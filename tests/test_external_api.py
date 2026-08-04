from unittest.mock import patch

import pytest

from src.external_api import convert_transaction_amount


@pytest.fixture
def rub_transaction():
    return {"operationAmount": {"amount": "150.50", "currency": {"code": "RUB"}}}


@pytest.fixture
def usd_transaction():
    return {"operationAmount": {"amount": "50.00", "currency": {"code": "USD"}}}


def test_convert_amount_rub(rub_transaction):
    """Для рублей API вообще не вызывается, возвращается исходное число"""

    result = convert_transaction_amount(rub_transaction)

    assert result == 150.50


@patch("src.external_api.requests.get")
def test_convert_amount_usd_success(mock_get, usd_transaction):
    """Успешный запрос курса доллара через API"""

    mock_response = mock_get.return_value
    mock_response.status_code = 200
    mock_response.json.return_value = {"result": 3750.0}

    result = convert_transaction_amount(usd_transaction)

    assert result == 3750.0

    mock_get.assert_called_once()


@patch("src.external_api.requests.get")
def test_convert_amount_api_error(mock_get, usd_transaction):
    """Сервер API вернул ошибку (например, статус-код 500)"""

    mock_response = mock_get.return_value
    mock_response.status_code = 500

    result = convert_transaction_amount(usd_transaction)

    assert result == 0.0
