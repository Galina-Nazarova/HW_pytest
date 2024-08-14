def filter_by_currency(transactions: list, type_of_valuta: str):
    """Функция генератор принимает на вход список словарей, представляющих транзакции.
    Функция генератор возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной (например, USD)."""
    # цикл для перебора элементов списка - словарей
    if len(transactions) == 0:
        raise AssertionError("Дан пустой список")
    else:
        for transaction in transactions:
            # условие для проверки равенства значения ключей "name" и "code" аданному аргументу
            if transaction["operationAmount"]["currency"]["name"] == type_of_valuta and transaction["operationAmount"]["currency"]["code"] == type_of_valuta:
                yield transaction

def transaction_descriptions(transactions: list):
    """Функция генератор принимает список словарей с транзакциями и
    возвращает описание каждой операции по очереди"""
    # цикл для перебора элементов списка - словарей
    for transaction in transactions:
        yield transaction["description"]

def card_number_generator(start: int, stop: int):
    """Функция генератор  выдает номера банковских карт в формате XXXX XXXX XXXX XXXX
    , где X — цифра номера карты.
    Генератор может сгенерировать номера карт в заданном диапазоне
    от 0000 0000 0000 0001 до 9999 9999 9999 9999.
    Генератор должен принимать начальное и конечное значения для генерации диапазона номеров."""
    for number in range(start, stop+1):
        yield ' '.join("{:016}".format(number)[i:i + 4] for i in range(0, 16, 4))


if __name__ == '__main__':
    transactions = []
    usd_transactions = filter_by_currency(transactions, "USD")
    for _ in range(2):
        print(next(usd_transactions))

    descriptions = transaction_descriptions(transactions)
    for _ in range(2):
        print(next(descriptions))

    for card_number in card_number_generator(1, 5):
        print(card_number)
