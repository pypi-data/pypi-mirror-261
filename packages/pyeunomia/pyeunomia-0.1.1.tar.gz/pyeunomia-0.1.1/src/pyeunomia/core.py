from pathlib import Path
import duckdb

class Singleton(type):
    """Singleton metaclass."""
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Eunomia(metaclass=Singleton):
    """Represents the Eunomia database, an OMOP CDM test database."""
    _duckdb_con = None
    def connect(self):
        """Returns a connection to the Eunomia database."""
        if not self._duckdb_con:
            wd = Path(__file__).resolve().parent
            self._duckdb_con = duckdb.connect(database = f"{wd}/data/eunomia.duckdb", read_only = False)
        return self._duckdb_con