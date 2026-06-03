from typing import Union

import logging

from logger import setup_logging

logger: logging.Logger = setup_logging("logs/masks.log")
logger.name = "masks"


def get_mask_card_number(card_number: Union[str, int, list]) -> str:
    """Функция вернет замаскированный номер карты в соответствии с шаблоном
    XXXX XX** **** XXXX, где X — это цифра номера"""
    logger.debug(f"Начало маскирования номера карты: {card_number}")
    if isinstance(card_number, int):
        card_number = str(card_number)
    if len(card_number) > 16:
        logger.error(
            f"Ошибка: Длина номера карты "
            f"более 16 знаков ({len(card_number)})"
        )
        return "Длина номера карты более 16 знаков"
    elif card_number == "":
        logger.error("Ошибка: Номер карты отсутствует (пустая строка)")
        return "Номер карты отсутствует"

    place_of_space = [4, 9, 14]
    place_of_star = [7, 8, 10, 11, 12, 13]
    card_number_list = list(map(int, card_number))
    for i in range(len(card_number_list)):
        if i in place_of_star:
            card_number_list[i] = "*"
        if i in place_of_space:
            card_number_list.insert(int(i), " ")
    result = "".join(map(str, card_number_list))
    logger.info("Успешное маскирование номера карты")
    return result


def get_mask_account(bank_account: Union[str, int]) -> str:
    """Функция вернет замаскированный номер счета в соответствии с шаблоном
    **XXXX, где X — это цифра номера"""

    logger.debug(f"Начало маскирования номера счета: {bank_account}")
    if isinstance(bank_account, int):
        bank_account = str(bank_account)
    if len(bank_account) != 20:
        logger.error(
            f"Ошибка: Номер счета имеет "
            f"неверную длину ({len(bank_account)})"
        )
        return "Hомер счета меньше или больше ожидаемой длины"
    else:
        bank_account_masks = []
        place_of_star = [0, 1]
        bank_account_list = list(map(int, bank_account))[14:]

        # Записываем генератор в одну строку, чтобы flake8 не ругался
        # на отступы
        bank_account_masks = [
            "*" if bank_account_list.index(el) in place_of_star else el
            for el in bank_account_list
        ]
        result = "".join(map(str, bank_account_masks))
        logger.info("Успешное маскирование номера счета")
        return result
