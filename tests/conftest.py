import pytest


# фикстура
@pytest.fixture
def card_numbers():
    return "7000 79** **** 6361" # ожидаемый результат


@pytest.fixture
def letters():
    return "olleh" # ожидаемый результат