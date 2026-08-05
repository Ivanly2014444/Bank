import json


def get_financial_data(path_file):
    """
    Читает JSON-файл и возвращает список транзакций.
    Если файл пустой, содержит не список или не найден, возвращает пустой список.

    """
    try:
        with open(path_file, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            else:
                return []
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []
