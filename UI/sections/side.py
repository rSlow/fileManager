import glob
import os.path
from tkinter import constants

from ..components.buttons_side_block import SideButtonsBlock
from ..components.side_files_field import FileField
from ..components.filestring import FileStringBlock
from .base import BaseSection


class SideSection(BaseSection):
    def __init__(self, master, header_text: str):
        super(SideSection, self).__init__(
            master=master,
            header_text=header_text
        )

        self.file_string = FileStringBlock(master=self)
        self.file_field = FileField(master=self)
        self.bottom_buttons = SideButtonsBlock(master=self)

        self.pack_elements()

    def pack_elements(self):
        self.file_string.pack(fill=constants.X)
        self.file_field.pack(fill=constants.BOTH, expand=True)
        self.bottom_buttons.pack(fill=constants.X)

    def get_files_list(self):
        files_list = []
        current_directory = self.file_string.get_directory()
        if current_directory:
            for path in glob.glob(f"{current_directory}/**", recursive=True):
                if os.path.isfile(path):
                    files_list.append(path)
        print(files_list)