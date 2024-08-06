

def filter_by_state(dict_list: list, state_key='EXECUTED') -> list:
    """ Функция принимает список словарей и опционально значение
    для ключа state(по умолчанию 'EXECUTED'). Функция возвращает
    новый список словарей, содержащий только те словари, у которых
    ключ state соответствует указанному значению."""
    # список для хранения отфильтрованных словарей
    new_dict_list = []
    # цикл для перебора элементов списка - словарей
    for dict_ in dict_list:
        # условие для проверки равенства значения ключа tste аданному аргументу
        if dict_['state'] == state_key:
            new_dict_list.append(dict_)
    if new_dict_list == []:
        raise AssertionError("Нет словарей с указанным статусом")

    return new_dict_list


def sort_by_date(dict_list: list, sort_rules: bool = True) -> list:
    """Функция принимает список словарей и необязательный
    параметр, задающий порядок сортировки (по умолчанию — убывание).
    Функция должна возвращать новый список, отсортированный
    по дате (date)."""
    return sorted(dict_list, key=lambda x: x['date'], reverse=sort_rules)
