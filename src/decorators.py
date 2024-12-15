import time
from functools import wraps


def log(filename=None):
    """
    Декоратор, который автоматически логирует начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки
    """
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            try:
                start = time.time()
                result = func(*args, **kwargs)
                end = time.time()
                time_for_work = end - start
                message_for_log = (
                    f"The result of working {func.__name__}: {result}\n" f"Time for working: {time_for_work:.20f}"
                )
                if filename:
                    with open(filename, "w", encoding="utf-8") as file:
                        file.write(message_for_log)
                else:
                    print(message_for_log)

                return result
            except Exception as error:
                error_message = (
                    f'{func.__name__} fell down with the error "{error}".\n'
                    f"The arguments of function was {args}, {kwargs}"
                )
                if filename:
                    with open(filename, "w", encoding="utf-8") as file:
                        file.write(error_message)
                else:
                    print(error_message)
                # raise error

        return inner

    return wrapper


@log(filename="mylog.txt")
def my_function(x: int | float, y: int | float) -> int | float:
    "Функция суммы аргументов х и y"
    return x + y


my_function("190080", 5804654982)
