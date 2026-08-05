import json
import logging
import os

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
