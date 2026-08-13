import json
import logging
import os
import re
from collections import Counter

os.makedirs("logs", exist_ok=True)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/utils.log", "w", encoding="utf-8")
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s: %(message)s"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_financial_data(path_file):
    """
    Читает JSON-файл и возвращает список транзакций.
    Если файл пустой, содержит не список или не найден, возвращает пустой список.

    """
    logger.info(f"Попытка чтения файла: {path_file}")
    try:
        with open(path_file, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                logger.info("Данные успешно прочитаны из файла")
                return data
            else:
                logger.warning(
                    f"Файл {path_file} содержит корректный JSON, но это не список"
                )
                return []
    except FileNotFoundError:
        logger.error(f"Файл не найден по пути: {path_file}")
        return []
    except json.JSONDecodeError:
        logger.error(f"{path_file} не является правильным JSON-текстом")
        return []


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """Фильтрует список банковских операций по поисковой строке в описании"""
    pattern = re.compile(search, re.IGNORECASE)

    filtered_data = []

    for d in data:
        description = d.get("description", "")
        if pattern.search(description):
            filtered_data.append(d)

    return filtered_data


def process_bank_operations(data: list[dict], categories: list[str]) -> dict:
    """Подсчитывает количество операций для каждой категории с помощью Counter."""
    found_categories = []

    for d in data:
        description = d.get("description", "")

        for c in categories:

            if re.search(c, description, re.IGNORECASE):
                found_categories.append(c)
                break

    counts = Counter(found_categories)

    return {c: counts[c] for c in categories}
