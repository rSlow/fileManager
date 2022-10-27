from tkinter import ttk, constants as c

from ..components.button import Button


class CentralButtonsBlockColumn(ttk.Frame):
    def __init__(self, master, listbox, **kwargs):
        super(CentralButtonsBlockColumn, self).__init__(master, **kwargs)
        self.listbox = listbox

        self.replace_to_new_button = Button(
            master=self,
            text="Заменить все старые",
            command=self.listbox.get_old_file_indexes
        )
        self.replace_to_old_button = Button(
            master=self,
            text="Заменить все новые",
            command=self.listbox.get_new_file_indexes
        )
        self.replace_all_button = Button(
            master=self,
            text="Заменить все",
            command=...
        )
        self.replace_selected_button = Button(
            master=self,
            text="Заменить выбранные",
            command=...
        )

        self._grid_buttons()

    def _grid_buttons(self):
        self.grid_columnconfigure(0, weight=1)

        self.replace_to_new_button.grid(row=0, column=0,
                                        sticky=c.NSEW,
                                        padx=1, pady=1)
        self.replace_to_old_button.grid(row=1, column=0,
                                        sticky=c.NSEW,
                                        padx=1, pady=1)
        self.replace_all_button.grid(row=2, column=0,
                                     sticky=c.NSEW,
                                     padx=1, pady=1)
        self.replace_selected_button.grid(row=3, column=0,
                                          sticky=c.NSEW,
                                          padx=1, pady=1)


class CentralButtonsBlock(ttk.Frame):
    def __init__(self, master, parent,
                 left_listbox, right_listbox,
                 **kwargs):
        super(CentralButtonsBlock, self).__init__(master, relief=c.RIDGE, **kwargs)
        self.parent = parent

        self.left_listbox = left_listbox
        self.right_listbox = right_listbox

        self.left_column = CentralButtonsBlockColumn(
            master=self,
            listbox=self.left_listbox
        )
        self.right_column = CentralButtonsBlockColumn(
            master=self,
            listbox=self.right_listbox
        )

        self._grid_columns()

    def _grid_columns(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.left_column.grid(row=0, column=0, sticky=c.NSEW)
        self.right_column.grid(row=0, column=1, sticky=c.NSEW)
