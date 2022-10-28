from tkinter import ttk, constants as c

from UI.components.button import Button
from utils.messageboxes import with_confirm


class SideButtonsBlock(ttk.Frame):
    pad = 1

    def __init__(self, *args, parent, **kwargs):
        super(SideButtonsBlock, self).__init__(*args, **kwargs)
        self.parent = parent

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
            command=self.parent.select_all
        )
        clear_selection_button = Button(
            master=self,
            text="Снять выделение",
            command=self.parent.unselect_all

        )
        add_selected_button = Button(
            master=self,
            text="Добавить выбранные",
            command=with_confirm(message="Добавляем выбранные элементы?")(self.parent.add_selected)
        )
        add_missing_button = Button(
            master=self,
            text="Добавить все отсутствующие",
            command=with_confirm(message="Добавляем все отсутствующие файлы?")(self.parent.add_all_missing)
        )
        add_replacing_exiting_button = Button(
            master=self,
            text="Добавить все и заменить все конфликтные",
            command=self.parent.add_all_with_replacing_all
        )
        add_replacing_older_button = Button(
            master=self,
            text="Добавить все и заменить старые",
            command=with_confirm(message="Добавляем все отсутствующие файлы и заменяем старые?")(
                self.parent.add_all_with_replacing_old)
        )

        select_all_button.grid(row=0, column=0, sticky=c.EW, padx=self.pad, pady=self.pad)
        clear_selection_button.grid(row=0, column=1, sticky=c.EW, padx=self.pad, pady=self.pad)
        add_selected_button.grid(row=1, column=0, sticky=c.EW, padx=self.pad, pady=self.pad)
        add_missing_button.grid(row=1, column=1, sticky=c.EW, padx=self.pad, pady=self.pad)
        add_replacing_exiting_button.grid(row=2, column=0, sticky=c.EW, padx=self.pad, pady=self.pad, columnspan=2)
        add_replacing_older_button.grid(row=3, column=0, sticky=c.EW, padx=self.pad, pady=self.pad, columnspan=2)
