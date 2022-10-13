from tkinter import constants

from UI.components.files_field import FileField
from UI.sections.base import BaseSection


class CentralSection(BaseSection):
    def __init__(self, master, header_text: str):
        super(CentralSection, self).__init__(
            master=master,
            header_text=header_text
        )
        self.pack_file_field()

    def pack_file_field(self):
        file_field = FileField(
            master=self
        )
        file_field.pack(fill=constants.X)
