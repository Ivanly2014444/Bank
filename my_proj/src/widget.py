import re

from masks import get_mask_account, get_mask_card_number

def mask_account_card(account_card: str) -> str:

    number_match = re.search(r'\d+', account_card)
    number = number_match.group() if number_match else ""

    name_match = re.search(r'\D+', account_card)
    name_card = name_match.group().strip() if name_match else ""

    """Функция принимает номер счета или карты, маскируя их"""

    if len(number) == 20:  # Если это номер счета
        masked_number = get_mask_account(number)

    elif len(number) == 16:  # Если это номер карты
        masked_number = get_mask_card_number(number)
    else:
        # На случай, если ввели неверное количество цифр
        masked_number = "Неверное количество цифр"
    return f"{name_card} {masked_number}".strip()


user_card = input("Введите название номер карты через пробел: ")
print(mask_account_card(user_card))


def get_date(date_string: str) -> str:
    year = date_string[:4]
    month = date_string[5:7]
    day = date_string[8:10]
    return f"{day}.{month}.{year}"


user_input = input("Введите дату  (например: 2024-03-11T02:26:18.671407): ")
print("Результат:", get_date(user_input))

