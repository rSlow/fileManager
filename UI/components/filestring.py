from tkinter import ttk
from tkinter.filedialog import askdirectory
from tkinter import constants
from os import getcwd

__all__ = [
    "FileStringBlock"
]


class SetCurrentDirButton(ttk.Button):
    def __init__(self, master, parent):
        super(SetCurrentDirButton, self).__init__(
            master=master,
            text="Текущая директория",
            command=self.set_current_directory
        )
        self.parent = parent

    def set_current_directory(self):
        self.parent.set_dir_entry_value(getcwd())


class SetDirButton(ttk.Button):
    def __init__(self, master, parent):
        super(SetDirButton, self).__init__(
            master=master,
            text="Выбрать директорию",
            command=self.set_directory
        )
        self.parent = parent

    def set_directory(self):
        initial_dir = self.parent.get_initial_dir()
        path = askdirectory(
            initialdir=initial_dir,
            title="Check work directory:"
        )
        if path or initial_dir:
            self.parent.set_dir_entry_value(
                path or initial_dir
            )


class DirEntry(ttk.Entry):
    def __init__(self, master):
        super(DirEntry, self).__init__(
            master=master,
            # width=50,
            background="white",
        )

    def toggle_state(self):
        if constants.DISABLED in self.state():
            self.config(state=constants.NORMAL)
        else:
            self.config(state=constants.DISABLED)


class FileStringBlock(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super(FileStringBlock, self).__init__(*args, **kwargs)
        self.directory_entry = DirEntry(master=self)
        self.dir_buttons = ttk.Frame(master=self)

        self.grid_dir_label()
        self.grid_buttons()

    def grid_dir_label(self):
        self.directory_entry.pack(fill=constants.X)

    def grid_buttons(self):
        SetDirButton(
            master=self.dir_buttons,
            parent=self
        ).pack(side=constants.LEFT, padx=3, pady=3)

        SetCurrentDirButton(
            master=self.dir_buttons,
            parent=self
        ).pack(side=constants.LEFT, padx=3, pady=3)

        self.dir_buttons.pack()

    def set_dir_entry_value(self, text: str):
        self.directory_entry.delete(first=0, last=constants.END)
        self.directory_entry.insert(
            index=0,
            string=text
        )

    def get_initial_dir(self):
        return self.directory_entry.get()