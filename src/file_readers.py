import os
import pandas as pd


def read_transactions_csv(file_path: str) -> list:
    """Считывает финансовые операции из CSV-файла и возвращает список словарей."""

    if not os.path.exists(file_path):
        return []

    try:
        df = pd.read_csv(file_path, delimiter=";")

        return df.to_dict(orient="records")

    except Exception:
        return []

#Проверка на работоспособность
# if __name__ == "__main__":
#
#     csv_path = os.path.join("..","data", "transactions.csv")
#     csv_data = read_transactions_csv(csv_path)
#     print(f"Количество транзакций: {len(csv_data)}")
#     if csv_data:
#         print(csv_data[0])
