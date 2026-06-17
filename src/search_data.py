import re
from collections import Counter
from typing import Any, Dict, List


def process_bank_search(
        data: List[Dict[str, Any]],
        search_str: str
) -> List[Dict[str, Any]]:
    """Фильтруем список транзакций по строке
    поиска в поле 'description'.
    Используем регулярные выражения для
    поиска совпадений без учета регистра.
    """
    if not search_str:
        return data

    filtered_data: List[Dict[str, Any]] = []
    # Компилируем паттерн с флагом игнорирования регистра
    pattern = re.compile(re.escape(search_str), re.IGNORECASE)

    for operation in data:
        description = operation.get("description", "")
        if isinstance(description, str):
            if pattern.search(description) or search_str.lower() in description.lower():
                filtered_data.append(operation)

    return filtered_data


def process_bank_operations(
        data: List[Dict[str, Any]],
        categories: List[str]
) -> Dict[str, int]:
    """Подсчитываем количество операций для
    заданных категорий в поле 'description'.
    Используем Counter из библиотеки collections.
    """
    # Собираем все описания из транзакций
    descriptions = [
        str(operation.get("description", ""))
        for operation in data
        if operation.get("description")
    ]

    counts = Counter(descriptions)

    result: Dict[str, int] = {
        category: counts[category] for category in categories
    }

    return result
