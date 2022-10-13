from tkinter import ttk, Frame
from tkinter import constants


class FileField(Frame):
    def __init__(self, master):
        super(FileField, self).__init__(
            master=master,
            height=500,
            borderwidth=1,
            relief=constants.RIDGE,
            bg="white"
        )
