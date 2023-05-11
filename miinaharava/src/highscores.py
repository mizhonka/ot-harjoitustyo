import sqlite3


class Highscores:
    """Luokka, joka pitää yllä tietokantaa ennätyksistä

    Attributes:
        _db: sql-tietokanta
    """

    def __init__(self):
        """Luokan konstruktori
        """
        self._db = sqlite3.connect("scores._db")
        self._db.isolation_level = None
        self._db.execute(
            "CREATE TABLE IF NOT EXISTS Easy (id INTEGER PRIMARY KEY, score INTEGER)")
        self._db.execute(
            "CREATE TABLE IF NOT EXISTS Medium (id INTEGER PRIMARY KEY, score INTEGER)")
        self._db.execute(
            "CREATE TABLE IF NOT EXISTS Hard (id INTEGER PRIMARY KEY, score INTEGER)")

    def clear_tables(self):
        """Tyhjentää taulukot
        """
        self._db.execute("DELETE FROM Easy")
        self._db.execute("DELETE FROM Medium")
        self._db.execute("DELETE FROM Hard")

    def table_name(self, _v):
        """Palauttaa vaikeusasteen mukaisen taulukon nimen

        Args:
            _v: pelattu vaikeusaste
        """
        table = "Easy"
        if _v in [1,2]:
            table = "Medium"
        elif _v in [3,4]:
            table = "Hard"
        return table

    def get_records(self, _v):
        """Hakee vaikeusasteen ennätykset

        Args:
            _v: pelattu vaikeusaste

        Returns:
            Ennätykset tuplena listassa
        """
        table = self.table_name(_v)
        command = "SELECT score FROM "+table+" ORDER BY score"
        return self._db.execute(command).fetchall()

    def set_record(self, _v, _t):
        """Tarkistaa, onko pelaajan tulos uusi ennätys ja lisää sen tarvittaessa tietokantaan

        Args:
            _v: pelattu vaikeusaste
            _t: pelaajan aika (tulos)
        """
        table = self.table_name(_v)
        command = "SELECT * FROM "+table
        scores = self._db.execute(command).fetchall()
        if len(scores) < 5:
            command = "INSERT INTO " + table + "(score) VALUES (?)"
            self._db.execute(command, [_t,])
        else:
            for _p in scores:
                if _t < _p[1]:
                    command = "SELECT id, MAX(score) FROM "+table
                    worst = self._db.execute(command).fetchone()
                    command = "DELETE FROM "+table+" WHERE id=?"
                    self._db.execute(command, [worst[0]])
                    command = "INSERT INTO " + table + "(score) VALUES (?)"
                    self._db.execute(command, [_t,])
                    break
