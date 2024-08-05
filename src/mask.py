

def get_mask_card_number(card_number: int) -> str:
    """Функция вернет замаскированный номер карты в соответствии с шаблоном
    XXXX XX** **** XXXX, где X — это цифра номера"""
    place_of_space = [4, 9, 14]
    place_of_star = [7, 8, 10, 11, 12, 13]
    card_number_list = list(map(int, str(card_number)))
    for i in range(len(card_number_list)):
        if i in place_of_star:
            card_number_list[i] = "*"
        if i in place_of_space:
            card_number_list.insert(i, " ")
    return "".join(map(str, card_number_list))


def get_mask_account(bank_account: int) -> str:
    """Функция вернет замаскированный номер счета в соответствии с шаблоном
    **XXXX, где X — это цифра номера"""
    place_of_star = [0, 1]
    bank_account_list = list(map(int, str(bank_account)))[14:]
    bank_account_masks = [
        "*" if bank_account_list.index(el) in place_of_star else el for el in bank_account_list
    ]
    return "".join(map(str, bank_account_masks))


if __name__ == "__main__":
    print(get_mask_card_number(7000792289606361))
    print(get_mask_account(73654108430135874305))
