import pytest

from src.search_data import process_bank_operations, process_bank_search


@pytest.fixture
def sample_data():
    return [
        {"id": 1, "description": "Перевод организации"},
        {"id": 2, "description": "Открытие вклада"},
        {"id": 3, "description": "Перевод с карты на карту"},
        {"id": 4, "description": "Перевод организации"},
    ]


def test_process_bank_search_found(sample_data):
    """Тест для поиска подстроки."""
    result = process_bank_search(sample_data, "Перевод")
    assert len(result) == 3


def test_process_bank_search_empty(sample_data):
    """Тест для передачи пустой строки поиска."""
    result = process_bank_search(sample_data, "")
    assert len(result) == 4


def test_process_bank_operations_counter(sample_data):
    """Тест для точного подсчета категорий с помощью Counter."""
    categories = ["Перевод организации", "Открытие вклада", "Прочее"]
    result = process_bank_operations(sample_data, categories)

    assert result["Перевод организации"] == 2
    assert result["Открытие вклада"] == 1
    assert result["Прочее"] == 0