import functools
import time
import logging

def log(log_filename=False):
    def logs(function):
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            if log_filename:
                logging.basicConfig(filename=log_filename, level=logging.INFO,
                                    format='%(asctime)s - %(levelname)s - %(message)s')
            else:
                logging.basicConfig(level=logging.INFO,
                                    format='%(asctime)s - %(levelname)s - %(message)s')
            try:
                result = function(*args, **kwargs)
                logging.info(f"{function.__name__}: {result}. Inputs:{args}, {kwargs}")
                return result
            except Exception as e:
                logging.error(f"{function.__name__}: {e}. Inputs:{args}, {kwargs}", exc_info=True)
                raise # Перебрасываем исключение
        return wrapper
    return logs
