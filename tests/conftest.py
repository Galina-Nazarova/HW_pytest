import pytest

@pytest.fixture
def numbers():
    return "321" # ожидаемый результат

@pytest.fixture
def letters():
    return "olleh" # ожидаемый результат