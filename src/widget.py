from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """Маскирует номер карты или счета вместе с его названием."""
    if not account_card:
        raise ValueError("Строка не должна быть пустой")

    # Разделяем строку по пробелам на элементы
    parts = account_card.split()

    # Номер счета/карты
    number = parts[-1]

    # Формируем имя карты
    name_card = " ".join(parts[:-1])

    """Функция принимает номер счета или карты, маскируя их"""

    if len(number) == 20:  # Если это номер счета
        masked_number = get_mask_account(number)

    elif len(number) == 16:  # Если это номер карты
        masked_number = get_mask_card_number(number)
    else:
        # На случай, если ввели неверное количество цифр
        raise ValueError("Неверное количество цифр в номере карты или счета")
    return f"{name_card} {masked_number}".strip()


def get_date(date_string: str) -> str:
    if not date_string or not date_string.strip():
        raise ValueError("Строка с датой отсутствует или пуста")

    # Необходим ISO формат: минимум 10 символов ГГГГ-ММ-ДД)
    if len(date_string) < 10 or date_string[4] != "-" or date_string[7] != "-":
        raise ValueError("Неверный формат даты. Ожидается ГГГГ-ММ-ДД")

    year = date_string[:4]
    month = date_string[5:7]
    day = date_string[8:10]

    # Проверка, что выделенные части состоят только из цифр
    if not (year.isdigit() and month.isdigit() and day.isdigit()):
        raise ValueError("Компоненты даты должны содержать только цифры")

    return f"{day}.{month}.{year}"
