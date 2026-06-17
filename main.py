import sys
from pathlib import Path
from typing import Any, Dict, List

from src.data_load import read_csv_transactions, read_excel_transactions
from src.processing import sort_by_date
from src.search_data import process_bank_operations, process_bank_search
from src.utils import get_data  # Чтение JSON
from src.widget import get_date, mask_account_card


def main() -> None:
    """Реализует основную логику программы."""
    current_dir = Path(__file__).resolve().parent

    print("Привет! Добро пожаловать в программу работы "
          "with банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    user_choice = input("Пользователь: ").strip()
    data: List[Dict[str, Any]] = []

    if user_choice == "1":
        print("\nПрограмма: Для обработки выбран JSON-файл.")
        json_path = current_dir / "data" / "operations.json"
        data = get_data(str(json_path))
    elif user_choice == "2":
        print("\nПрограмма: Для обработки выбран CSV-файл.")
        csv_path = current_dir / "data" / "transactions.csv"
        data = read_csv_transactions(str(csv_path))
    elif user_choice == "3":
        print("\nПрограмма: Для обработки выбран XLSX-файл.")
        excel_path = current_dir / "data" / "transactions_excel.xlsx"
        data = read_excel_transactions(str(excel_path))
    else:
        print("\nПрограмма: Неверный пункт меню. Завершение работы.")
        sys.exit()

    valid_statuses = {"EXECUTED", "CANCELED", "PENDING"}
    status_input = ""

    while True:
        print("\nПрограмма: Введите статус, по которому необходимо "
              "выполнить фильтрацию.")
        print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
        status_input = input("Пользователь: ").strip().upper()

        if status_input in valid_statuses:
            print(f'\nПрограмма: Операции отфильтрованы '
                  f'по статусу "{status_input}"')
            break
        else:
            print(f'\nПрограмма: Статус операции "{status_input}" '
                  f'недоступен.')

    filtered_data = [
        op for op in data if str(op.get("state", "")).upper() == status_input
    ]

    print("\nПрограмма: Отсортировать операции по дате? Да/Нет")
    sort_choice = input("Пользователь: ").strip().lower()

    if sort_choice == "да":
        print("\nПрограмма: Отсортировать по возрастанию или по убыванию?")
        sort_order = input("Пользователь: ").strip().lower()

        is_reverse = True if "убыван" in sort_order else False
        filtered_data = sort_by_date(filtered_data, sort_rules=is_reverse)

    print("\nПрограмма: Выводить только рублевые транзакции? Да/Нет")
    rub_choice = input("Пользователь: ").strip().lower()

    if rub_choice == "да":
        rub_variants = {"RUB", "руб."}
        filtered_data = [
            op for op in filtered_data
            if str(op.get("operationAmount", {}).get("currency", {})
                   .get("code")).upper() in rub_variants
            or str(op.get("operationAmount", {}).get("currency", {})
                   .get("name")).lower() in rub_variants
        ]

    print("\nПрограмма: Отфильтровать список транзакций по определенному "
          "слову в описании? Да/Нет")
    word_choice = input("Пользователь: ").strip().lower()

    if word_choice == "да":
        search_word = input("Введите слово для поиска: ").strip()
        filtered_data = process_bank_search(filtered_data, search_word)

    print("\nПрограмма: Распечатываю итоговый список транзакций...\n")

    if not filtered_data:
        print("Программа: Не найдено ни одной транзакции, "
              "подходящей под ваши условия фильтрации")
        return

    print(f"Программа: Всего банковских операций в выборке: "
          f"{len(filtered_data)}\n")

    for op in filtered_data:

        raw_date = str(op.get("date", ""))
        formatted_date = "Дата неизвестна"
        if raw_date:
            try:
                formatted_date = get_date(raw_date)
            except Exception:
                formatted_date = raw_date[:10]

        description = op.get("description", "Без описания")

        from_info = str(op.get("from", "")).strip()
        to_info = str(op.get("to", "")).strip()

        if from_info and from_info != "None":
            masked_from = mask_account_card(from_info)
        else:
            masked_from = ""

        if to_info and to_info != "None":
            masked_to = mask_account_card(to_info)
        else:
            masked_to = ""

        if masked_from:
            transfer_route = f"{masked_from} -> {masked_to}"
        else:
            transfer_route = masked_to

        amount = op.get("operationAmount", {}).get("amount", "0")
        currency = op.get("operationAmount", {}).get("currency", {})
        cur_name = currency.get("name", "")

        print(f"{formatted_date} {description}")
        print(transfer_route)
        print(f"Сумма: {amount} {cur_name}\n")

        print("--- Аналитика категорий в итоговой выборке ---")
        cats = [
            "Перевод организации",
            "Перевод со счета на счет",
            "Открытие вклада"
        ]
        print(process_bank_operations(filtered_data, cats))

    if __name__ == "__main__":
        main()
