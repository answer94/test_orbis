from flask import abort
import sqlite3


class Database():
    def __init__(self):
        self.connection = sqlite3.connect("objects.db")
        self.cur = self.connection.cursor()
        self.create_table()

    def __connect(self):
        self.connection = sqlite3.connect("objects.db")
        self.cur = self.connection.cursor()

    def __close(self):
        self.connection.close()

    def read(self, id):
        if id.isdigit():
            self.__connect()
            self.cur.execute(f"SELECT * FROM Objects WHERE  objectid = {id}")
            try:
                self.rows = self.cur.fetchall()
                if len(self.rows) == 0:
                    abort(404)

                self.idobj, self.name, self.type, self.parents = self.rows[0]
                if self.type == 'папка':
                    self.cur.execute(f"SELECT * FROM Objects WHERE  parents = '{self.parents}'")
                    self.all = self.cur.fetchall()
                    self.__close()
                    return self.all
            except IndexError:
                abort(500)
        else:
            return abort(400)

    def read_all(self):
        self.__connect()
        self.cur.execute(f"SELECT * FROM Objects")
        self.rows = self.cur.fetchall()
        self.__close()
        return self.rows

    def create_table(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS Objects(
               objectid INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT NOT NULL,
               type TEXT NOT NULL,
               parents TEXT NOT NULL)""")

    def insert(self, name, type, parents):
        self.cur.execute("INSERT INTO Objects VALUES(NULL,?,?,?);", (f"{name}", f"{type}", f"{parents}"))
        self.connection.commit()
