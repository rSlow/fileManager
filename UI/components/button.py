from tkinter import ttk, constants


class Button(ttk.Button):
    def __init__(self, master, text: str):
        super(Button, self).__init__(
            master=master,
            text=text
        )

    def pack(self, *args,
             pad_x=2,
             pad_y=2,
             fill=constants.X,
             side=constants.LEFT,
             **kwargs):
        super(Button, self).pack(
            *args,
            side=side,
            fill=fill,
            padx=pad_x,
            pady=pad_y,
            **kwargs
        )
