from tkinter import constants as c, ttk

from ..components.section_header import SectionHeader


class BaseSection(ttk.Frame):
    def __init__(self, master, parent, header_text: str):
        super(BaseSection, self).__init__(
            master=master,
            padding=5
        )

        self.grid_header(header_text=header_text)
        self.parent = parent

    def grid_header(self, header_text):
        header_block = SectionHeader(
            master=self,
            text=header_text,
        )
        header_block.grid(
            row=0, column=0,
            sticky=c.EW,
        )
