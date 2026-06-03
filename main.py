from pathlib import Path

from src.external_api import convert_transactions
from src.mask import get_mask_account, get_mask_card_number
from src.utils import get_data

current_dir = Path(__file__).resolve().parent
DATA_PATH = current_dir / "data" / "operations.json"
transactions = get_data(file_path=DATA_PATH)

# пустой список для хранения результатов amount
"""for transaction in transactions:
    if transaction == 1:
        rub_amount = convert_transactions(transaction)

        print(rub_amount)"""
for transaction in transactions:
    # Проверяем, что перед нами словарь (а не число 1)
    if isinstance(transaction, dict):
        # 1. Считаем сумму в рублях
        rub_amount = convert_transactions(transaction)
        print(f"Сумма: {rub_amount}")

        # 2. Маскируем данные (чтобы сработал masks.log)
        if "to" in transaction:
            info_to = transaction["to"]
            if "Счет" in info_to:
                print(get_mask_account(info_to))
            else:
                print(get_mask_card_number(info_to))

        # Прерываем цикл после первой транзакции, чтобы просто проверить работу
        break
