transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79114.93",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {
            "amount": "43318.34",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {
            "amount": "56883.54",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {
            "amount": "67314.70",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]


def filter_by_currency(data, currency_code):
    """Функция принимает список словарей и фильтрует их по валюте"""
    return (
        t
        for t in data
        if t.get("operationAmount", {}).get("currency", {}).get("code", "").upper()
        == currency_code.upper()
    )


def transaction_descriptions(data):
    """Функция принимаетсписок словарей и по очередивозвращает описание каждой операции, либо выдает пустую строку"""
    for d in data:
        yield d.get("description", "")


def card_number_generator(start, end):
    for num in range(start, end + 1):
        num_str = str(num)
        if len(num_str) != 16:
            raise ValueError("Номер карты должен состоять из 16 цифр")
        number_of_zero = 16 - len(num_str)

        card_str = ("0" * number_of_zero) + num_str
        yield f"{card_str[0:4]} {card_str[4:8]} {card_str[8:12]} {card_str[12:16]}"
