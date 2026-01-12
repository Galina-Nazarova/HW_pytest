import functools
from time import time


def log(filename=False):
    """
    Декоратор, который создает файл и записывает результат
    декорируемой функции в него
    """

    def logging(function):
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            time_1 = time()
            result = function(*args, **kwargs)
            time_2 = time()
            if not filename:
                print(
                    f'{function.__name__}: {result}. Inputs:{args}, {kwargs}'
                )
            else:
                with open(filename, 'w', encoding='utf-8') as file:
                    file.write(
                        f'{function.__name__}: {result}. Inputs:{args}, {kwargs}'
                    )
            return result

        return wrapper

    return logging
