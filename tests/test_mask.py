import pytest
from src.mask import get_mask_card_number

def test_get_mask_card_number_empty(empty_string):
        assert get_mask_card_number("") == empty_string

# Параметризация. Проверка работы функции на различных входных
# форматах номеров карт, включая граничные случаи и нестандартные длины номеров.
# Тестирование правильности маскирования номера карты
@pytest.mark.parametrize('value, expected', [
    ("7000792289606361", "7000 79** **** 6361"),
    ("7000792289606362", "7000 79** **** 6362"),
    ("700079228960636333", "Длина номера карты более 16 знаков"),
]
                         )
def test_get_mask_card_number_parametrize(value, expected):
    assert get_mask_card_number(value) == expected
