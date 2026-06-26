def get_mask_card_number(card_number: str) -> str:
    """ Функция принимает на вход номер карты и возвращает ее маску """
    card_start = card_number[0:6]
    card_end = card_number[-4:]
    hidden_part = card_number[6:-4]

    masked_number = card_start + len(hidden_part) * "*" + card_end

    part_1 = masked_number[0:4]
    part_2 = masked_number[4:8]
    part_3 = masked_number[8:12]
    part_4 = masked_number[12:16]

    return f"{part_1} {part_2} {part_3} {part_4}"


def get_mask_account(account_number: str) -> str:
    """ Функция принимает на вход номер счета и возвращает ее маску """
    account_end = account_number[-4:]
    stars_mask = "**"

    masked_account = stars_mask + account_end

    return masked_account


user_card = input("Введите номер карты: ")
print(get_mask_card_number(user_card))

user_account = input("Введите номер счета: ")
print(get_mask_account(user_account))
