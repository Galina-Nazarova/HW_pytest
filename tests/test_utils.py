import json
import pytest
from src.utils import get_data


def test_get_data_successfull(mocker):
    """Тест: файл существует и содержит корректный список транзакций"""
    # 1. Готовим фейковые данные
    mock_data = [{
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }]
    mocker.patch("src.utils.Path.exists", return_value=True)
    mocker.patch("builtins.open", mocker.mock_open(read_data='[]'))
    mocker.patch("json.load", return_value=mock_data)

    result = get_data("fake_path.json")

    assert result == mock_data
    assert isinstance(result, list)


def test_get_data_file_not_found(mocker):
    """Тест: файла нет -> должен вернуться []"""
    mocker.patch("src.utils.Path.exists", return_value=False)

    assert get_data("non_existent.json") == []


def test_get_data_invalid_json(mocker):
    """Тест: файл содержит ошибку (не JSON) -> должен вернуться []"""
    mocker.patch("src.utils.Path.exists", return_value=True)
    mocker.patch("builtins.open", mocker.mock_open(read_data='invalid json'))
    mocker.patch("json.load", side_effect=json.JSONDecodeError("msg", "doc", 0))

    assert get_data("corrupt.json") == []


def test_get_data_not_a_list(mocker):
    """Тест: в файле словарь вместо списка -> должен вернуться []"""
    mocker.patch("src.utils.Path.exists", return_value=True)
    mocker.patch("builtins.open", mocker.mock_open(read_data='{}'))
    mocker.patch("json.load", return_value={"id": 1})  # Вернули словарь

    assert get_data("not_a_list.json") == []
