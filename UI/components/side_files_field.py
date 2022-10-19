import glob
import os.path
from tkinter import Listbox, Frame, Scrollbar
from tkinter import constants as c

from UI.components.file import File


class FileField(Frame):
    def __init__(self, master):
        super(FileField, self).__init__(
            master=master,
            bg="white",
        )
        self.scrollbar_x = Scrollbar(
            master=self,
            orient=c.HORIZONTAL,
        )
        self.scrollbar_y = Scrollbar(master=self, orient=c.VERTICAL)
        self.listbox = Listbox(
            master=self,
            height=30,
            width=80,
            xscrollcommand=self.scrollbar_x.set,
            yscrollcommand=self.scrollbar_y.set,
            selectmode=c.MULTIPLE,
            selectbackground="#cccccc"
        )

        self.scrollbar_x.config(command=self.listbox.xview)
        self.scrollbar_y.config(command=self.listbox.yview)

        self.scrollbar_y.pack(fill=c.Y, side=c.RIGHT)
        self.scrollbar_x.pack(fill=c.X, side=c.BOTTOM)
        self.listbox.pack(fill=c.BOTH, expand=False)

        directory = "/home/rslow/Рабочий стол/работа/"
        for path in glob.glob(f"{directory}/**", recursive=True):
            if not os.path.isdir(path):
                self.listbox.insert(c.END, path[len(directory):])

    def add_file(self, file: File):
        self.listbox.insert(c.END, file)

    def select_all(self):
        self.listbox.selection_set(0, c.END)

    def unselect_all(self):
        self.listbox.selection_clear(0, c.END)
