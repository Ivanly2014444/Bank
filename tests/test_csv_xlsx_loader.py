from unittest.mock import MagicMock, patch

from src.csv_xlsx_loader import read_transactions_xlsx


@patch("src.csv_xlsx_loader.pd.read_excel")
def test_xlsx_reading(mock_read_excel):
    """Тестируем функцию с установленными значениями"""
    mock_df = MagicMock()

    mock_df.to_dict.return_value = [{"id": 325, "status": "OK"}]

    mock_read_excel.return_value = mock_df

    result = read_transactions_xlsx("data/transactions_excel.xlsx")

    assert result == [{"id": 325, "status": "OK"}]


@patch("src.file_readers.pd.read_excel")
def test_xlsx_file_not_found(mock_read_excel):
    """Файл xlsx не существует"""

    mock_read_excel.side_effect = FileNotFoundError
    result = read_transactions_xlsx("no/no/no_file.xlsx")

    assert result == []
