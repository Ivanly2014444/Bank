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