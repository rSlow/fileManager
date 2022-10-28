from tkinter import Tk, constants as c
from tkinter.messagebox import showwarning

from UI.components.button import Button
from UI.sections.central import CentralSection
from UI.sections.side import SideSection
from configfile import Config
from utils.filemanager import FileManager
from utils.messageboxes import with_confirm


class App(Tk):
    def __init__(self, *args, **kwargs):
        super(App, self).__init__(*args, **kwargs)

        self.protocol("WM_DELETE_WINDOW", self.on_close)
        self.title("File Manager")
        self.resizable(False, False)

        self.configuration = Config.load()
        self.filemanager = FileManager(app=self)

        self.left_section = SideSection(
            master=self,
            parent=self,
            side=c.LEFT,
            header_text="Флешка",
            initial_dir=self.configuration.left_dir
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
            initial_dir=self.configuration.right_dir
        )

        self.scan_button = Button(
            master=self,
            text="Сканировать",
            command=self.watch_files
        )
        self.update_button = Button(
            master=self,
            text="Синхронизировать с заменой старых файлов на новые",
            command=self.synchronize
        )

        self.pack_sections()

    @with_confirm(message="Синхронизировать файлы?")
    def synchronize(self):
        self.left_section.add_all_with_replacing_old()
        self.right_section.add_all_with_replacing_old()
        self.watch_files()

    def pack_sections(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.left_section.grid(row=0, column=0, sticky=c.EW)
        self.central_section.grid(row=0, column=1, sticky=c.NSEW)
        self.right_section.grid(row=0, column=2, sticky=c.EW)

        self.scan_button.grid(row=1, column=0, columnspan=3, sticky=c.EW, pady=2, padx=5)
        self.update_button.grid(row=2, column=0, columnspan=3, sticky=c.EW, pady=2, padx=5)

    def watch_files(self):
        if self.left_section.get_dir() and self.right_section.get_dir():
            self.left_section.unselect_all()
            self.central_section.unselect_all()
            self.right_section.unselect_all()

            self.filemanager.scan_files()

            left_sections_files = self.filemanager.left_section_files
            central_section_files = self.filemanager.central_section_files
            right_section_files = self.filemanager.right_section_files

            self.left_section.place_new_files(left_sections_files)
            self.central_section.place_new_files(central_section_files)
            self.right_section.place_new_files(right_section_files)

        else:
            showwarning(
                title="Предупреждение",
                message="Требуется выбрать обе директории!"
            )

    def set_configuration(self):
        if left_dir := self.left_section.get_dir():
            self.configuration.left_dir = left_dir
        if right_dir := self.right_section.get_dir():
            self.configuration.right_dir = right_dir

        self.configuration.save()

    def on_close(self):
        self.set_configuration()
        self.destroy()


root = App()
