# MongoDB Data API

- the modern way to access data is via API endpoints
- can develop UI using any platform or language and access data API to access, update, delete data
- enable Data API on [https://cloud.mongodb.com](https://cloud.mongodb.com)
- create a user and API key to access the database
- set appropriate permission settings (read/write, e.g.)
- test API using the "Test Your API" button which directs you to the web-based Postman app
    - Postman is a popular application to test APIs

## REST API
- Representational State Transfer Application Programming Interface
- a set of architectural principles and constraints for designing and interacting with web services
- it is not a specific technology or protocol but rather a style of building and consuming web services.
- RESTful APIs are commonly used in web development for creating communication interfaces between different software systems over the internet

The key principles and characteristics of RESTful APIs include:

1. **Stateless:** Each request from a client to a server must contain all the information needed to understand and process the request. The server should not rely on any previous requests or store any client-specific state between requests.

2. **Client-Server Architecture:** REST separates the concerns of the client (the user interface and user experience) from the server (the data storage and processing). This separation allows both the client and server to evolve independently.

3. **Uniform Interface:** REST APIs have a consistent and uniform interface, which typically includes a set of standard HTTP methods (GET, POST, PUT, DELETE) for performing operations on resources. Each resource is identified by a unique URI (Uniform Resource Identifier).

4. **Resource-Based:** In REST, everything is considered a resource, and each resource is identified by a URL. Resources can represent entities such as users, products, or any other data object.

5. **Representation:** Resources can have multiple representations, such as JSON, XML, HTML, or others. Clients can request the representation they prefer or understand.

6. **Stateless Communication:** Each request from a client to a server must be self-contained and include all necessary information. Servers do not need to maintain any information about the client's state between requests.

7. **Layered System:** REST allows for the use of a layered architecture, where different components (e.g., load balancers, caches, security layers) can be added or removed without affecting the core functionality.

8. **Cacheability:** Responses from a REST API can be explicitly marked as cacheable or non-cacheable, allowing for efficient use of caching mechanisms to improve performance.

9. **Statelessness:** RESTful interactions should be stateless, meaning that each request from a client to a server must contain all the information needed to understand and process the request. Servers should not rely on any previous requests or store any client-specific state between requests.

10. **Idempotent:** Certain HTTP methods, like GET, HEAD, and PUT, should be idempotent. This means that making the same request multiple times should have the same effect as making it once. It ensures that repeated requests do not have unintended side effects.

RESTful APIs are widely used in web and mobile application development because they are simple, scalable, and easy to understand. They leverage the existing HTTP protocol, making them accessible to a wide range of clients and platforms. Developers use HTTP methods to perform CRUD (Create, Read, Update, Delete) operations on resources, making it a popular choice for building web services.

- E.g.:
- pick POST
- set URL end point: https://us-west-2.aws.data.mongodb-api.com/app/data-ezpqr/endpoint/data/v1/action/insertOne
- set Headers key:value pairs:
    - Content-Type: application/json
    - Access-Control-Request-Headers: *
    - api-key: `<your API key generated for a user>`
- Body:
```json
{
    "collection": "recipes",
    "database": "myDatabase",
    "dataSource": "Cluster0",
    "document": {
        "name": "Fajita",
        "ingredients": [
            "potato",
            "onion",
            "ground beef",
            "oil"
        ],
        "prep_time": 55
    }
}
```
- if successfully, submitted, you'll see a JSON result body with a unique object id:

```json
{
    "insertedId": "<object id>"
}
```


## API Access using requests library

- install `requests` library as it's not a standard library
- 
```bash
$ pip install requests
```
- Python provides a powerful `requests` library to work with Web API
- detail guide on requests library - [https://realpython.com/python-requests/#request-headers](https://realpython.com/python-requests/#request-headers)


```python
import requests
```


```python
help(requests)
```

    Help on package requests:
    
    NAME
        requests
    
    DESCRIPTION
        Requests HTTP Library
        ~~~~~~~~~~~~~~~~~~~~~
    
        Requests is an HTTP library, written in Python, for human beings.
        Basic GET usage:
    
           >>> import requests
           >>> r = requests.get('https://www.python.org')
           >>> r.status_code
           200
           >>> b'Python is a programming language' in r.content
           True
    
        ... or POST:
    
           >>> payload = dict(key1='value1', key2='value2')
           >>> r = requests.post('https://httpbin.org/post', data=payload)
           >>> print(r.text)
           {
             ...
             "form": {
               "key1": "value1",
               "key2": "value2"
             },
             ...
           }
    
        The other HTTP methods are supported - see `requests.api`. Full documentation
        is at <https://requests.readthedocs.io>.
    
        :copyright: (c) 2017 by Kenneth Reitz.
        :license: Apache 2.0, see LICENSE for more details.
    
    PACKAGE CONTENTS
        __version__
        _internal_utils
        adapters
        api
        auth
        certs
        compat
        cookies
        exceptions
        help
        hooks
        models
        packages
        sessions
        status_codes
        structures
        utils
    
    FUNCTIONS
        check_compatibility(urllib3_version, chardet_version, charset_normalizer_version)
    
    DATA
        __author_email__ = 'me@kennethreitz.org'
        __build__ = 143616
        __cake__ = '✨ 🍰 ✨'
        __copyright__ = 'Copyright Kenneth Reitz'
        __description__ = 'Python HTTP for Humans.'
        __license__ = 'Apache 2.0'
        __title__ = 'requests'
        __url__ = 'https://requests.readthedocs.io'
        chardet_version = None
        charset_normalizer_version = '3.3.0'
        codes = <lookup 'status_codes'>
    
    VERSION
        2.31.0
    
    AUTHOR
        Kenneth Reitz
    
    FILE
        /usr/local/lib/python3.12/site-packages/requests/__init__.py
    
    



```python
# let's use API provided by Internation Space Station
# http://api.open-notify.org/iss-now.json
response = requests.get('http://api.open-notify.org/iss-now.json')
print(response.json())
```

    {'iss_position': {'latitude': '41.3050', 'longitude': '86.9968'}, 'timestamp': 1696909836, 'message': 'success'}



```python
end_point = 'https://us-west-2.aws.data.mongodb-api.com/app/data-ezpqr/endpoint/data/v1/action'
```


```python
funct = 'find'
```


```python
api_key = '<paste your key here>'
```


```python
headers = {'Content-Type': 'application/json', 
        'Access-Control-Request-Headers': '*',
        'api-key': f'{api_key}'}
```


```python
payload = {
    "collection": "recipes",
    "database": "myDatabase",
    "dataSource": "Cluster0",
    "filter": {
        "ingredients": "potato"
    }
}
```


```python
# use session to store and cache headers info
session = requests.Session()
```


```python
session.headers.update(headers)
```


```python
# send payload/body as json parameter and NOT data
response = session.post(f'{end_point}/{funct}', json=payload)
```


```python
# let's see the help on Response object
help(response)
```

    Help on Response in module requests.models object:
    
    class Response(builtins.object)
     |  The :class:`Response <Response>` object, which contains a
     |  server's response to an HTTP request.
     |
     |  Methods defined here:
     |
     |  __bool__(self)
     |      Returns True if :attr:`status_code` is less than 400.
     |
     |      This attribute checks if the status code of the response is between
     |      400 and 600 to see if there was a client error or a server error. If
     |      the status code, is between 200 and 400, this will return True. This
     |      is **not** a check to see if the response code is ``200 OK``.
     |
     |  __enter__(self)
     |
     |  __exit__(self, *args)
     |
     |  __getstate__(self)
     |      Helper for pickle.
     |
     |  __init__(self)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  __iter__(self)
     |      Allows you to use a response as an iterator.
     |
     |  __nonzero__(self)
     |      Returns True if :attr:`status_code` is less than 400.
     |
     |      This attribute checks if the status code of the response is between
     |      400 and 600 to see if there was a client error or a server error. If
     |      the status code, is between 200 and 400, this will return True. This
     |      is **not** a check to see if the response code is ``200 OK``.
     |
     |  __repr__(self)
     |      Return repr(self).
     |
     |  __setstate__(self, state)
     |
     |  close(self)
     |      Releases the connection back to the pool. Once this method has been
     |      called the underlying ``raw`` object must not be accessed again.
     |
     |      *Note: Should not normally need to be called explicitly.*
     |
     |  iter_content(self, chunk_size=1, decode_unicode=False)
     |      Iterates over the response data.  When stream=True is set on the
     |      request, this avoids reading the content at once into memory for
     |      large responses.  The chunk size is the number of bytes it should
     |      read into memory.  This is not necessarily the length of each item
     |      returned as decoding can take place.
     |
     |      chunk_size must be of type int or None. A value of None will
     |      function differently depending on the value of `stream`.
     |      stream=True will read data as it arrives in whatever size the
     |      chunks are received. If stream=False, data is returned as
     |      a single chunk.
     |
     |      If decode_unicode is True, content will be decoded using the best
     |      available encoding based on the response.
     |
     |  iter_lines(self, chunk_size=512, decode_unicode=False, delimiter=None)
     |      Iterates over the response data, one line at a time.  When
     |      stream=True is set on the request, this avoids reading the
     |      content at once into memory for large responses.
     |
     |      .. note:: This method is not reentrant safe.
     |
     |  json(self, **kwargs)
     |      Returns the json-encoded content of a response, if any.
     |
     |      :param \*\*kwargs: Optional arguments that ``json.loads`` takes.
     |      :raises requests.exceptions.JSONDecodeError: If the response body does not
     |          contain valid json.
     |
     |  raise_for_status(self)
     |      Raises :class:`HTTPError`, if one occurred.
     |
     |  ----------------------------------------------------------------------
     |  Readonly properties defined here:
     |
     |  apparent_encoding
     |      The apparent encoding, provided by the charset_normalizer or chardet libraries.
     |
     |  content
     |      Content of the response, in bytes.
     |
     |  is_permanent_redirect
     |      True if this Response one of the permanent versions of redirect.
     |
     |  is_redirect
     |      True if this Response is a well-formed HTTP redirect that could have
     |      been processed automatically (by :meth:`Session.resolve_redirects`).
     |
     |  links
     |      Returns the parsed header links of the response, if any.
     |
     |  next
     |      Returns a PreparedRequest for the next request in a redirect chain, if there is one.
     |
     |  ok
     |      Returns True if :attr:`status_code` is less than 400, False if not.
     |
     |      This attribute checks if the status code of the response is between
     |      400 and 600 to see if there was a client error or a server error. If
     |      the status code is between 200 and 400, this will return True. This
     |      is **not** a check to see if the response code is ``200 OK``.
     |
     |  text
     |      Content of the response, in unicode.
     |
     |      If Response.encoding is None, encoding will be guessed using
     |      ``charset_normalizer`` or ``chardet``.
     |
     |      The encoding of the response content is determined based solely on HTTP
     |      headers, following RFC 2616 to the letter. If you can take advantage of
     |      non-HTTP knowledge to make a better guess at the encoding, you should
     |      set ``r.encoding`` appropriately before accessing this property.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __dict__
     |      dictionary for instance variables (if defined)
     |
     |  __weakref__
     |      list of weak references to the object (if defined)
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |
     |  __attrs__ = ['_content', 'status_code', 'headers', 'url', 'history', '...
    



```python
response.status_code
```




    200




```python
response.headers
```




    {'content-encoding': 'gzip', 'content-type': 'application/json', 'strict-transport-security': 'max-age=31536000; includeSubdomains;', 'vary': 'Origin', 'x-appservices-request-id': '6524d19c194aa844588827c6', 'x-frame-options': 'DENY', 'date': 'Tue, 10 Oct 2023 04:22:53 GMT', 'content-length': '200', 'x-envoy-upstream-service-time': '909', 'server': 'mdbws', 'x-envoy-decorator-operation': 'baas-main.baas-prod.svc.cluster.local:8086/*'}




```python
# status_code 200 is OK
if response.status_code == 200:
    data = response.json()
else:
    print(response)
```


```python
data
```




    {'documents': [{'_id': '65246969eff7a7b93ceedc0f',
       'name': 'patatas bravas',
       'ingredients': ['potato',
        'tomato',
        'olive oil',
        'onion',
        'garlic',
        'paprika'],
       'prep_time': 72},
      {'_id': '6524c26c22d249950599ffb1',
       'name': 'Fajita',
       'ingredients': ['potato', 'onion', 'ground beef', 'oil'],
       'prep_time': 55}]}




```python
# json() method returns python dictionary
type(data)
```




    dict




```python
from pprint import pprint
```


```python
for obj in data['documents']:
    #pprint(obj)
    print(f"Recipe: {obj['name']} needs following ingredients:")
    print('\t', end= '')
    #for ing in obj['ingredients']:
    #    print(ing, end=',')
    print(', '.join(obj['ingredients']))
    print(f'Prep time: {obj["prep_time"]}') 
    print()
```

    Recipe: patatas bravas needs following ingredients:
    	potato, tomato, olive oil, onion, garlic, paprika
    Prep time: 72
    
    Recipe: Fajita needs following ingredients:
    	potato, onion, ground beef, oil
    Prep time: 55
    



```python
from typing import Dict
from typing import Any
```


```python
# let's create our own API function to insert the recipe
def insertRecipe(session: requests.Session, payload: Dict[str, Any]) -> None:
    end_point = 'https://us-west-2.aws.data.mongodb-api.com/app/data-ezpqr/endpoint/data/v1/action/insertOne'
    response = session.post(end_point, json=payload)
    return response
    
    
```


```python
payload = {
    "collection": "recipes",
    "database": "myDatabase",
    "dataSource": "Cluster0",
    "document": {
        "name": "Beef Enchilada",
        "ingredients": [
            "potato",
            "onion",
            "ground beef",
            "oil",
            "tortillas",
            "cheese"
        ],
        "prep_time": 35
    }
}
```


```python
result = insertRecipe(session, payload)
```


```python
# 201 Created Success!
if result.status_code == 201:
    print(result.json())
else:
    print(result)
```

    {'insertedId': '6524d8c051cf4db0aa503ec1'}



```python

```


```python

```
