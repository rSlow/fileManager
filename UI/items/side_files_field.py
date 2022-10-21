from tkinter import Listbox, Frame, Scrollbar
from tkinter import constants as c

from utils.file import File


class FileField(Frame):
    def __init__(self, master, width: int = 50, height: int = 30):
        super(FileField, self).__init__(
            master=master,
            bg="white",
        )
        self.scrollbar_x = Scrollbar(
            master=self,
            orient=c.HORIZONTAL,
        )
        self.scrollbar_y = Scrollbar(master=self, orient=c.VERTICAL)
        self.listbox = Listbox(
            master=self,
            width=width,
            height=height,
            xscrollcommand=self.scrollbar_x.set,
            yscrollcommand=self.scrollbar_y.set,
            selectmode=c.MULTIPLE,
            selectbackground="#cccccc"
        )
        self.listbox.bind("<<ListboxSelect>>", self.update_frame)

        self.scrollbar_x.config(command=self.listbox.xview)
        self.scrollbar_y.config(command=self.listbox.yview)

        self.scrollbar_y.pack(fill=c.Y, side=c.RIGHT)
        self.scrollbar_x.pack(fill=c.X, side=c.BOTTOM)
        self.listbox.pack(fill=c.BOTH, expand=False)

    def update_frame(self, event=None):
        if event:
            selection = event.widget.curselection()
        else:
            selection = self.listbox.curselection()
        self.master.selected_label.set_value(len(selection))

    def watch_files(self, files: list[File]):
        self.clear()

        for file in files:
            self.append_file(file)

    def get_selected(self) -> tuple[int]:
        return self.listbox.curselection()

    def append_file(self, file: File):
        self.listbox.insert(c.END, file)

    def clear(self):
        self.listbox.delete(0, c.END)

    def select_all(self):
        self.listbox.selection_set(0, c.END)
        self.update_frame()

    def unselect_all(self):
        self.listbox.selection_clear(0, c.END)
        self.update_frame()
