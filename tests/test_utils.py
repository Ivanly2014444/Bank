import json

from src.utils import get_financial_data


def test_get_financial_data_success(tmp_path):
    """Файл существует и содержит корректный список словарей"""
    test_file = tmp_path / "operations.json"

    test_data = [{"id": 1, "state": "EXECUTED"}, {"id": 2, "state": "CANCELED"}]
    test_file.write_text(json.dumps(test_data), encoding="utf-8")

    result = get_financial_data(str(test_file))
    assert result == test_data


def test_get_financial_data_file_not_found():
    """Файл не найден — функция должна вернуть пустой список"""
    result = get_financial_data("non_existent_file.json")
    assert result == []


def test_get_financial_data_empty_file(tmp_path):
    """Файл пустой (вызывает ошибку JSONDecodeError)"""
    test_file = tmp_path / "empty.json"

    test_file.write_text("", encoding="utf-8")

    result = get_financial_data(str(test_file))
    assert result == []
