import glob
import os.path
from tkinter import constants

from ..components.button import Button
from ..items.buttons_side_block import SideButtonsBlock
from utils.file import File
from ..components.selected_label import SelectedLabel
from ..items.side_files_field import FileField
from ..items.filestring import FileStringBlock
from .base import BaseSection


class SideSection(BaseSection):
    def __init__(self, master, header_text: str):
        super(SideSection, self).__init__(
            master=master,
            header_text=header_text
        )

        self.file_string = FileStringBlock(master=self)
        self.file_field = FileField(master=self)
        self.selected_label = SelectedLabel(master=self)
        self.bottom_buttons = SideButtonsBlock(master=self, parent=self)

        self._scan_button = Button(
            master=self,
            text="Сканировать",
            command=lambda: self.watch_files()
        )

        self.pack_elements()

    def get_all_files(self):
        files = []
        directory = self.file_string.get_directory()
        if os.path.isdir(directory):
            directory_pattern = os.path.join(directory, "**")
            for path in glob.glob(directory_pattern, recursive=True):
                if os.path.isfile(path):
                    files.append(File(base_dir=directory, path=path))
        return files

    def pack_elements(self):
        self.file_string.pack(fill=constants.X)
        self.file_field.pack(fill=constants.BOTH, expand=True)
        self.selected_label.pack(fill=constants.X)
        self.bottom_buttons.pack(fill=constants.X)
        self._scan_button.pack(fill=constants.X)

    def watch_files(self):
        files = self.get_all_files()
        self.file_field.watch_files(files)
