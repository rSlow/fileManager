from tkinter import constants, ttk

from ..components.files_field import FileField
from ..components.filestring import FileStringBlock
from .base import BaseSection


class SideSection(BaseSection):
    def __init__(self, master, header_text: str):
        super(SideSection, self).__init__(
            master=master,
            header_text=header_text
        )

        self.pack_file_string()
        self.pack_file_field()
        self.pack_bottom_buttons()

    def pack_file_string(self):
        file_string = FileStringBlock(
            master=self
        )
        file_string.pack(fill=constants.X)

    def pack_file_field(self):
        file_field = FileField(
            master=self
        )
        file_field.pack(fill=constants.X)

    def pack_bottom_buttons(self):
        buttons_row = ttk.Frame(master=self)
        ttk.Button(master=buttons_row, text="Добавить все").pack(side=constants.LEFT)
        ttk.Button(master=buttons_row, text="Добавить выбранные").pack(side=constants.LEFT)
        ttk.Button(master=buttons_row, text="Выбрать все").pack(side=constants.LEFT)

        buttons_row.pack(fill=constants.X)

        ttk.Button(master=self, text="Синхронизировать с приоритетом").pack(fill=constants.X)
