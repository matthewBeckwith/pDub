import tkinter as tk
from tkinter import messagebox

from db import Dub
from password import generate


class GUI(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)

        self.pack()
        self.master.title("pDub")
        self.db = Dub()

        # Components
        # ----------
        # CREATE a New Password Button
        self.new_btn = tk.Button(self, text="NEW", width=5, height=3, command=self.generate)
        self.new_btn.pack()

        # LISTBOX of All Saved Passwords
        self.rows = self.db.get_all()
        self.password_list = tk.Listbox(self)
        for row in self.rows:
            self.password_list.insert(tk.END, row[0])
        self.password_list.pack()

        self.mainloop()

    def generate(self):
        if tk.messagebox.askyesno(title="Strength", message="Would you like to make an Advanced Strength Password?"):
            new_password = generate(11, 'advanced')
        else:
            new_password = generate(11, 'normal')

        if tk.messagebox.askyesno(title="Generated Password", message=f"Is this Password acceptable?\n{new_password}"):
            new_name = "new password"
            self.db.save(new_name, new_password)
            self.password_list.insert(tk.END, new_name)
        else:
            self.generate()

