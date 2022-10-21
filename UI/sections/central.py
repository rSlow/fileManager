import tkinter as tk
from tkinter import constants as c, font as _font

from ..components.selected_label import SelectedLabel
from ..items.central_buttons_block import CentralButtonsBlock
from ..sections.base import BaseSection
from utils.file import File
from utils.filemanager import CentralFileSection


class ModifiedListBox(tk.Listbox):
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

        self.left_listbox = ModifiedListBox(
            master=self,
            yscrollcommand=self._scroll_left_y,
            xscrollcommand=self._scroll_left_x,
            selectmode=c.MULTIPLE,
            height=height,
            width=width
        )
        self.right_listbox = ModifiedListBox(
            master=self,
            yscrollcommand=self._scroll_right_y,
            xscrollcommand=self._scroll_right_x,
            selectmode=c.MULTIPLE,
            height=height,
            width=width
        )

        self.left_selected_label = SelectedLabel(
            master=self,
            font=_font.Font(size=10)
        )
        self.right_selected_label = SelectedLabel(
            master=self,
            font=_font.Font(size=10)
        )

        self.buttons_block = CentralButtonsBlock(
            master=self,
            parent=self,
            left_listbox=self.left_listbox,
            right_listbox=self.right_listbox
        )

        self._config_scrollbars()
        self.grid_elements()

    def _config_scrollbars(self):
        self.scrollbar_y.config(command=self._lists_yview)
        self.scrollbar_x.config(command=self._lists_xview)

    # Y-view
    def _scroll_left_y(self, start, end):
        if self.right_listbox.yview() != self.left_listbox.yview():
            self.right_listbox.yview_moveto(start)
        self.scrollbar_y.set(start, end)

    def _scroll_right_y(self, start, end):
        if self.left_listbox.yview() != self.right_listbox.yview():
            self.left_listbox.yview_moveto(start)
        self.scrollbar_y.set(start, end)

    def _lists_yview(self, *args):
        self.left_listbox.yview(*args)
        self.right_listbox.yview(*args)

    # X-view
    def _scroll_left_x(self, start, end):
        if self.right_listbox.xview() != self.left_listbox.xview():
            self.right_listbox.xview_moveto(start)
        self.scrollbar_x.set(start, end)

    def _scroll_right_x(self, start, end):
        if self.left_listbox.xview() != self.right_listbox.xview():
            self.left_listbox.xview_moveto(start)
        self.scrollbar_x.set(start, end)

    def _lists_xview(self, *args):
        self.left_listbox.xview(*args)
        self.right_listbox.xview(*args)

    def grid_elements(self):
        self.left_listbox.grid(row=1, column=0, sticky=c.NSEW)
        self.right_listbox.grid(row=1, column=1, sticky=c.NSEW)
        self.scrollbar_y.grid(row=1, column=2, sticky=c.NS)
        self.scrollbar_x.grid(row=2, column=0, sticky=c.EW, columnspan=3)
        self.left_selected_label.grid(row=3, column=0, sticky=c.NSEW)
        self.right_selected_label.grid(row=3, column=1, sticky=c.NSEW)
        self.buttons_block.grid(row=4, column=0, sticky=c.NSEW, columnspan=3)

    def place_new_files(self, section_files: CentralFileSection):
        self.left_listbox.clear()
        self.right_listbox.clear()

        for file in section_files.left_side:
            self.left_listbox.append_file(file)
        for file in section_files.right_side:
            self.right_listbox.append_file(file)
