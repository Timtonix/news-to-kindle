import sqlite3


class International:
    def __init__(self):
        self.con = sqlite3.connect("international.db")
        self.cursor = self.con.cursor()
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS journeaux(date TEXT NOT NULL, lien TEXT NOT NULL, timestamp INTEGER NOT NULL)"""
        )

        self.con.commit()

    def insert_journeaux(self, date, lien, timestamp):
        self.cursor.execute("INSERT INTO journeaux VALUES (?,?, ?)", (date, lien, timestamp))
        self.con.commit()

    def get_journeaux(self):
        self.cursor.execute("SELECT * FROM journeaux ORDER BY timestamp")



if __name__ == "__main__":
    bdd = International()
    bdd.insert_journeaux("HIER", "demain")