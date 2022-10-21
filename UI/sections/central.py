import tkinter as tk
from tkinter import constants as c

from UI.sections.base import BaseSection
from utils.file import File
from utils.filemanager import CentralFileSection


class ModifyListBox(tk.Listbox):
    def append_file(self, file: File):
        self.insert(c.END, file)

    def clear(self):
        self.delete(0, c.END)


class CentralSection(BaseSection):
    def __init__(self, master, parent,
                 header_text: str,
                 width: int = 35,
                 height: int = 33
                 ):
        super(CentralSection, self).__init__(
            master=master,
            header_text=header_text,
            parent=parent
        )

        self.scrollbar_y = tk.Scrollbar(self, orient=c.VERTICAL)
        self.scrollbar_x = tk.Scrollbar(self, orient=c.HORIZONTAL)

        self.left_list = ModifyListBox(
            master=self,
            yscrollcommand=self._scroll_left_y,
            xscrollcommand=self._scroll_left_x,
            selectmode=c.MULTIPLE,
            height=height,
            width=width
        )
        self.right_list = ModifyListBox(
            master=self,
            yscrollcommand=self._scroll_right_y,
            xscrollcommand=self._scroll_right_x,
            selectmode=c.MULTIPLE,
            height=height,
            width=width
        )

        self.scrollbar_y.config(command=self._lists_yview)
        self.scrollbar_x.config(command=self._lists_xview)

        self.grid_elements()

    # Y-view
    def _scroll_left_y(self, start, end):
        if self.right_list.yview() != self.left_list.yview():
            self.right_list.yview_moveto(start)
        self.scrollbar_y.set(start, end)

    def _scroll_right_y(self, start, end):
        if self.left_list.yview() != self.right_list.yview():
            self.left_list.yview_moveto(start)
        self.scrollbar_y.set(start, end)

    def _lists_yview(self, *args):
        self.left_list.yview(*args)
        self.right_list.yview(*args)

    # X-view
    def _scroll_left_x(self, start, end):
        if self.right_list.xview() != self.left_list.xview():
            self.right_list.xview_moveto(start)
        self.scrollbar_x.set(start, end)

    def _scroll_right_x(self, start, end):
        if self.left_list.xview() != self.right_list.xview():
            self.left_list.xview_moveto(start)
        self.scrollbar_x.set(start, end)

    def _lists_xview(self, *args):
        self.left_list.xview(*args)
        self.right_list.xview(*args)

    def grid_elements(self):
        self.left_list.grid(row=1, column=0, sticky=c.NSEW)
        self.right_list.grid(row=1, column=1, sticky=c.NSEW)
        self.scrollbar_y.grid(row=1, column=2, sticky=c.NS)
        self.scrollbar_x.grid(row=2, column=0, sticky=c.EW, columnspan=3)

    def place_new_files(self, section_files: CentralFileSection):
        self.left_list.clear()
        self.right_list.clear()

        for file in section_files.left_side:
            self.left_list.append_file(file)
        for file in section_files.right_side:
            self.right_list.append_file(file)
