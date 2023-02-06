from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

from db import Dub
from password import generate
from save_as_window import SaveAsWindow


class GUI(Frame):
    def __init__(self):
        Frame.__init__(self)

        self.pack()
        self.master.title("pDub")
        self.config(height=500, width=750)
        self.db = Dub()

        # Components
        # ----------
        # CREATE a New Password Button
        self.new_btn = Button(self, text="NEW", command=self.generate)
        self.new_btn.pack()
        self.new_btn.place(x=10, y=10, height=50, width=80)

        # LISTBOX of All Saved Passwords
        self.rows = self.db.get_all()
        self.password_list = Listbox(self, height=20, width=50)
        for row in self.rows:
            self.password_list.insert(END, row[0])
        self.password_list.pack()
        self.password_list.place(x=100, y=10)
        
        # DELETE a saved password
        self.del_btn = Button(self, text="DELETE", command=self.delete)
        self.del_btn.pack()
        self.del_btn.place(x=10, y=360, height=50, width=80)

        self.mainloop()

    def generate(self):
        if messagebox.askyesno(title="Strength", message="Would you like to make an Advanced Strength Password?"):
            new_password = generate(11, 'advanced')
        else:
            new_password = generate(11, 'normal')

        if messagebox.askyesno(title="Generated Password", message=f"Is this Password acceptable?\n{new_password}"):
            SaveAsWindow()

            # new_name = "new password"
            # self.db.save(new_name, new_password)
            # self.password_list.insert(tk.END, new_name)
        else:
            self.generate()

    def delete(self):
        print(self.password_list.get(self.password_list.curselection()))
