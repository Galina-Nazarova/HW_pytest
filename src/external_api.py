import os
from typing import Any, Dict
import requests
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv("API_KEY")
print(f"Мой ключ загрузился: {API_KEY}")


def convert_transactions(transaction: Dict[str, Any]) -> float:
    """
    Функция принимает на вход транзакцию и возвращает
    сумму транзакции (amount) в рублях, тип данных —
    float. Если транзакция была в USD или  EUR,
    происходит обращение к внешнему API для получения
    текущего
    курса валют и конвертации суммы операции в рубли.
    Для конвертации валюты воспользуйтесь
    Exchange Rates Data API:
    https://apilayer.com/exchangerates_data-api.
    Функцию конвертации поместите в модуль external_api.
    Используйте переменные окружения из файла
    .env для сокрытия чувствительных данных
    (токенов доступа для API). Создайте шаблон файла .env
    и разместите в репозитории на GitHub.
    Напишите тесты для новых функций, используйте
    Mock и patch.
    """
    try:
        # Извлекаем данные из структуры транзакции
        amount_data = transaction.get("operationAmount", {})
        amount = float(amount_data.get("amount", 0))
        currency = amount_data.get("currency", {}).get("code")

        # Если уже в рублях — просто возвращаем число
        if currency == "RUB":
            return amount

        if currency in ["USD", "EUR"]:
            url = "https://api.apilayer.com/exchangerates_data/convert"

            params = {
                "to": "RUB",
                "from": currency,
                "amount": amount
            }

            headers = {"apikey": API_KEY}

            response = requests.get(url, params=params, headers=headers, timeout=5)
            status_code = response.status_code
            print('f Статус код:{status_code}')
            response.raise_for_status()
            data = response.json()
            return float(data.get("result", 0.0))

    except Exception:
        return 0.0



