import functools


def log(filename=None):
    """Декоратор с аргументами для логирования работы функций"""

    def write_messenger(text):
        """Обеспечивает отправку текста лога в целевое назначение"""

        if filename:
            with open(filename, "a", encoding="utf-8") as f:
                f.write(text + "\n")
        else:
            print(text)

    def my_dec(func):
        """Принимает декорируемую функцию и оборачивает её в wrapper"""

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            """Выполняет целевую функцию и фиксирует результат или ошибку"""
            try:
                result = func(*args, **kwargs)
                write_messenger(f"{func.__name__} ok")
                return result
            except Exception as e:
                write_messenger(
                    f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"
                )
                raise e

        return wrapper

    return my_dec

    # @log(filename="mylog.txt")
    # def my_function(x, y):
    # return x / y
