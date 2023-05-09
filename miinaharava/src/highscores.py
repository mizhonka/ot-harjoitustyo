import sqlite3
class Highscores:
    """Luokka, joka pitää yllä tietokantaa ennätyksistä

    Attributes:
        db: sql-tietokanta
    """
    def __init__(self):
        """Luokan konstruktori
        """
        self.db=sqlite3.connect("scores.db")
        self.db.isolation_level=None
        self.db.execute("CREATE TABLE IF NOT EXISTS Easy (id INTEGER PRIMARY KEY, score INTEGER)")
        self.db.execute("CREATE TABLE IF NOT EXISTS Medium (id INTEGER PRIMARY KEY, score INTEGER)")
        self.db.execute("CREATE TABLE IF NOT EXISTS Hard (id INTEGER PRIMARY KEY, score INTEGER)")
    
    def clear_tables(self):
        self.db.execute("DELETE FROM Easy")
        self.db.execute("DELETE FROM Medium")
        self.db.execute("DELETE FROM Hard")
    
    def set_record(self, v, t):
        """Tarkistaa, onko pelaajan tulos uusi ennätys ja lisää sen tarvittaessa tietokantaan

        Args:
            v: pelattu vaikeusaste
            t: pelaajan aika (tulos)
        """
        table="Easy"
        if v==1:
            table="Medium"
        elif v==2:
            table="Hard"
        command="SELECT score FROM "+table
        scores=self.db.execute(command).fetchall()
        command="INSERT INTO " +table + "(score) VALUES (?)"
        if len(scores)<5:
            self.db.execute(command, [t,])
            command="SELECT * FROM "+table+" ORDER BY score"
            self.db.execute(command)
        print(self.db.execute("SELECT score FROM Easy").fetchall())
        print(self.db.execute("SELECT score FROM Medium").fetchall())
        print(self.db.execute("SELECT score FROM Hard").fetchall())