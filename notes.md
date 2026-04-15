# PYTHON
 - python3
 - pip3

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## class

```PYTHON
class ClassName
    # constructor
    def __init__(self, params):
        # code
        self.params = params

    def to_dict(self):
        return {
            "params": [
                {
                    "key1": "value1"
                },
                {
                    "key1": "value1"
                }
            ]
        }

classObj = className(params=[{"key1": "vlaue1"}])

print(classObj.to_dict())
```

## HTTP Server

packages/library
 - BaseHttpRequestHandler, HTTPServer from http.server

server class
```PYTHON
# class Child(Parent)
class RequestHandler(BaseHttpRequestHandler):
    # func to handle ROUTES
    
# global func to run server.
```

## Router

router class to handle path, method and action
 - static function
  - get path, method
  - loop routes against request url
  - loop until found, if found return respone with 200 code
  - failed, exit loop return error with 404 code (page not found)



# POSTGRESQL
- sudo apt install postgresql
- psycopg2 . PostgreSQL python db adapter.

## Driver

### psycopg2
```bash
pip3 install psycopg2-binary
```

## DB

### Operations
```bash
sudo -i -u postgres
```

```sql
ALTER USER postgres WITH PASSWORD 'postgres';
```

```sql
CREATE USER root WITH PASSWORD 'password' CREATEDB CREATEROLE;
```

```sql
CREATE DATABASE portfolio;
```

```bash
psql -U root -d portfolio -h localhost -W
```

# PYTHON Psycopg usage

```python
class DATABASE:
    # static method to define connection.
    # return psycopg2 connect () with params to connect db.
    # dbname, user, password, host, port
```

## Repository to perform DB Operations

```python
class ClassRepository:
    # staticmethod - select, create, update, delete
    # inside method - connect to DB class, open cursor, cursor execute sql, fetch, close conn,cur
    # fetch: cursor_factory - RealDictCursor~([param]), None~(tuple - [0])
```

### Basic Flow
```python
Database > RepositoryClass > ServiceClass~ModelClass > ControllerClass
```
