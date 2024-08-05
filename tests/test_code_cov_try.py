from src.code_cov_try import finder

def test_finder_basic():
    assert finder([1, '2', [], {}, ('3',)], int) == 1
    assert finder([1, '2', [], {}, ('3',), 3], int) == 2

def test_finder_zero():
    assert finder([1, 2, [], {}, ('3',), 3], str) == 0


def test_finder_empty():
    assert finder([], str) == 0

def test_finder_not_list():
    assert finder(12345, int) == None

# поставить библиотеку покрытия poetry add --group dev pytest-cov
# покрытие кода тестами: pytest --cov

