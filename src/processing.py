import math


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

def calculate_logariphm(x, base):
    return math.log(x, base)


def reverse_string(my_string):
    return my_string[::-1]

if __name__ == '__main__':
    data = [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]
    print(filter_by_state(data, 'CANCELED'))
    print(sort_by_date(data))


