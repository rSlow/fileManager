from tkinter import ttk, constants
from typing import Sequence, Literal

from UI.components.button import Button


class SideButtonsBlock(ttk.Frame):
    # def __init__(self,
    #              *args,
    #              orient: Literal["left", "right", "top", "bottom"],
    #              buttons: list[ttk.Button] | None = None,
    #              **kwargs):
    #     super(ButtonsBlock, self).__init__(*args, **kwargs)
    #
    #     for button in buttons:
    #         button.pack(side=orient)
    def __init__(self, master):
        super(SideButtonsBlock, self).__init__(master=master)

        first_row = ttk.Frame(master=self)
        Button(master=first_row, text="Добавить все").pack()
        Button(master=first_row, text="Добавить выбранные").pack()
        Button(master=first_row, text="Выбрать все").pack()

        first_row.pack()
        # buttons_row.pack(fill=constants.X)
        #
        Button(master=self, text="Синхронизировать с приоритетом").pack(
            side=constants.TOP
        )
