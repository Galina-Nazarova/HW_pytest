from pathlib import Path

from src.external_api import convert_transactions
from src.utils import get_data

current_dir = Path(__file__).resolve().parent
DATA_PATH = current_dir / "data" / "operations.json"
transactions = get_data(file_path=DATA_PATH)

# пустой список для хранения результатов amount
for transaction in transactions:
    if transaction == 1:
        rub_amount = convert_transactions(transaction)

        print(rub_amount)

"""amounts_in_rub = []

for transaction in transactions:
    rub_amount = convert_transactions(transaction)
    amounts_in_rub.append(rub_amount)

print(amounts_in_rub)"""