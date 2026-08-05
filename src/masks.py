import logging
import os

os.makedirs("logs", exist_ok=True)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/masks.log", "w", encoding="utf-8")
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s: %(message)s"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    logger.info("Начало маскирования номера карты")
    if len(card_number) != 16:
        logger.error(f"Некорректный номер карты: {card_number}")
        raise ValueError("Номер карты должен состоять из 16 цифр")
    card_start = card_number[0:6]
    card_end = card_number[-4:]
    hidden_part = card_number[6:-4]

    masked_number = card_start + len(hidden_part) * "*" + card_end

    part_1 = masked_number[0:4]
    part_2 = masked_number[4:8]
    part_3 = masked_number[8:12]
    part_4 = masked_number[12:16]
    logger.info("Номер карты успешно замаскирован")
    return f"{part_1} {part_2} {part_3} {part_4}"


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счета и возвращает ее маску"""
    logger.info("Начало маскирования номера счета")
    if len(account_number) != 20:
        logger.error(f"Некорректный номер счета: {account_number}")
        raise ValueError("Номер счета должен состоять из 20 цифр")
    account_end = account_number[-4:]
    stars_mask = "**"

    masked_account = stars_mask + account_end
    logger.info("Номер счета успешно замаскирован")
    return masked_account
