from unittest.mock import MagicMock, patch

from src.file_readers import read_transactions_csv


@patch("src.file_readers.pd.read_csv")
def test_csv_reading(mock_read_csv):
    """Тестируем функцию с установленными значениями"""
    mock_df = MagicMock()

    mock_df.to_dict.return_value = [{"id": 777, "status": "OK"}]

    mock_read_csv.return_value = mock_df

    result = read_transactions_csv("data/transactions.csv")

    assert result == [{"id": 777, "status": "OK"}]


@patch("src.file_readers.pd.read_csv")
def test_csv_file_not_found(mock_read_csv):
    """Файл CSV не существует"""

    mock_read_csv.side_effect = FileNotFoundError
    result = read_transactions_csv("no/no/no_file.csv")

    assert result == []
