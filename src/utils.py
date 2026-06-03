import json
from pathlib import Path
from typing import Any, Dict, List
import logging
from logger import setup_logging

logger: logging.Logger = setup_logging("logs/utils.log")
logger.name = "utils"


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
    logger.debug(f"Попытка чтения данных из файла: {file_path}")
    path = Path(file_path)
    print(path.absolute())
    if not path.exists():
        logger.error(f"Ошибка: Файл не найден по пути {path.absolute()}")
        return []
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, list):
                logger.info(f"Успешно прочитано транзакций: {len(data)}")
                return data
            logger.error(
                "Ошибка: JSON содержит структуру, "
                "отличную от списка (list)"
            )
            return []
    except json.JSONDecodeError as e:
        logger.error(
            f"Ошибка: Некорректный формат JSON. "
            f"Подробности: {e}"
        )
        return []
    except Exception as e:
        logger.error(
            f"Произошла непредвиденная ошибка "
            f"при чтении файла: {e}"
        )
        return []
