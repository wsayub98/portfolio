# PYTHON

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



