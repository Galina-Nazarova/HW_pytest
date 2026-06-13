from pathlib import Path

from src.data_load import read_csv_transactions, read_excel_transactions
from src.external_api import convert_transactions
from src.mask import get_mask_account, get_mask_card_number
from src.utils import get_data

current_dir = Path(__file__).resolve().parent
#DATA_PATH = current_dir / "data" / "operations.json"
#transactions = get_data(file_path=DATA_PATH)

DATA_PATH = current_dir / "data" / "transactions.csv"
transactions = read_csv_transactions(DATA_PATH)

# DATA_PATH = current_dir / "data" / "transactions_excel.xlsx"
# transactions = read_excel_transactions(DATA_PATH)


# пустой список для хранения результатов amount
"""for transaction in transactions:
    if transaction == 1:
        rub_amount = convert_transactions(transaction)

        print(rub_amount)"""

for transaction in transactions:
    if isinstance(transaction, dict):
        # 1. Выводим сумму
        rub_amount = convert_transactions(transaction)
        print(f"Сумма: {rub_amount}")

        # 2. Маскируем данные на основе длины или содержимого
        if "to" in transaction:
            info_to = str(transaction["to"]).strip()

            # Убираем лишние слова, чтобы посчитать чистые цифры
            digits_only = "".join(c for c in info_to if c.isdigit())

            if "Счет" in info_to or len(digits_only) == 20:
                print(get_mask_account(info_to))
            else:
                print(get_mask_card_number(info_to))

        # Прерываем цикл после первой транзакции для проверки
        break
