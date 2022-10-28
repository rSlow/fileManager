from tkinter import ttk


class SectionHeader(ttk.Label):
    def __init__(self, *args,
                 text: str,
                 **kwargs):
        super(SectionHeader, self).__init__(
            *args,
            text=text,
            **kwargs
        )
