from src.csv_xlsx_loader import read_transactions_xlsx
from src.file_readers import read_transactions_csv
from src.processing import filter_by_state, sort_by_date
from src.utils import get_financial_data, process_bank_search
from src.widget import get_date, mask_account_card


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    while True:
        choice = input("Пользователь: ")

        transactions = []
        if choice == "1":
            print("Программа: Для обработки выбран JSON-файл.")
            transactions = get_financial_data("data/operations.json")
            break

        elif choice == "2":
            print("Программа: Для обработки выбран CSV-файл.")
            transactions = read_transactions_csv("data/transactions.csv")
            break

        elif choice == "3":
            print("Программа: Для обработки выбран XLSX-файл.")
            transactions = read_transactions_xlsx("data/transactions_excel.xlsx")
            break

        else:
            print("Программа: Результат не найден, попробуйте снова")

    print(
        "Программа: Введите статус, по которому необходимо выполнить фильтрацию. "
        "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
    )

    while True:
        filter_choice = input("Пользователь: ").upper()

        if filter_choice == "EXECUTED":
            # ИСПРАВЛЕНИЕ: Результат сразу записываем в основную переменную transactions
            transactions = filter_by_state(transactions, filter_choice)
            print(f"Программа: Операции отфильтрованы по статусу {filter_choice}")
            break
        elif filter_choice == "CANCELED":
            transactions = filter_by_state(transactions, filter_choice)
            print(f"Программа: Операции отфильтрованы по статусу {filter_choice}")
            break
        elif filter_choice == "PENDING":
            transactions = filter_by_state(transactions, filter_choice)
            print(f"Программа: Операции отфильтрованы по статусу {filter_choice}")
            break
        else:
            print(f"Статус операции {filter_choice} недоступен.")

    # Блок сортировки по дате
    print("Программа: Отсортировать операции по дате? Да/Нет")
    sort_choice = input("Пользователь: ").lower()
    if sort_choice == "да":
        print("Программа: Отсортировать по возрастанию или по убыванию?")
        sort_by_order = input("Пользователь: ").lower()

        is_descending = sort_by_order == "по убыванию"
        transactions = sort_by_date(transactions, descending=is_descending)

    # Блок валюты
    print("Программа: Выводить только рублевые транзакции? Да/Нет")
    sort_by_currency = input("Пользователь: ").lower()
    if sort_by_currency == "да":
        transactions = [
            t
            for t in transactions
            if (
                # Для JSON структуры
                (
                    isinstance(t.get("operationAmount"), dict)
                    and t.get("operationAmount", {}).get("currency", {}).get("code")
                    == "RUB"
                )
                or t.get("currency_code") == "RUB"
                or t.get("currency") == "RUB"
            )
        ]

    # Блок фильтрации по слову
    print(
        "Программа: Отфильтровать список транзакций по определенному слову в описании? Да/Нет"
    )
    filtered_by_word_choice = input("Пользователь: ").lower()
    if filtered_by_word_choice == "да":
        print("Программа: Введите слово")
        user_input_word = input("Пользователь: ")
        transactions = process_bank_search(transactions, user_input_word)

    print("Программа: Распечатываю итоговый список транзакций...")

    if not transactions:
        print(
            "Программа: Не найдено ни одной транзакции, подходящей под ваши условия фильтрации"
        )
    else:
        print(f"Всего банковских операций в выборке: {len(transactions)}\n")

        for t in transactions:
            # Форматируем дату и берем описание
            date_string = t.get("date", "")
            description = t.get("description", "Описание отсутствует")

            formatted_date = get_date(date_string) if date_string else "Дата неизвестна"

            from_info = t.get("from", "")
            to_info = t.get("to", "")

            if from_info and to_info:
                direction = (
                    f"{mask_account_card(from_info)} -> {mask_account_card(to_info)}"
                )
            elif to_info:
                direction = mask_account_card(to_info)
            else:
                direction = mask_account_card(from_info) if from_info else ""

            if isinstance(t.get("operationAmount"), dict):
                amount = t["operationAmount"].get("amount", "0")
                currency = t["operationAmount"].get("currency", {}).get("code", "RUB")
            else:
                amount = t.get("amount", "0")
                currency = t.get("currency_code") or t.get("currency") or "RUB"

            print(f"{formatted_date} {description}")
            if direction:
                print(direction)
            print(f"Сумма: {amount} {currency}\n")


if __name__ == "__main__":
    main()
