from functools import wraps
from typing import Any, Callable


def log(filename: str | None = "") -> Callable:
    """
    Декоратор для логирования вызовов функции.
    Параметры:  filename (str | None): Путь к файлу для логов. Если не указан, лог выводится в консоль.
    Возвращает: Callable: Обёрнутая функция с логированием.
    """

    def wrapper(func: Callable) -> Callable:
        @wraps(func)
        def inner(*args: Any, **kwargs: Any) -> Any:
            try:
                message_ok = f"{func.__name__} ok"
                result = func(*args, **kwargs)
                if filename:
                    with open(filename, "w") as file:
                        file.write(f"{message_ok}\n")
                else:
                    print(f"{message_ok}")
                return result
            except Exception as e:
                message_err = f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}"
                if filename:
                    with open(filename, "w") as file:
                        file.write(f"{message_err}\n")
                else:
                    print(f"{message_err}")

        return inner

    return wrapper


print(help(log))
