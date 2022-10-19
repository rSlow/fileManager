from tkinter import ttk, constants as c
from typing import Sequence, Literal

from UI.components.button import Button


class SideButtonsBlock(ttk.Frame):
    pad = 1

    def __init__(self, master):
        super(SideButtonsBlock, self).__init__(master=master)

        self.configure_grid()
        self.grid_buttons()

    def configure_grid(self):
        self.grid_columnconfigure(
            index=0,
            weight=1,
        )
        self.grid_columnconfigure(
            index=1,
            weight=1
        )

    def grid_buttons(self):
        select_all_button = Button(
            master=self,
            text="Выбрать все",
        )
        clear_selection_button = Button(
            master=self,
            text="Снять выделение"
        )
        add_selected_button = Button(
            master=self,
            text="Добавить выбранные"
        )
        add_missing_button = Button(
            master=self,
            text="Добавить только отсутствующие"
        )
        add_replacing_exiting_button = Button(
            master=self,
            text="Добавить все, заменяя все конфликтные"
        )
        add_replacing_older_button = Button(
            master=self,
            text="Добавить все, заменяя старые конфликтные"
        )

        select_all_button.grid(row=0, column=0, sticky=c.EW, padx=self.pad, pady=self.pad)
        clear_selection_button.grid(row=0, column=1, sticky=c.EW, padx=self.pad, pady=self.pad)
        add_selected_button.grid(row=1, column=0, sticky=c.EW, padx=self.pad, pady=self.pad)
        add_missing_button.grid(row=1, column=1, sticky=c.EW, padx=self.pad, pady=self.pad)
        add_replacing_exiting_button.grid(row=2, column=0, sticky=c.EW, padx=self.pad, pady=self.pad, columnspan=2)
        add_replacing_older_button.grid(row=3, column=0, sticky=c.EW, padx=self.pad, pady=self.pad, columnspan=2)

    def pack_second_row(self):
        second_row = ttk.Frame(master=self)

        select_all_button = Button(
            master=second_row,
            text="Выбрать все",
            command=self.master.file_field.select_all
        )
        unselect_all_button = Button(
            master=self,
            text="Снять все выделения",
            command=self.master.file_field.unselect_all
        )

        select_all_button.pack(side=c.LEFT)
        unselect_all_button.pack(side=c.RIGHT)
        second_row.pack(fill=c.BOTH, expand=True)

    def pack_bottom_button(self):
        Button(
            master=self,
            text="Синхронизировать с приоритетом",
            command=self.master.get_files_list
        ).pack(
            side=c.BOTTOM,
        )
