# pyeunomia

Eunomia is a standard dataset in the OMOP (Observational Medical Outcomes Partnership) Common Data Model (CDM) for testing and demonstration purposes. Eunomia is used for many of the exercises in the [Book of OHDSI](https://ohdsi.github.io/TheBookOfOhdsi/).

This library is just a simple wrapper for the SQLite Eunomia database. 

## Usage

The `connect()` method returns a SQL interface compliant with the DB-API 2.0 specification described by [PEP 249](https://peps.python.org/pep-0249/).

```python
import pyeunomia
conn = pyeunomia.Eunomia().connect()
cur = conn.execute("select count(*) from person")
cur.fetchone()
```
```
(2694,)
```
```python
conn.close()
```