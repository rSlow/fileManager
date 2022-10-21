from tkinter import constants as c, font as _font

from utils.confirm_decorator import with_confirm
from utils.filemanager import SideFileSection
from ..items.side_buttons_block import SideButtonsBlock
from ..components.selected_label import SelectedLabel
from ..items.side_files_field import FileField
from ..items.filestring import FileStringBlock
from .base import BaseSection
from tkinter.messagebox import showerror


class SideSection(BaseSection):
    def __init__(self, master, parent, side, header_text: str, initial_dir: str | None = None):
        super(SideSection, self).__init__(
            master=master,
            header_text=header_text,
            parent=parent
        )
        self.side = side

        self.file_string = FileStringBlock(master=self, initial_dir=initial_dir)
        self.file_field = FileField(master=self)
        self.selected_label = SelectedLabel(master=self, font=_font.Font(size=12))
        self.bottom_buttons = SideButtonsBlock(master=self, parent=self)

        self.pack_elements()

    def pack_elements(self):
        """start from row=1"""
        self.grid_columnconfigure(0, weight=1)

        self.file_string.grid(row=1, column=0, sticky=c.EW)
        self.file_field.grid(row=2, column=0, sticky=c.EW)
        self.selected_label.grid(row=3, column=0, sticky=c.EW)
        self.bottom_buttons.grid(row=4, column=0, sticky=c.EW)

    def get_dir(self):
        return self.file_string.get_directory()

    def place_new_files(self, file_section: SideFileSection):
        self.file_field.clear()
        for file in file_section:
            self.file_field.append_file(file)

    @with_confirm(message="Добавляем все отсутствующие файлы?")
    def add_all_missing(self):
        self.select_all()
        self.add_selected()

    def select_all(self):
        self.file_field.select_all()

    def unselect_all(self):
        self.file_field.unselect_all()

    @with_confirm(message="Добавляем выбранные элементы?")
    def add_selected(self):
        selected_fields = self.file_field.get_selected()
        filemanager = self.parent.filemanager
        match self.side:
            case c.LEFT:
                section_files = filemanager.left_section_files
            case c.RIGHT:
                section_files = filemanager.right_section_files
            case _:
                raise AttributeError(f"section type is not {c.LEFT} or {c.RIGHT}")

        try:
            section_files.copy_selected(selected_fields)
        except Exception as ex:
            showerror(
                title="Ошибка копирования",
                message=f"{ex.args}"
            )
        finally:
            self.parent.watch_files()
            self.selected_label.set_value(0)
