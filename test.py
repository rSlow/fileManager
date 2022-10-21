try:
    from Tkinter import *
except ImportError:
    from tkinter import *


class MultipleScrollingListbox(Frame):
    def __init__(self, master):
        super(MultipleScrollingListbox, self).__init__(master=master)

        self.scrollbar = Scrollbar(self, orient='vertical')

        self.list1 = Listbox(self, yscrollcommand=self.scroll_left, selectmode=MULTIPLE)
        self.list2 = Listbox(self, yscrollcommand=self.scroll_right, selectmode=MULTIPLE)

        self.scrollbar.config(command=self.lists_yview)

        self.pack_elements()

        for x in range(30):
            self.list1.insert('end', x)
            self.list2.insert('end', x)

    def scroll_left(self, start, end):
        if self.list2.yview() != self.list1.yview():
            self.list2.yview_moveto(start)
        self.scrollbar.set(start, end)

    def scroll_right(self, start, end):
        if self.list1.yview() != self.list2.yview():
            self.list1.yview_moveto(start)
        self.scrollbar.set(start, end)

    def pack_elements(self):
        self.list1.pack(fill='y', side='left')
        self.list2.pack(expand=1, fill='both', side='left')
        self.scrollbar.pack(side='right', fill='y')

    def lists_yview(self, *args):
        self.list1.yview(*args)
        self.list2.yview(*args)


if __name__ == "__main__":
    root = Tk()
    frame = MultipleScrollingListbox(master=root)
    frame.pack()
    root.mainloop()
