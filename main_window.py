from tkinter import *
from tkinter.ttk import *

from db import Dub
from password import generate


class MainWindow(Tk):
    def __init__(self):
        Tk.__init__(self)

        # Window Settings
        self.title("pDub")
        self.geometry("600x480")

        # Load Images
        search_img = PhotoImage(file="~/Documents/Programming/Python/pDub/assets/search.png")
        show_img = PhotoImage(file="~/Documents/Programming/Python/pDub/assets/eye.png")

        # Components
        self.show_all_btn = Button(self, image=show_img, text="Show All")
        self.show_all_btn.grid(row=0, column=0)

        self.search_btn = Button(self, image=search_img, text="Search")
        self.search_btn.grid(row=0, column=2)

        self.mainloop()


if __name__ == "__main__":
    MainWindow()
