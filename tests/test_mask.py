import pytest

from src.mask import get_mask_account, get_mask_card_number


def test_get_mask_card_number_empty(empty_string):
    assert get_mask_card_number("") == empty_string


# Параметризация. Проверка работы функции на различных входных
# форматах номеров карт, включая граничные случаи и нестандартные длины номеров.
# Тестирование правильности маскирования номера карты


@pytest.mark.parametrize(
    "value, expected",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("7000792289606362", "7000 79** **** 6362"),
        (7000792289606362, "7000 79** **** 6362"),
        ("700079228960636333", "Длина номера карты более 16 знаков"),
    ],
)
def test_get_mask_card_number_parametrize(value, expected):

    assert get_mask_card_number(value) == expected


# Фикстура. Проверка работы номера счета с другой  длиной
def test_get_mask_account(low_account_number):
    assert get_mask_account("654108430135874305") == low_account_number


# Параметризация. Тестирование правильности маскирования номера счета.
# Проверка работы функции с различными форматами и длинами номеров счетов.
@pytest.mark.parametrize(
    "value, expected",
    [
        ("73654108430135874305", "**4305"),
        ("73654108430135874306", "**4306"),
        (73654108430135874305, "**4305"),
        (654108430135874305, "Hомер счета меньше или больше ожидаемой длины"),
    ],
)
def test_get_mask_account_parametrize(value, expected):
    assert get_mask_account(value) == expected
