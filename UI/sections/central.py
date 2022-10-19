from tkinter import constants, ttk

from ..items.side_files_field import FileField
from UI.sections.base import BaseSection


class CentralSection(BaseSection):
    def __init__(self, master, header_text: str):
        super(CentralSection, self).__init__(
            master=master,
            header_text=header_text
        )
        self.pack_file_field()
        ttk.Label(width=70, master=self).pack()

    def pack_file_field(self):
        file_field = FileField(
            master=self,
        )
        file_field.pack(fill=constants.X)
