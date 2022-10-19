from tkinter import Tk, constants as c
from tkinter.ttk import Separator

from UI.sections.central import CentralSection
from UI.sections.side import SideSection


class App(Tk):
    def __init__(self, *args, **kwargs):
        super(App, self).__init__(*args, **kwargs)
        self.title("File Manager")
        # self.resizable(False, False)

        # self.columnconfigure(index=0, weight=1)
        # self.columnconfigure(index=1, weight=1)

        self.left_section = SideSection(master=self, header_text="Флешка")
        # self.central_section = CentralSection(master=self, header_text="Конфликты")
        self.right_section = SideSection(master=self, header_text="Компьютер")

        self.pack_sections()

    def pack_sections(self):
        self.left_section.pack()
        # self.central_section.pack()
        self.right_section.pack()


root = App()
