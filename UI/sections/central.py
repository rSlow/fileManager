import tkinter as tk
from tkinter import constants as c

from ..components.selected_label import SelectedLabel
from ..items.central_buttons_block import CentralButtonsBlock
from ..sections.base import BaseSection
from utils.filemanager import CentralFileSection


class ModifiedListBox(tk.Listbox):
    NEW = "[NEW]"

    def __init__(self, selected_label, side, **kwargs):
        super(ModifiedListBox, self).__init__(**kwargs)
        self.selected_label = selected_label
        self.side = side
        self.bind("<<ListboxSelect>>", self.update_label_value)

    def append_file_alias(self, filename_alias: str):
        self.insert(c.END, filename_alias)

    def clear(self):
        self.delete(0, c.END)

    def unselect_all(self):
        self.selection_clear(0, c.END)
        self.update_label_value()

    def update_label_value(self, event=None):
        if event:
            selection = event.widget.curselection()
        else:
            selection = self.curselection()
        self.selected_label.set_value(len(selection))

    def get_all_filenames(self) -> list[str]:
        return self.get(0, c.END)

    @property
    def filemanager_central_section(self):
        app = self.master.master.master
        if hasattr(app, "filemanager"):
            return app.filemanager

    def copy_files(self, indexes: list[int] | tuple[int]):
        self.filemanager_central_section.copy_selected_to_side(
            indexes=indexes,
            to_side=self.side
        )

    def copy_selected(self):
        selected_indexes = self.curselection()
        self.copy_files(selected_indexes)

    def copy_all(self):
        self.copy_files([*range(self.size())])

    def copy_old_files(self):
        files = self.get_all_filenames()
        old_file_indexes_list = []
        for index, filename in enumerate(files):
            if not filename.startswith(self.NEW):
                old_file_indexes_list.append(index)
        self.copy_files(old_file_indexes_list)

    def copy_new_files(self):
        files = self.get_all_filenames()
        new_file_indexes_list = []
        for index, filename in enumerate(files):
            if filename.startswith(self.NEW):
                new_file_indexes_list.append(index)
        self.copy_files(new_file_indexes_list)


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

        self.left_selected_label = SelectedLabel(
            master=self,
            font_size=10
        )
        self.right_selected_label = SelectedLabel(
            master=self,
            font_size=10
        )

        self.left_listbox = ModifiedListBox(
            master=self,
            selected_label=self.left_selected_label,
            xscrollcommand=self._scroll_left_x,
            yscrollcommand=self._scroll_left_y,
            selectmode=c.MULTIPLE,
            height=height,
            width=width,
            side=c.LEFT
        )
        self.right_listbox = ModifiedListBox(
            master=self,
            selected_label=self.right_selected_label,
            xscrollcommand=self._scroll_right_x,
            yscrollcommand=self._scroll_right_y,
            selectmode=c.MULTIPLE,
            height=height,
            width=width,
            side=c.RIGHT
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

    def append_left_file_alias(self, file_alias: str):
        self.left_listbox.append_file_alias(file_alias)

    def append_right_file_alias(self, file_alias: str):
        self.right_listbox.append_file_alias(file_alias)

    def update_label_values(self):
        self.left_listbox.update_label_value()
        self.right_listbox.update_label_value()

    def _grid_elements(self):
        self.left_listbox.grid(row=1, column=0, sticky=c.NSEW)
        self.right_listbox.grid(row=1, column=1, sticky=c.NSEW)
        self.scrollbar_y.grid(row=1, column=2, sticky=c.NS)
        self.scrollbar_x.grid(row=2, column=0, sticky=c.EW, columnspan=3)
        self.left_selected_label.grid(row=3, column=0, sticky=c.NSEW)
        self.right_selected_label.grid(row=3, column=1, sticky=c.NSEW)

    def unselect_all(self):
        self.left_listbox.unselect_all()
        self.right_listbox.unselect_all()


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

    def unselect_all(self):
        self.file_frame.unselect_all()

    def place_new_files(self, section_files: CentralFileSection):
        self.file_frame.clear()

        for left_file, right_file in zip(
                section_files.left_side,
                section_files.right_side
        ):
            if left_file.edit_date > right_file.edit_date:
                self.file_frame.append_left_file_alias(left_file.as_center_new)
                self.file_frame.append_right_file_alias(right_file.as_center_old)

            elif left_file.edit_date < right_file.edit_date:
                self.file_frame.append_left_file_alias(left_file.as_center_old)
                self.file_frame.append_right_file_alias(right_file.as_center_new)
