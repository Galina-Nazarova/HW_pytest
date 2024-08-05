import pytest


# фикстура. Проверка, что функция корректно обрабатывает входные строки,
# где отсутствует номер карты.
@pytest.fixture
def empty_string():
    return "Номер карты отсутствует" # ожидаемый результат



@pytest.fixture
def letters():
    return "olleh" # ожидаемый результат