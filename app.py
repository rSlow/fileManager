from tkinter import Tk, constants as c, ttk

from UI.components.button import Button
from UI.sections.central import CentralSection
from UI.sections.side import SideSection
from utils.filemanager import FileManager


class App(Tk):
    def __init__(self, *args, **kwargs):
        super(App, self).__init__(*args, **kwargs)
        self.filename = None

        self.set_filename("File Manager")
        self.filemanager = FileManager(app=self)
        self.resizable(False, False)

        self.left_section = SideSection(
            master=self,
            parent=self,
            side=c.LEFT,
            header_text="Флешка",
            initial_dir="/home/rslow/Рабочий стол/копия"
            # initial_dir="/home/rslow/Рабочий стол/флешка рабочая"
        )
        self.central_section = CentralSection(
            master=self,
            parent=self,
            header_text="Конфликты"
        )
        self.right_section = SideSection(
            master=self,
            parent=self,
            side=c.RIGHT,
            header_text="Компьютер",
            initial_dir="/home/rslow/Рабочий стол/работа"
        )

        self._scan_button = Button(
            master=self,
            text="Сканировать",
            command=lambda: self.watch_files()
        )

        self.pack_sections()

    def pack_sections(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.left_section.grid(row=0, column=0, sticky=c.EW)
        self.central_section.grid(row=0, column=1, sticky=c.NSEW)
        self.right_section.grid(row=0, column=2, sticky=c.EW)

        self._scan_button.grid(row=1, column=0, columnspan=3, sticky=c.EW, pady=5, padx=5)

    def watch_files(self):
        if self.left_section.get_dir() and self.right_section.get_dir():
            self.filemanager.scan_files()

            left_sections_files = self.filemanager.left_section_files
            central_section_files = self.filemanager.central_section_files
            right_section_files = self.filemanager.right_section_files

            self.left_section.place_new_files(left_sections_files)
            self.central_section.place_new_files(central_section_files)
            self.right_section.place_new_files(right_section_files)

        else:
            pass

    def set_filename(self, filename: str):
        self.filename = filename
        self.title(self.filename)


root = App()
