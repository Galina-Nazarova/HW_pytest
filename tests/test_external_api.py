from src.external_api import convert_transactions


def test_convert_transactions_rub():
    """Проверяет, если валюта RUB, API не вызывается,
    возвращается сумма как float"""
    transaction = {
        "operationAmount": {
            "amount": "100.50",
            "currency": {"code": "RUB"}
        }
    }
    # Здесь mocker не нужен, так как запроса в интернет не будет
    assert convert_transactions(transaction) == 100.50


def test_convert_transactions_usd_success(mocker):
    """Иммитирует успешный ответ API для USD (курс 75.0)"""
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"result": 4300.0}
    mocker.patch("requests.get", return_value=mock_response)

    transaction = {
        "operationAmount": {
            "amount": "100",
            "currency": {"code": "USD"}
        }
    }
    assert convert_transactions(transaction) == 4300.0


def test_convert_transactions_api_error(mocker):
    """Тест: если API выдает ошибку (например, 401 или 429)"""
    mock_response = mocker.Mock()
    mock_response.status_code = 429
    mocker.patch("requests.get", return_value=mock_response)

    transaction = {
        "operationAmount": {"amount": "100", "currency": {"code": "EUR"}}
    }
    assert convert_transactions(transaction) == 0.0


def test_convert_transactions_network_exception(mocker):
    """Тест: если вообще нет интернета (Exception)"""
    mocker.patch("requests.get", side_effect=Exception("Connection Error"))

    transaction = {
        "operationAmount": {"amount": "100", "currency": {"code": "USD"}}
    }

    assert convert_transactions(transaction) == 0.0
