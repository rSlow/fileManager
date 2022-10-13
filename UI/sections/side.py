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
        self.file_field.pack(fill=constants.X)
        self.bottom_buttons.pack(fill=constants.X)
