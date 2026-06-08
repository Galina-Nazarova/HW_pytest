import csv
from pathlib import Path

import pandas as pd


def read_csv_transactions(file_path):
    """Считывает финансовые операции из CSV-файла и
        возвращает список словарей."""
    transactions = []
    path = Path(file_path)

    if not path.exists():
        return transactions

    try:
        with open(path, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=";")
            for row in reader:
                if not row.get("id"):
                    continue

                # Безопасно переводим сумму в float
                try:
                    amount_val = float(row.get("amount", 0))
                except (ValueError, TypeError):
                    amount_val = 0.0

                transaction = {
                    "id": int(row["id"]),
                    "state": row.get("state", ""),
                    "date": row.get("date", ""),
                    "operationAmount": {
                        "amount": amount_val,  # Теперь здесь сразу число float
                        "currency": {
                            "name": row.get("currency_name", ""),
                            "code": row.get("currency_code", ""),
                        },
                    },
                    "from": row.get("from", ""),
                    "to": row.get("to", ""),
                    "description": row.get("description", ""),
                }
                transactions.append(transaction)
    except Exception:
        return []

    return transactions


def read_excel_transactions(file_path):
    """Считывает финансовые операции из Excel-файла (.xlsx) и
        возвращает список словарей."""
    transactions = []
    path = Path(file_path)

    if not path.exists():
        return transactions

    try:
        df = pd.read_excel(path, dtype=str)
        df = df.fillna("")

        for _, row in df.iterrows():
            if not row.get("id"):
                continue

            raw_id = row["id"]
            if "." in raw_id:
                raw_id = raw_id.split(".")[0]

            try:
                amount_val = float(row.get("amount", 0))
            except (ValueError, TypeError):
                amount_val = 0.0

            transaction = {
                "id": int(raw_id),
                "state": row.get("state", ""),
                "date": row.get("date", ""),
                "operationAmount": {
                    "amount": amount_val,  # Теперь здесь сразу число float
                    "currency": {
                        "name": row.get("currency_name", ""),
                        "code": row.get("currency_code", ""),
                    },
                },
                "from": row.get("from", ""),
                "to": row.get("to", ""),
                "description": row.get("description", ""),
            }
            transactions.append(transaction)
    except Exception:
        return []

    return transactions
