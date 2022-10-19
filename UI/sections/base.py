from tkinter import constants, ttk

from ..components.section_header import SectionHeader


class BaseSection(ttk.Frame):
    def __init__(self, master, header_text: str):
        super(BaseSection, self).__init__(
            master=master,
            padding=5
        )
        self.pack_header(header_text=header_text)

    def pack_header(self, header_text):
        header_block = SectionHeader(
            master=self,
            text=header_text,
        )
        header_block.pack(anchor=constants.CENTER)

    def pack(self, side=constants.LEFT):
        super(BaseSection, self).pack(
            fill=constants.X,
            expand=True,
            anchor=constants.N,
            side=side,
        )

    def has_path(self):
        return False
