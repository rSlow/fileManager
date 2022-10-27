from tkinter import ttk, font as _font


class SelectedLabel(ttk.Label):
    def __init__(self, *args, font_size, **kwargs):
        super(SelectedLabel, self).__init__(
            *args,
            font=_font.Font(size=font_size),
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
