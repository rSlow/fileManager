from tkinter import ttk
from typing import Iterable


class ButtonsRow(ttk.Frame):
    def __init__(self, buttons: Iterable[ttk.Button], **kwargs):
        super(ButtonsRow, self).__init__(**kwargs)
        self.buttons = [*buttons]

    def pack(self):
        for button in self.buttons:
            button.pack(

            )
