import re

def mask_account_card(account_card: str) -> str:
    number = re.search(r'\d+', account_card).group()
    name_card = re.search(r'\D+',account_card).group().strip()

    """Функция принимает номер счета или карты, маскируя их"""

    if len(number) == 20:# Если это номер счета
        masked_number = "**" + number[-4:]

    elif len(number) == 16:# Если это номер карты
        part_1 = number[:4]
        part_2 = number[4:6] + "**"
        part_3 = "****"
        part_4 = number[-4:]
        masked_number = f'{part_1} {part_2} {part_3} {part_4}'
    else:
        # На случай, если ввели неверное количество цифр
        masked_number = "Неверное количество цифр"
    return f"{name_card} {masked_number}"

user_card = input("Введите название номер карты через пробел: ")
print(mask_account_card(user_card))

def get_date(date_string: str) -> str:
    year = date_string [:4]
    month = date_string [5:7]
    day = date_string [8:10]
    return f'{day}.{month}.{year}'

user_input = input("Введите дату  (например: 2024-03-11T02:26:18.671407): ")
print("Результат:", get_date(user_input))