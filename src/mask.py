from typing import Union


def get_mask_card_number(card_number: Union[str, int, list]) -> str:
    """Функция вернет замаскированный номер карты в соответствии с шаблоном
    XXXX XX** **** XXXX, где X — это цифра номера"""
    if isinstance(card_number, int):
        card_number = str(card_number)
    if len(card_number) > 16:
        return ("Длина номера карты более 16 знаков")
    elif card_number == "":
        return "Номер карты отсутствует"

    place_of_space = [4, 9, 14]
    place_of_star = [7, 8, 10, 11, 12, 13]
    card_number_list = list(map(int, card_number))
    for i in range(len(card_number_list)):
        if i in place_of_star:
            card_number_list[i] = "*"
        if i in place_of_space:
            card_number_list.insert(int(i), " ")
    return "".join(map(str, card_number_list))


def get_mask_account(bank_account: Union[str, int]) -> str:
    """Функция вернет замаскированный номер счета в соответствии с шаблоном
    **XXXX, где X — это цифра номера"""
    if isinstance(bank_account, int):
        bank_account = str(bank_account)
    if len(bank_account) != 20:
        return "Hомер счета меньше или больше ожидаемой длины"
    else:
        bank_account_masks = []
        place_of_star = [0, 1]
        bank_account_list = list(map(int, bank_account))[14:]
        bank_account_masks = [
            "*" if bank_account_list.index(el) in place_of_star else el for el in bank_account_list
        ]
        return "".join(map(str, bank_account_masks))
