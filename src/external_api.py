import os

import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")


def convert_transaction_amount(transaction):
    """
    Принимает словарь транзакции и возвращает сумму в рублях (RUB).
    Если валюта отличная от RUB, запрашивает актуальный курс через APILayer.

    """
    if "operationAmount" not in transaction:
        return 0.0
    amount = float(transaction["operationAmount"]["amount"])
    currency_code = transaction["operationAmount"]["currency"]["code"]

    if currency_code == "RUB":
        return amount

    url = "https://marketplace.apilayer.com/exchangerates_data-api"
    headers = {"apikey": api_key}
    params = {"to": "RUB", "from": currency_code, "amount": amount}

    try:
        response = requests.get(url, headers=headers, params=params)

        if response.status_code != 200:
            return 0.0

        response_data = response.json()
        return float(response_data["result"])
    except Exception:
        print("Ошибка при конвертации валюты через API")
        return 0.0
