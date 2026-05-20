import json
from pathlib import Path
from typing import Any, Dict, List


def get_data(file_path: str) -> List[Dict[str, Any]]:
    """Функуия принимает на вход путь до JSON-файла
    и возвращает список словарей с данными о
    финансовых транзакциях. Если файл пустой,
    содержит не список или не найден, функция
    возвращает пустой список. Функцию поместите в модуль
    utils Файл с данными о финансовых транзациях
    operations.json поместите в директорию
    data/ в корне проекта.
    Ссылка на файл: operations.json."""
    path = Path(file_path)
    # Проверка на существование файла
    print(path.absolute())
    if not path.exists():
        return []
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            return []
    except (json.JSONDecodeError, Exception):
        return []
