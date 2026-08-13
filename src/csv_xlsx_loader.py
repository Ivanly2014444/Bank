import os

import pandas as pd


def read_transactions_xlsx(file_path: str) -> list:
    """Считывает финансовые операции из XLSX-файла и возвращает список словарей."""

    if not os.path.exists(file_path):
        return []

    try:
        df = pd.read_excel(file_path)
        return df.to_dict(orient="records")
    except Exception:
        return []


# if __name__ == "__main__":
#
#     xlsx_path = os.path.join("..","data", "transactions_excel.xlsx")
#     xlsx_data = read_transactions_xlsx(xlsx_path)
#     print(f"Количество транзакций: {len(xlsx_data)}")
#     if xlsx_data:
#         print(xlsx_data[0])
