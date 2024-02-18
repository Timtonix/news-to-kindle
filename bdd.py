import sqlite3


class International:
    def __init__(self):
        self.con = sqlite3.connect("international.db")
        self.cursor = self.con.cursor()
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS journeaux(numero INT NOT NULL, titre TEXT NOT NULL, lien TEXT NOT NULL, date TEXT NOT NULL)"""
        )
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS downloaded(lien TEXT NOT NULL, numero INT NOT NULL)"""
        )

        self.con.commit()

    def insert_journeaux(self, date, lien, timestamp):
        self.cursor.execute("INSERT INTO journeaux VALUES (?,?, ?)", (date, lien, timestamp))
        self.con.commit()

    def get_journeaux(self):
        self.cursor.execute("SELECT * FROM journeaux ORDER BY numero")
        return self.cursor.fetchall()

    def count_table(self):
        self.cursor.execute("SELECT COUNT(*) FROM journeaux")
        return self.cursor.fetchone()[0]




if __name__ == "__main__":
    bdd = International()
    bdd.insert_journeaux("HIER", "demain")