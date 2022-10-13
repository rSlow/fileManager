from tkinter import Tk

from UI.sections.central import CentralSection
from UI.sections.side import SideSection


class App(Tk):
    def __init__(self, *args, **kwargs):
        super(App, self).__init__(*args, **kwargs)
        self.title("File Manager")
        self.resizable(False, False)

        self.columnconfigure(index=0, weight=1)
        self.columnconfigure(index=1, weight=1)
        SideSection(master=self, header_text="Флешка").pack()
        CentralSection(master=self, header_text="Конфликты").pack()
        SideSection(master=self, header_text="Компьютер").pack()


root = App()
