import pytest

from src.widget import get_date, mask_account_card


def test_mask_account_card_account(is_account):
    """Тесты для проверки, что функция корректно распознает
    и применяет нужный тип маскировки в зависимости от типа входных данных (счет).
    """
    assert mask_account_card("Счет 35383033474447895560") == is_account


def test_mask_account_card_card(is_card_number):
    """# Тесты для проверки, что функция корректно распознает
    и применяет нужный тип маскировки в зависимости от типа входных данных (карта).
    и тестирование некорректных данных"""
    assert mask_account_card("Visa Platinum 7000792289606361") == is_card_number
    assert mask_account_card("Visa Platinum 7000792289606361") == is_card_number

    # Тестирование некорректных данных и проверка ее устойчивости к ошибкам
    with pytest.raises(AssertionError) as exc_info:
        mask_account_card("Visa Platinum !7000792289606361")

    # Проверяем, что сообщение об ошибке соответствует ожидаемому
    assert str(exc_info.value) == "Даны некорректные данные"


# Параметризация. Параметризованные тесты с разными типами карт и счетов
# для проверки универсальности функции.
@pytest.mark.parametrize(
    "value, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 7000792289606361", "Maestro 7000 79** **** 6361"),
        ("Счет 73654108430135874306", "Счет **4306"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card_parametrize(value, expected):
    assert mask_account_card(value) == expected


# Тестирование правильности преобразования даты.
def test_get_date(is_true_data_formate):
    assert get_date("2024-03-11T02:26:18.671407") == is_true_data_formate
    # Тестирование некорректных данных и проверка ее устойчивости к ошибкам
    with pytest.raises(AssertionError) as exc_info:
        get_date("")

    # Проверяем, что сообщение об ошибке соответствует ожидаемому
    assert str(exc_info.value) == "Даны некорректные данные"


# Проверка работы функции на различных входных форматах даты,
# включая граничные случаи и нестандартные строки с датами.
# Проверка, что функция корректно обрабатывает входные строки, где отсутствует дата.


@pytest.mark.parametrize(
    "value, expected",
    [
        ("2024-03-12T02:26:18.671407", "12.03.2024"),
        ("2024-03-12T02:26:18.671407", "12.03.2024"),
    ],
)
def test_get_date_parametrize(value, expected):
    assert get_date(value) == expected
