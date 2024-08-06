
import src.processing as proc
import pytest
from src.processing import calculate_logariphm



"""def test_add():
    assert add(2, 2) == 4

"""
def test_calculate_logariphm():
    assert calculate_logariphm(8, 2) == 3.0
    assert calculate_logariphm(8, 4) == 1.5


    with pytest.raises(ValueError):
        calculate_logariphm(0, 2)

    with pytest.raises(ValueError):
        calculate_logariphm(8, 0)
#для декоратора
"""def test_reverse_string_numbers(numbers):
    assert proc.reverse_string("123") == numbers


def test_reverse_string_letters(letters):
    assert proc.reverse_string("hello") == letters

# для параметризации

@pytest.mark.parametrize('value, expected', [
    ("123", "321"),
    ("hello", "olleh"),
    ("world", "dlrow"),
]
                         )
def test_reverse_string_numbers(value, expected):
    assert proc.reverse_string(value) == expected"""