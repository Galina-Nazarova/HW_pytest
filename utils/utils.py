import json


def get_transactions_data (data_path:str)-> list[dict]:
    """Функция, которая принимает на вход путь до JSON-файла и возвращает список
    словарей с данными о финансовых транзакциях. Если файл пустой, содержит не
    список или не найден, функция возвращает пустой список. Функцию поместите в модуль
    utils. Файл с данными о финансовых транзациях data/operations.json
    """
    try:
        with open(data_path, encoding='utf-8') as operation_file:
            try:
                transactions_data = json.load(operation_file)
                return(transactions_data)
            except json.JSONDecodeError:
                print("Ошибка декодирования файла")
                return False
    except FileNotFoundError:
        print("Файл не найден")
        return False



if __name__ == '__main__':
    pass