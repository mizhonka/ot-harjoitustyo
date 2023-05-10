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
        """Tyhjentää taulukot
        """
        self.db.execute("DELETE FROM Easy")
        self.db.execute("DELETE FROM Medium")
        self.db.execute("DELETE FROM Hard")
    
    def table_name(self, v):
        """Palauttaa vaikeusasteen mukaisen taulukon nimen

        Args:
            v: pelattu vaikeusaste
        """
        table="Easy"
        if v==1 or v==2:
            table="Medium"
        elif v==3 or v==4:
            table="Hard"
        return table
    
    def get_records(self, v):
        """Hakee vaikeusasteen ennätykset

        Args:
            v: pelattu vaikeusaste
        
        Returns:
            Ennätykset tuplena listassa
        """
        table=self.table_name(v)
        command="SELECT score FROM "+table+" ORDER BY score"
        return self.db.execute(command).fetchall()
    
    def set_record(self, v, t):
        """Tarkistaa, onko pelaajan tulos uusi ennätys ja lisää sen tarvittaessa tietokantaan

        Args:
            v: pelattu vaikeusaste
            t: pelaajan aika (tulos)
        """
        table=self.table_name(v)
        command="SELECT * FROM "+table
        scores=self.db.execute(command).fetchall()
        if len(scores)<5:
            command="INSERT INTO " +table + "(score) VALUES (?)"
            self.db.execute(command, [t,])
        else:
            for p in scores:
                if t<p[1]:
                    command="SELECT id, MAX(score) FROM "+table
                    worst=self.db.execute(command).fetchone()
                    command="DELETE FROM "+table+" WHERE id=?"
                    self.db.execute(command, [worst[0]])
                    command="INSERT INTO " +table + "(score) VALUES (?)"
                    self.db.execute(command, [t,])
                    break