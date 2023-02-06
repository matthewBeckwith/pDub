from tkinter import *
from tkinter.ttk import *

from db import Dub


class SaveAsWindow(Frame):
    def __init__(self):
        Frame.__init__(self)

        self.pack()
        self.master.title("Save As...")
        self.db = Dub()

        # Components
        # ----------
        # SAVE a New Password Button
        self.new_btn = Button(self, text="SAVE", command=self.save)
        self.new_btn.grid()

        # REROLL a New Password Button
        self.new_btn = Button(self, text="REROLL", command=self.save)
        self.new_btn.grid()

        self.mainloop()

    def save(self):
        print("Saved!")
