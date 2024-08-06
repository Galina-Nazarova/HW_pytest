import pytest
from src.processing import calculate_logariphm, filter_by_state


def test_calculate_logariphm():
    assert calculate_logariphm(8, 2) == 3.0
    assert calculate_logariphm(8, 4) == 1.5


    with pytest.raises(ValueError):
        calculate_logariphm(0, 2)

    with pytest.raises(ValueError):
        calculate_logariphm(8, 0)

#Фикстура. Тестирование фильтрации списка словарей по заданному статусу state
def test_filter_by_state(is_true_state_value):
    data = [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]
    assert filter_by_state(data, 'CANCELED') == is_true_state_value

    # Проверка работы функции при отсутствии словарей с указанным статусом 
    # state  в списке.
    with pytest.raises(AssertionError) as exc_info:
        filter_by_state(data, 'ENTERED')

    # Проверяем, что сообщение об ошибке соответствует ожидаемому
    assert str(exc_info.value) == "Нет словарей с указанным статусом"


#Параметризация тестов для различных возможных значений статуса state
@pytest.mark.parametrize('data, state, expected', [
    ([
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ], 'EXECUTED', [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
        ]
    ),
    ([
         {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
         {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
         {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
         {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
     ], 'CANCELED', [
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
     ]
    ),
]
                         )
def test_filter_by_state_parametrize(data, state, expected):
    assert filter_by_state(data, state) == expected