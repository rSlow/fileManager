from tkinter import ttk, font as _font


class SelectedLabel(ttk.Label):
    def __init__(self, *args, font=None, **kwargs):
        super(SelectedLabel, self).__init__(
            *args,
            font=font or _font.Font(size=12),
            **kwargs
        )
        self.value = 0
        self._update()

    def set_value(self, value: int):
        self.value = value
        self._update()

    def _update(self):
        self.configure(
            text=f"Выбрано элементов: {self.value}"
        )
