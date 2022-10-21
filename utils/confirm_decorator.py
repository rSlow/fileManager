from functools import wraps
from tkinter.messagebox import askokcancel


def with_confirm(message, title=None):
    if title is None:
        title = "Подтверждение"

    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            if askokcancel(title=title, message=message):
                return func(*args, **kwargs)

        return inner

    return wrapper
