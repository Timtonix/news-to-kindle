import sqlite3


class International:
    def __init__(self):
        self.con = sqlite3.connect("international.db")
        self.cursor = self.con.cursor()
        self.execute(
            """CREATE TABLE IF NOT EXISTS journeaux(date DATE NOT NULL, lien TEXT NOT NULL)"""
        )

        self.con.commit()

    def insert_journeaux(self, date, lien):
        self.cursor.execute("INSERT INTO journeaux VALUES (?,?)", (date, lien))



if __name__ == "__main__":
    bdd = International()
    bdd.insert_journeaux("HIER", "demain")