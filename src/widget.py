import src.mask as mk

# после девелоп
# develop


def mask_account_card(type_and_number_of_card: str) -> str:
    """Функция вернет замаскированный номер счета в соответствии с шаблоном
     **XXXX, где X — это цифра номера счета
     XXXX XX** **** XXXX, где X — это цифра номера карты
      с названием

      """
    name = ''
    digit = ''
    for el in type_and_number_of_card:
        if el.isdigit():
            digit += el
        else:
            name += el
    if len(digit) == 20:
        bank_account_masks = mk.get_mask_account(int(digit))
        return name + bank_account_masks
    else:
        card_number_masks = mk.get_mask_card_number(int(digit))
        return name + card_number_masks


def get_date(initial_data_format: str) -> str:
    """Функция вернет дату в соответствии с шаблоном
    "ДД.ММ.ГГГГ" ("11.03.2024") """
    date = initial_data_format[8:10] + '.'
    date_format = date + initial_data_format[5:7] + '.' + initial_data_format[:4]
    return date_format


if __name__ == "__main__":

    print(mask_account_card('Счет 35383033474447895560'))
    print(get_date("2024-03-11T02:26:18.671407"))
    # print(get_mask_card_number(7000792289606361))
    # print(get_mask_account(73654108430135874305))
