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
def is_account():
    return "Счет **5560" # ожидаемый результат


@pytest.fixture
def is_card_number():
    return "Visa Platinum 7000 79** **** 6361" # ожидаемый результат
@pytest.fixture
def letters():
    return "olleh" # ожидаемый результат

#Тестирование правильности преобразования даты.
@pytest.fixture
def is_true_data_formate():
    return "11.03.2024" # ожидаемый результат


@pytest.fixture
def is_true_state_value():
    return [
        {
            'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'
        }, {
            'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'
        }
    ] # ожидаемый результат

