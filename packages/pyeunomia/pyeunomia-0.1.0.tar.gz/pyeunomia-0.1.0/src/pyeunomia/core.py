import sqlite3
from pathlib import Path

class Singleton(type):
    """Singleton metaclass."""
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Eunomia(metaclass=Singleton):
    """Represents the Eunomia database, an OMOM CDM test database."""
    _sqlite_con = None
    def connect(self):
        """Returns a connection to the Eunomia database."""
        if not self._sqlite_con:
            wd = Path(__file__).resolve().parent
            self._sqlite_con = sqlite3.connect(wd / "data" / "cdm.sqlite")
        return self._sqlite_con