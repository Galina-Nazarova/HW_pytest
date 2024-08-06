import pytest


# фикстура. Проверка, что функция корректно обрабатывает входные строки,
# где отсутствует номер карты.
@pytest.fixture
def empty_string():
    return "Номер карты отсутствует" # ожидаемый результат

@pytest.fixture
def low_account_number():
    return "Hомер счета меньше или больше ожидаемой длины" # ожидаемый результат

@pytest.fixture
def letters():
    return "olleh" # ожидаемый результат