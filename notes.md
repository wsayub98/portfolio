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
        try:
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
        except Exception as e:
            return {
                "error": str(e)
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

### Router Class
1. register - receive routes defined.
2. set a dict for each route with path,method as key(tuple) and action as value.
3. assign to a local variable that can use accross functions in the router class.
4. handle / request handler. use handler.path,handler.command to find route action in a dict set at no.2


### Routes storage
1. define path, method, action
2. action called from Controller 
3. register by using Router class 

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

# PYTHON POSTGRESQL
```python
import json
json.dumps(dict_data)
```
- convert to json before update/insert json column datatype

## CRUD
### Update
```python
sql = f"UPDATE table SET {key1} = %s, {key2} = %s, {json_key} = %s WHERE id = %s"
values = (value1, value2, json_value)
cursor.execute(sql, values: list)
```
### Create
```python
sql = f"INSERT INTO table ({key1},{key2}) VALUES (%s, %s)"
cursor.execute(sql, values:list)
``` 
### Delete
```python
sql = f"DELETE FROM table WHERE id = %s"
cursor.execute(sql, values:list)
```

# API Request
## Get params body
```python
content_length = int(handler.headers["Content-Length"])
body = handler.rfile.read(content_length)
params = json.loads(body.decode("utf-8")) if body else None
```

## Validation
```python
Raise ValidationError(message)
```
