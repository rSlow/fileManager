import tkinter as tk
from tkinter import constants as c, font as _font

from ..components.selected_label import SelectedLabel
from ..items.central_buttons_block import CentralButtonsBlock
from ..sections.base import BaseSection
from utils.file import File
from utils.filemanager import CentralFileSection


class ModifiedListBox(tk.Listbox):
    def append_file(self, file: File):
        self.insert(c.END, file.as_center)

    def clear(self):
        self.delete(0, c.END)


class DoubleListBox(tk.Frame):
    def __init__(self, master, parent,
                 width: int = 35,
                 height: int = 33):
        super(DoubleListBox, self).__init__(
            master=master,
        )
        self.parent = parent

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

        self._config_scrollbars()
        self._grid_elements()

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

    def clear(self):
        self.left_listbox.clear()
        self.right_listbox.clear()

    def append_left_file(self, file: File):
        self.left_listbox.append_file(file)

    def append_right_file(self, file: File):
        self.right_listbox.append_file(file)

    def _grid_elements(self):
        self.left_listbox.grid(row=1, column=0, sticky=c.NSEW)
        self.right_listbox.grid(row=1, column=1, sticky=c.NSEW)
        self.scrollbar_y.grid(row=1, column=2, sticky=c.NS)
        self.scrollbar_x.grid(row=2, column=0, sticky=c.EW, columnspan=3)
        self.left_selected_label.grid(row=3, column=0, sticky=c.NSEW)
        self.right_selected_label.grid(row=3, column=1, sticky=c.NSEW)


class CentralSection(BaseSection):
    def __init__(self, master, parent,
                 header_text: str
                 ):
        super(CentralSection, self).__init__(
            master=master,
            header_text=header_text,
            parent=parent
        )

        self.file_frame = DoubleListBox(
            master=self,
            parent=self
        )
        self.buttons_block = CentralButtonsBlock(
            master=self,
            parent=self,
            left_listbox=self.file_frame.left_listbox,
            right_listbox=self.file_frame.right_listbox
        )

        self._grid_elements()

    def _grid_elements(self):
        self.file_frame.grid(row=1, column=0, sticky=c.NSEW)
        self.buttons_block.grid(row=2, column=0, sticky=c.NSEW, )

    def place_new_files(self, section_files: CentralFileSection):
        self.file_frame.clear()

        for file in section_files.left_side:
            self.file_frame.append_left_file(file)

        for file in section_files.right_side:
            self.file_frame.append_right_file(file)
