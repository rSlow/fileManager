from functools import wraps
from tkinter.messagebox import askokcancel, showerror, showinfo

from UI.exceptions import NotScannedError


def not_scanned_error():
    showerror(
        title="Ошибка",
        message="Сначала необходимо просканировать!"
    )


def copy_error(message: str):
    showerror(
        title="Ошибка копирования",
        message=f"{message}"
    )


def sync_not_needed():
    showinfo(
        title="Сообщение",
        message="Все файлы синхронизированы!"
    )


def with_confirm(message: str, title: str = None):
    if title is None:
        title = "Подтверждение"

    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            if askokcancel(title=title, message=message):
                try:
                    return func(*args, **kwargs)
                except NotScannedError:
                    not_scanned_error()

        return inner

    return wrapper
