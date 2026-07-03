def filter_by_state(data: list[dict], state: str="EXECUTED") -> list[dict]:
    result = []
    for item in data:
        if item.get("state") == state:
            result.append(item)
    return result


def sort_by_date(data: list[dict], descending: bool = True) -> list[dict]:
    return sorted(data, key=lambda x: x["date"], reverse=descending)


if __name__ == "__main__":
    # 1. Создаем тестовый список словарей
    test_data = [
        {"id": 414288290, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]

    # 2. Проверяем работу по умолчанию (должен найти EXECUTED)
    print("Проверка со статусом по умолчанию (EXECUTED):")
    result_default = filter_by_state(test_data)
    print(result_default)

    print("\nПроверка со статусом CANCELED:")
    result_canceled = filter_by_state(test_data, "CANCELED")
    print(result_canceled)

    result_sorted = sort_by_date(test_data)
    print(f"Сортировка по убыванию:\n{result_sorted}")
