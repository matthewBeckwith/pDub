import sqlite3
from datetime import date


class Dub:
    def __init__(self):
        self.con = sqlite3.connect("data.db")
        self.c = self.con.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS dubs(name TEXT, password TEXT, created_date TEXT)''')

        self.rows = []

    def __del__(self):
        self.con.commit()
        self.con.close()

    def save(self, name, password):
        self.c.execute("INSERT INTO dubs VALUES (?, ?, ?)", (name, password, date.today()))
        self.get_all()

    def get_by_name(self, name) -> list:
        return self.c.execute("SELECT * FROM dubs WHERE name = (?)", (name,))

    def get_all(self) -> list:
        return self.c.execute("SELECT * FROM dubs")

    def remove_by_name(self, name):
        self.c.execute("DELETE FROM dubs WHERE name = (?)", (name,))
        self.get_all()
