from unittest.mock import mock_open, patch

import pandas as pd

from src.data_load import read_csv_transactions, read_excel_transactions


# --- ТЕСТЫ ДЛЯ CSV ---
@patch("builtins.open", new_callable=mock_open, read_data=(
    "id;state;date;amount;currency_name;currency_code;from;to;description\n"
    "650703;EXECUTED;2023-09-05;16210.0;Sol;PEN;Счет 123;Счет 456;Перевод\n"
))
@patch("pathlib.Path.exists")
def test_read_csv_transactions_success(mock_exists, mock_file):
    """Тест успешного чтения корректного CSV-файла
     с разделителем ';'."""
    mock_exists.return_value = True

    result = read_csv_transactions("fake_path.csv")

    assert len(result) == 1
    # Поскольку результат — это список словарей, берем первый элемент [0]
    assert result[0]["id"] == 650703
    assert result[0]["operationAmount"]["amount"] == 16210.0
    assert result[0]["operationAmount"]["currency"]["code"] == "PEN"


@patch("pathlib.Path.exists")
def test_read_csv_transactions_file_not_found(mock_exists):
    """Тест возврата пустого списка, если CSV-файл
    не существует."""
    mock_exists.return_value = False
    result = read_csv_transactions("non_existent.csv")
    assert result == []


@patch("builtins.open", side_effect=Exception("Ошибка чтения"))
@patch("pathlib.Path.exists")
def test_read_csv_transactions_exception(mock_exists, mock_file):
    """Тест перехвата исключений при ошибках чтения CSV."""
    mock_exists.return_value = True
    result = read_csv_transactions("corrupted.csv")
    assert result == []


# --- ТЕСТЫ ДЛЯ EXCEL ---
@patch("pandas.read_excel")
@patch("pathlib.Path.exists")
def test_read_excel_transactions_success(mock_exists, mock_read_excel):
    """Тест успешного парсинга DataFrame из Excel-файла."""
    mock_exists.return_value = True

    # Имитируем данные, которые возвращает pandas.read_excel
    mock_df = pd.DataFrame(
        [
            {
                "id": "3598919",
                "state": "EXECUTED",
                "date": "2020-12-06",
                "amount": "29740",
                "currency_name": "Peso",
                "currency_code": "COP",
                "from": "Discover 111",
                "to": "Discover 222",
                "description": "Перевод с карты",
            }
        ]
    )
    mock_read_excel.return_value = mock_df

    result = read_excel_transactions("fake_path.xlsx")

    assert len(result) == 1
    assert result[0]["id"] == 3598919
    assert result[0]["operationAmount"]["amount"] == 29740.0


@patch("pathlib.Path.exists")
def test_read_excel_transactions_file_not_found(mock_exists):
    """Тест возврата пустого списка."""
    mock_exists.return_value = False
    result = read_excel_transactions("non_existent.xlsx")
    assert result == []


@patch("pandas.read_excel")
@patch("pathlib.Path.exists")
def test_read_excel_transactions_exception(mock_exists, mock_read_excel):
    """Тест обработки исключения при ошибке чтения Excel."""
    mock_exists.return_value = True
    mock_read_excel.side_effect = Exception("Ошибка формата файла")

    result = read_excel_transactions("corrupted.xlsx")
    assert result == []
