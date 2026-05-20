import functools
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """
    Декоратор, который логирует вызов функции и ее результат.
    Если filename передан, пишет в файл, иначе — в консоль.
    """
    def wrapper(func: Callable) -> Callable:
        @functools.wraps(func)
        def inner(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                log_msg = f"{func.__name__}: {result}. Inputs:{args}, {kwargs}"

                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(log_msg + "\n")
                else:
                    print(log_msg)

                return result
            except Exception as e:
                log_msg = (
                    f"{func.__name__} error: {type(e).__name__}. "
                    f"Inputs: {args}, {kwargs}"
                )
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(log_msg + "\n")
                else:
                    print(log_msg)
                raise e
        return inner
    return wrapper
