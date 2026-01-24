# JSON

- JavaScript Object Notation
- lightweight data-interchange format between systems, client and server, e.g.
- easy for humans to read and write and easy for machines to parse and generate
- often used to transmit data between a server and a web application, as well as for configuration files and data storage (document databases, such as MongoDB)
- JSON is language-independent, meaning it can be used with virtually any programming language
- JSON data is represented as a collection of key-value pairs
    - keys are strings and values can be strings, numbers, booleans, arrays, or other JSON objects
    
- here are couple of examples of JSON data:

```json
{
  "name": "John Doe",
  "age": 30,
  "isStudent": false,
  "hobbies": ["reading", "swimming", "programming"],
  "address": {
    "street": "123 Main St",
    "city": "Exampleville",
    "zipcode": "12345"
  }
}

{
"employees":[
  {"firstName":"John", "lastName":"Doe"},
  {"firstName":"Anna", "lastName":"Smith"},
  {"firstName":"Peter", "lastName":"Jones"}
]
}
```

- JSON syntax is similar to Python dictionary

## Python JSON library

- Python provides starndard library to encode and decode JSON data
- https://docs.python.org/3/library/json.html
- `json.dumps(obj)`
    - converts/encodes Python data structure to JSON string
- `json.loads(str)`
    - decodes JSON strings into Python data structure


```python
import json
```


```python
help(json)
```

    Help on package json:
    
    NAME
        json
    
    MODULE REFERENCE
        https://docs.python.org/3.10/library/json.html
        
        The following documentation is automatically generated from the Python
        source files.  It may be incomplete, incorrect or include features that
        are considered implementation detail and may vary between Python
        implementations.  When in doubt, consult the module reference at the
        location listed above.
    
    DESCRIPTION
        JSON (JavaScript Object Notation) <https://json.org> is a subset of
        JavaScript syntax (ECMA-262 3rd edition) used as a lightweight data
        interchange format.
        
        :mod:`json` exposes an API familiar to users of the standard library
        :mod:`marshal` and :mod:`pickle` modules.  It is derived from a
        version of the externally maintained simplejson library.
        
        Encoding basic Python object hierarchies::
        
            >>> import json
            >>> json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
            '["foo", {"bar": ["baz", null, 1.0, 2]}]'
            >>> print(json.dumps("\"foo\bar"))
            "\"foo\bar"
            >>> print(json.dumps('\u1234'))
            "\u1234"
            >>> print(json.dumps('\\'))
            "\\"
            >>> print(json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True))
            {"a": 0, "b": 0, "c": 0}
            >>> from io import StringIO
            >>> io = StringIO()
            >>> json.dump(['streaming API'], io)
            >>> io.getvalue()
            '["streaming API"]'
        
        Compact encoding::
        
            >>> import json
            >>> mydict = {'4': 5, '6': 7}
            >>> json.dumps([1,2,3,mydict], separators=(',', ':'))
            '[1,2,3,{"4":5,"6":7}]'
        
        Pretty printing::
        
            >>> import json
            >>> print(json.dumps({'4': 5, '6': 7}, sort_keys=True, indent=4))
            {
                "4": 5,
                "6": 7
            }
        
        Decoding JSON::
        
            >>> import json
            >>> obj = ['foo', {'bar': ['baz', None, 1.0, 2]}]
            >>> json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]') == obj
            True
            >>> json.loads('"\\"foo\\bar"') == '"foo\x08ar'
            True
            >>> from io import StringIO
            >>> io = StringIO('["streaming API"]')
            >>> json.load(io)[0] == 'streaming API'
            True
        
        Specializing JSON object decoding::
        
            >>> import json
            >>> def as_complex(dct):
            ...     if '__complex__' in dct:
            ...         return complex(dct['real'], dct['imag'])
            ...     return dct
            ...
            >>> json.loads('{"__complex__": true, "real": 1, "imag": 2}',
            ...     object_hook=as_complex)
            (1+2j)
            >>> from decimal import Decimal
            >>> json.loads('1.1', parse_float=Decimal) == Decimal('1.1')
            True
        
        Specializing JSON object encoding::
        
            >>> import json
            >>> def encode_complex(obj):
            ...     if isinstance(obj, complex):
            ...         return [obj.real, obj.imag]
            ...     raise TypeError(f'Object of type {obj.__class__.__name__} '
            ...                     f'is not JSON serializable')
            ...
            >>> json.dumps(2 + 1j, default=encode_complex)
            '[2.0, 1.0]'
            >>> json.JSONEncoder(default=encode_complex).encode(2 + 1j)
            '[2.0, 1.0]'
            >>> ''.join(json.JSONEncoder(default=encode_complex).iterencode(2 + 1j))
            '[2.0, 1.0]'
        
        
        Using json.tool from the shell to validate and pretty-print::
        
            $ echo '{"json":"obj"}' | python -m json.tool
            {
                "json": "obj"
            }
            $ echo '{ 1.2:3.4}' | python -m json.tool
            Expecting property name enclosed in double quotes: line 1 column 3 (char 2)
    
    PACKAGE CONTENTS
        decoder
        encoder
        scanner
        tool
    
    CLASSES
        builtins.ValueError(builtins.Exception)
            json.decoder.JSONDecodeError
        builtins.object
            json.decoder.JSONDecoder
            json.encoder.JSONEncoder
        
        class JSONDecodeError(builtins.ValueError)
         |  JSONDecodeError(msg, doc, pos)
         |  
         |  Subclass of ValueError with the following additional properties:
         |  
         |  msg: The unformatted error message
         |  doc: The JSON document being parsed
         |  pos: The start index of doc where parsing failed
         |  lineno: The line corresponding to pos
         |  colno: The column corresponding to pos
         |  
         |  Method resolution order:
         |      JSONDecodeError
         |      builtins.ValueError
         |      builtins.Exception
         |      builtins.BaseException
         |      builtins.object
         |  
         |  Methods defined here:
         |  
         |  __init__(self, msg, doc, pos)
         |      Initialize self.  See help(type(self)) for accurate signature.
         |  
         |  __reduce__(self)
         |      Helper for pickle.
         |  
         |  ----------------------------------------------------------------------
         |  Data descriptors defined here:
         |  
         |  __weakref__
         |      list of weak references to the object (if defined)
         |  
         |  ----------------------------------------------------------------------
         |  Static methods inherited from builtins.ValueError:
         |  
         |  __new__(*args, **kwargs) from builtins.type
         |      Create and return a new object.  See help(type) for accurate signature.
         |  
         |  ----------------------------------------------------------------------
         |  Methods inherited from builtins.BaseException:
         |  
         |  __delattr__(self, name, /)
         |      Implement delattr(self, name).
         |  
         |  __getattribute__(self, name, /)
         |      Return getattr(self, name).
         |  
         |  __repr__(self, /)
         |      Return repr(self).
         |  
         |  __setattr__(self, name, value, /)
         |      Implement setattr(self, name, value).
         |  
         |  __setstate__(...)
         |  
         |  __str__(self, /)
         |      Return str(self).
         |  
         |  with_traceback(...)
         |      Exception.with_traceback(tb) --
         |      set self.__traceback__ to tb and return self.
         |  
         |  ----------------------------------------------------------------------
         |  Data descriptors inherited from builtins.BaseException:
         |  
         |  __cause__
         |      exception cause
         |  
         |  __context__
         |      exception context
         |  
         |  __dict__
         |  
         |  __suppress_context__
         |  
         |  __traceback__
         |  
         |  args
        
        class JSONDecoder(builtins.object)
         |  JSONDecoder(*, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, strict=True, object_pairs_hook=None)
         |  
         |  Simple JSON <https://json.org> decoder
         |  
         |  Performs the following translations in decoding by default:
         |  
         |  +---------------+-------------------+
         |  | JSON          | Python            |
         |  +===============+===================+
         |  | object        | dict              |
         |  +---------------+-------------------+
         |  | array         | list              |
         |  +---------------+-------------------+
         |  | string        | str               |
         |  +---------------+-------------------+
         |  | number (int)  | int               |
         |  +---------------+-------------------+
         |  | number (real) | float             |
         |  +---------------+-------------------+
         |  | true          | True              |
         |  +---------------+-------------------+
         |  | false         | False             |
         |  +---------------+-------------------+
         |  | null          | None              |
         |  +---------------+-------------------+
         |  
         |  It also understands ``NaN``, ``Infinity``, and ``-Infinity`` as
         |  their corresponding ``float`` values, which is outside the JSON spec.
         |  
         |  Methods defined here:
         |  
         |  __init__(self, *, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, strict=True, object_pairs_hook=None)
         |      ``object_hook``, if specified, will be called with the result
         |      of every JSON object decoded and its return value will be used in
         |      place of the given ``dict``.  This can be used to provide custom
         |      deserializations (e.g. to support JSON-RPC class hinting).
         |      
         |      ``object_pairs_hook``, if specified will be called with the result of
         |      every JSON object decoded with an ordered list of pairs.  The return
         |      value of ``object_pairs_hook`` will be used instead of the ``dict``.
         |      This feature can be used to implement custom decoders.
         |      If ``object_hook`` is also defined, the ``object_pairs_hook`` takes
         |      priority.
         |      
         |      ``parse_float``, if specified, will be called with the string
         |      of every JSON float to be decoded. By default this is equivalent to
         |      float(num_str). This can be used to use another datatype or parser
         |      for JSON floats (e.g. decimal.Decimal).
         |      
         |      ``parse_int``, if specified, will be called with the string
         |      of every JSON int to be decoded. By default this is equivalent to
         |      int(num_str). This can be used to use another datatype or parser
         |      for JSON integers (e.g. float).
         |      
         |      ``parse_constant``, if specified, will be called with one of the
         |      following strings: -Infinity, Infinity, NaN.
         |      This can be used to raise an exception if invalid JSON numbers
         |      are encountered.
         |      
         |      If ``strict`` is false (true is the default), then control
         |      characters will be allowed inside strings.  Control characters in
         |      this context are those with character codes in the 0-31 range,
         |      including ``'\t'`` (tab), ``'\n'``, ``'\r'`` and ``'\0'``.
         |  
         |  decode(self, s, _w=<built-in method match of re.Pattern object at 0x7fb2612735e0>)
         |      Return the Python representation of ``s`` (a ``str`` instance
         |      containing a JSON document).
         |  
         |  raw_decode(self, s, idx=0)
         |      Decode a JSON document from ``s`` (a ``str`` beginning with
         |      a JSON document) and return a 2-tuple of the Python
         |      representation and the index in ``s`` where the document ended.
         |      
         |      This can be used to decode a JSON document from a string that may
         |      have extraneous data at the end.
         |  
         |  ----------------------------------------------------------------------
         |  Data descriptors defined here:
         |  
         |  __dict__
         |      dictionary for instance variables (if defined)
         |  
         |  __weakref__
         |      list of weak references to the object (if defined)
        
        class JSONEncoder(builtins.object)
         |  JSONEncoder(*, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, sort_keys=False, indent=None, separators=None, default=None)
         |  
         |  Extensible JSON <https://json.org> encoder for Python data structures.
         |  
         |  Supports the following objects and types by default:
         |  
         |  +-------------------+---------------+
         |  | Python            | JSON          |
         |  +===================+===============+
         |  | dict              | object        |
         |  +-------------------+---------------+
         |  | list, tuple       | array         |
         |  +-------------------+---------------+
         |  | str               | string        |
         |  +-------------------+---------------+
         |  | int, float        | number        |
         |  +-------------------+---------------+
         |  | True              | true          |
         |  +-------------------+---------------+
         |  | False             | false         |
         |  +-------------------+---------------+
         |  | None              | null          |
         |  +-------------------+---------------+
         |  
         |  To extend this to recognize other objects, subclass and implement a
         |  ``.default()`` method with another method that returns a serializable
         |  object for ``o`` if possible, otherwise it should call the superclass
         |  implementation (to raise ``TypeError``).
         |  
         |  Methods defined here:
         |  
         |  __init__(self, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, sort_keys=False, indent=None, separators=None, default=None)
         |      Constructor for JSONEncoder, with sensible defaults.
         |      
         |      If skipkeys is false, then it is a TypeError to attempt
         |      encoding of keys that are not str, int, float or None.  If
         |      skipkeys is True, such items are simply skipped.
         |      
         |      If ensure_ascii is true, the output is guaranteed to be str
         |      objects with all incoming non-ASCII characters escaped.  If
         |      ensure_ascii is false, the output can contain non-ASCII characters.
         |      
         |      If check_circular is true, then lists, dicts, and custom encoded
         |      objects will be checked for circular references during encoding to
         |      prevent an infinite recursion (which would cause an RecursionError).
         |      Otherwise, no such check takes place.
         |      
         |      If allow_nan is true, then NaN, Infinity, and -Infinity will be
         |      encoded as such.  This behavior is not JSON specification compliant,
         |      but is consistent with most JavaScript based encoders and decoders.
         |      Otherwise, it will be a ValueError to encode such floats.
         |      
         |      If sort_keys is true, then the output of dictionaries will be
         |      sorted by key; this is useful for regression tests to ensure
         |      that JSON serializations can be compared on a day-to-day basis.
         |      
         |      If indent is a non-negative integer, then JSON array
         |      elements and object members will be pretty-printed with that
         |      indent level.  An indent level of 0 will only insert newlines.
         |      None is the most compact representation.
         |      
         |      If specified, separators should be an (item_separator, key_separator)
         |      tuple.  The default is (', ', ': ') if *indent* is ``None`` and
         |      (',', ': ') otherwise.  To get the most compact JSON representation,
         |      you should specify (',', ':') to eliminate whitespace.
         |      
         |      If specified, default is a function that gets called for objects
         |      that can't otherwise be serialized.  It should return a JSON encodable
         |      version of the object or raise a ``TypeError``.
         |  
         |  default(self, o)
         |      Implement this method in a subclass such that it returns
         |      a serializable object for ``o``, or calls the base implementation
         |      (to raise a ``TypeError``).
         |      
         |      For example, to support arbitrary iterators, you could
         |      implement default like this::
         |      
         |          def default(self, o):
         |              try:
         |                  iterable = iter(o)
         |              except TypeError:
         |                  pass
         |              else:
         |                  return list(iterable)
         |              # Let the base class default method raise the TypeError
         |              return JSONEncoder.default(self, o)
         |  
         |  encode(self, o)
         |      Return a JSON string representation of a Python data structure.
         |      
         |      >>> from json.encoder import JSONEncoder
         |      >>> JSONEncoder().encode({"foo": ["bar", "baz"]})
         |      '{"foo": ["bar", "baz"]}'
         |  
         |  iterencode(self, o, _one_shot=False)
         |      Encode the given object and yield each string
         |      representation as available.
         |      
         |      For example::
         |      
         |          for chunk in JSONEncoder().iterencode(bigobject):
         |              mysocket.write(chunk)
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
         |  item_separator = ', '
         |  
         |  key_separator = ': '
    
    FUNCTIONS
        dump(obj, fp, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)
            Serialize ``obj`` as a JSON formatted stream to ``fp`` (a
            ``.write()``-supporting file-like object).
            
            If ``skipkeys`` is true then ``dict`` keys that are not basic types
            (``str``, ``int``, ``float``, ``bool``, ``None``) will be skipped
            instead of raising a ``TypeError``.
            
            If ``ensure_ascii`` is false, then the strings written to ``fp`` can
            contain non-ASCII characters if they appear in strings contained in
            ``obj``. Otherwise, all such characters are escaped in JSON strings.
            
            If ``check_circular`` is false, then the circular reference check
            for container types will be skipped and a circular reference will
            result in an ``RecursionError`` (or worse).
            
            If ``allow_nan`` is false, then it will be a ``ValueError`` to
            serialize out of range ``float`` values (``nan``, ``inf``, ``-inf``)
            in strict compliance of the JSON specification, instead of using the
            JavaScript equivalents (``NaN``, ``Infinity``, ``-Infinity``).
            
            If ``indent`` is a non-negative integer, then JSON array elements and
            object members will be pretty-printed with that indent level. An indent
            level of 0 will only insert newlines. ``None`` is the most compact
            representation.
            
            If specified, ``separators`` should be an ``(item_separator, key_separator)``
            tuple.  The default is ``(', ', ': ')`` if *indent* is ``None`` and
            ``(',', ': ')`` otherwise.  To get the most compact JSON representation,
            you should specify ``(',', ':')`` to eliminate whitespace.
            
            ``default(obj)`` is a function that should return a serializable version
            of obj or raise TypeError. The default simply raises TypeError.
            
            If *sort_keys* is true (default: ``False``), then the output of
            dictionaries will be sorted by key.
            
            To use a custom ``JSONEncoder`` subclass (e.g. one that overrides the
            ``.default()`` method to serialize additional types), specify it with
            the ``cls`` kwarg; otherwise ``JSONEncoder`` is used.
        
        dumps(obj, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)
            Serialize ``obj`` to a JSON formatted ``str``.
            
            If ``skipkeys`` is true then ``dict`` keys that are not basic types
            (``str``, ``int``, ``float``, ``bool``, ``None``) will be skipped
            instead of raising a ``TypeError``.
            
            If ``ensure_ascii`` is false, then the return value can contain non-ASCII
            characters if they appear in strings contained in ``obj``. Otherwise, all
            such characters are escaped in JSON strings.
            
            If ``check_circular`` is false, then the circular reference check
            for container types will be skipped and a circular reference will
            result in an ``RecursionError`` (or worse).
            
            If ``allow_nan`` is false, then it will be a ``ValueError`` to
            serialize out of range ``float`` values (``nan``, ``inf``, ``-inf``) in
            strict compliance of the JSON specification, instead of using the
            JavaScript equivalents (``NaN``, ``Infinity``, ``-Infinity``).
            
            If ``indent`` is a non-negative integer, then JSON array elements and
            object members will be pretty-printed with that indent level. An indent
            level of 0 will only insert newlines. ``None`` is the most compact
            representation.
            
            If specified, ``separators`` should be an ``(item_separator, key_separator)``
            tuple.  The default is ``(', ', ': ')`` if *indent* is ``None`` and
            ``(',', ': ')`` otherwise.  To get the most compact JSON representation,
            you should specify ``(',', ':')`` to eliminate whitespace.
            
            ``default(obj)`` is a function that should return a serializable version
            of obj or raise TypeError. The default simply raises TypeError.
            
            If *sort_keys* is true (default: ``False``), then the output of
            dictionaries will be sorted by key.
            
            To use a custom ``JSONEncoder`` subclass (e.g. one that overrides the
            ``.default()`` method to serialize additional types), specify it with
            the ``cls`` kwarg; otherwise ``JSONEncoder`` is used.
        
        load(fp, *, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)
            Deserialize ``fp`` (a ``.read()``-supporting file-like object containing
            a JSON document) to a Python object.
            
            ``object_hook`` is an optional function that will be called with the
            result of any object literal decode (a ``dict``). The return value of
            ``object_hook`` will be used instead of the ``dict``. This feature
            can be used to implement custom decoders (e.g. JSON-RPC class hinting).
            
            ``object_pairs_hook`` is an optional function that will be called with the
            result of any object literal decoded with an ordered list of pairs.  The
            return value of ``object_pairs_hook`` will be used instead of the ``dict``.
            This feature can be used to implement custom decoders.  If ``object_hook``
            is also defined, the ``object_pairs_hook`` takes priority.
            
            To use a custom ``JSONDecoder`` subclass, specify it with the ``cls``
            kwarg; otherwise ``JSONDecoder`` is used.
        
        loads(s, *, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)
            Deserialize ``s`` (a ``str``, ``bytes`` or ``bytearray`` instance
            containing a JSON document) to a Python object.
            
            ``object_hook`` is an optional function that will be called with the
            result of any object literal decode (a ``dict``). The return value of
            ``object_hook`` will be used instead of the ``dict``. This feature
            can be used to implement custom decoders (e.g. JSON-RPC class hinting).
            
            ``object_pairs_hook`` is an optional function that will be called with the
            result of any object literal decoded with an ordered list of pairs.  The
            return value of ``object_pairs_hook`` will be used instead of the ``dict``.
            This feature can be used to implement custom decoders.  If ``object_hook``
            is also defined, the ``object_pairs_hook`` takes priority.
            
            ``parse_float``, if specified, will be called with the string
            of every JSON float to be decoded. By default this is equivalent to
            float(num_str). This can be used to use another datatype or parser
            for JSON floats (e.g. decimal.Decimal).
            
            ``parse_int``, if specified, will be called with the string
            of every JSON int to be decoded. By default this is equivalent to
            int(num_str). This can be used to use another datatype or parser
            for JSON integers (e.g. float).
            
            ``parse_constant``, if specified, will be called with one of the
            following strings: -Infinity, Infinity, NaN.
            This can be used to raise an exception if invalid JSON numbers
            are encountered.
            
            To use a custom ``JSONDecoder`` subclass, specify it with the ``cls``
            kwarg; otherwise ``JSONDecoder`` is used.
    
    DATA
        __all__ = ['dump', 'dumps', 'load', 'loads', 'JSONDecoder', 'JSONDecod...
    
    VERSION
        2.0.9
    
    AUTHOR
        Bob Ippolito <bob@redivi.com>
    
    FILE
        /opt/anaconda3/envs/py/lib/python3.10/json/__init__.py
    
    


## Encoding basic Python objects to JSON


```python
json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
```




    '["foo", {"bar": ["baz", null, 1.0, 2]}]'




```python
print(json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True))
```

    {"a": 0, "b": 0, "c": 0}



```python
# pretty printing
print(json.dumps({'4': 5, '6': 7}, sort_keys=True, indent=4))
```

    {
        "4": 5,
        "6": 7
    }


## Decoding JSON


```python
json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')
```




    ['foo', {'bar': ['baz', None, 1.0, 2]}]




```python

```
