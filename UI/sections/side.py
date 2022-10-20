from tkinter import constants

from utils.filemanager import SideFileSection
from ..items.buttons_side_block import SideButtonsBlock
from ..components.selected_label import SelectedLabel
from ..items.side_files_field import FileField
from ..items.filestring import FileStringBlock
from .base import BaseSection


class SideSection(BaseSection):
    def __init__(self, master, header_text: str, initial_dir: str | None = None):
        super(SideSection, self).__init__(
            master=master,
            header_text=header_text
        )

        self.file_string = FileStringBlock(master=self, initial_dir=initial_dir)
        self.file_field = FileField(master=self)
        self.selected_label = SelectedLabel(master=self)
        self.bottom_buttons = SideButtonsBlock(master=self, parent=self)

        self.pack_elements()

    def pack_elements(self):
        self.file_string.pack(fill=constants.X)
        self.file_field.pack(fill=constants.BOTH, expand=True)
        self.selected_label.pack(fill=constants.X)
        self.bottom_buttons.pack(fill=constants.X)

    def get_dir(self):
        return self.file_string.get_directory()

    def place_new_files(self, file_section: SideFileSection):
        self.file_field.clear()
        for file in file_section:
            self.file_field.append_file(file)
