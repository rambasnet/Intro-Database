# Python & SQLite

- Python is a general purpose programming language
- Python provides sqlite3 library to connect and manipulate SQLite database
- https://docs.python.org/3/library/sqlite3.html#module-sqlite3

## Connect to a SQLite DB


```python
import sqlite3

conn = sqlite3.connect("test.db")
```


```python
print(sqlite3.version)
```

    2.6.0



```python
conn.close()
```


```python
help(sqlite3)
```

    Help on package sqlite3:
    
    NAME
        sqlite3
    
    MODULE REFERENCE
        https://docs.python.org/3.10/library/sqlite3.html
        
        The following documentation is automatically generated from the Python
        source files.  It may be incomplete, incorrect or include features that
        are considered implementation detail and may vary between Python
        implementations.  When in doubt, consult the module reference at the
        location listed above.
    
    DESCRIPTION
        The sqlite3 extension module provides a DB-API 2.0 (PEP 249) compliant
        interface to the SQLite library, and requires SQLite 3.7.15 or newer.
        
        To use the module, start by creating a database Connection object:
        
            import sqlite3
            cx = sqlite3.connect("test.db")  # test.db will be created or opened
        
        The special path name ":memory:" can be provided to connect to a transient
        in-memory database:
        
            cx = sqlite3.connect(":memory:")  # connect to a database in RAM
        
        Once a connection has been established, create a Cursor object and call
        its execute() method to perform SQL queries:
        
            cu = cx.cursor()
        
            # create a table
            cu.execute("create table lang(name, first_appeared)")
        
            # insert values into a table
            cu.execute("insert into lang values (?, ?)", ("C", 1972))
        
            # execute a query and iterate over the result
            for row in cu.execute("select * from lang"):
                print(row)
        
            cx.close()
        
        The sqlite3 module is written by Gerhard Häring <gh@ghaering.de>.
    
    PACKAGE CONTENTS
        dbapi2
        dump
    
    CLASSES
        builtins.Exception(builtins.BaseException)
            Error
                DatabaseError
                    DataError
                    IntegrityError
                    InternalError
                    NotSupportedError
                    OperationalError
                    ProgrammingError
                InterfaceError
            Warning
        builtins.object
            Connection
            Cursor
            PrepareProtocol
            Row
        
        class Connection(builtins.object)
         |  SQLite database connection object.
         |  
         |  Methods defined here:
         |  
         |  __call__(self, /, *args, **kwargs)
         |      Call self as a function.
         |  
         |  __enter__(self, /)
         |      Called when the connection is used as a context manager.
         |      
         |      Returns itself as a convenience to the caller.
         |  
         |  __exit__(self, type, value, traceback, /)
         |      Called when the connection is used as a context manager.
         |      
         |      If there was any exception, a rollback takes place; otherwise we commit.
         |  
         |  __init__(self, /, *args, **kwargs)
         |      Initialize self.  See help(type(self)) for accurate signature.
         |  
         |  backup(self, /, target, *, pages=-1, progress=None, name='main', sleep=0.25)
         |      Makes a backup of the database.
         |  
         |  close(self, /)
         |      Close the database connection.
         |      
         |      Any pending transaction is not committed implicitly.
         |  
         |  commit(self, /)
         |      Commit any pending transaction to the database.
         |      
         |      If there is no open transaction, this method is a no-op.
         |  
         |  create_aggregate(self, /, name, n_arg, aggregate_class)
         |      Creates a new aggregate.
         |  
         |  create_collation(self, name, callback, /)
         |      Creates a collation function.
         |  
         |  create_function(self, /, name, narg, func, *, deterministic=False)
         |      Creates a new function.
         |  
         |  cursor(...)
         |      Return a cursor for the connection.
         |  
         |  enable_load_extension(self, enable, /)
         |      Enable dynamic loading of SQLite extension modules.
         |  
         |  execute(...)
         |      Executes an SQL statement.
         |  
         |  executemany(self, sql, parameters, /)
         |      Repeatedly executes an SQL statement.
         |  
         |  executescript(self, sql_script, /)
         |      Executes multiple SQL statements at once.
         |  
         |  interrupt(self, /)
         |      Abort any pending database operation.
         |  
         |  iterdump(self, /)
         |      Returns iterator to the dump of the database in an SQL text format.
         |  
         |  load_extension(self, name, /)
         |      Load SQLite extension module.
         |  
         |  rollback(self, /)
         |      Roll back to the start of any pending transaction.
         |      
         |      If there is no open transaction, this method is a no-op.
         |  
         |  set_authorizer(self, /, authorizer_callback)
         |      Sets authorizer callback.
         |  
         |  set_progress_handler(self, /, progress_handler, n)
         |      Sets progress handler callback.
         |  
         |  set_trace_callback(self, /, trace_callback)
         |      Sets a trace callback called for each SQL statement (passed as unicode).
         |  
         |  ----------------------------------------------------------------------
         |  Data descriptors defined here:
         |  
         |  DataError
         |  
         |  DatabaseError
         |  
         |  Error
         |  
         |  IntegrityError
         |  
         |  InterfaceError
         |  
         |  InternalError
         |  
         |  NotSupportedError
         |  
         |  OperationalError
         |  
         |  ProgrammingError
         |  
         |  Warning
         |  
         |  in_transaction
         |  
         |  isolation_level
         |  
         |  row_factory
         |  
         |  text_factory
         |  
         |  total_changes
        
        class Cursor(builtins.object)
         |  SQLite database cursor class.
         |  
         |  Methods defined here:
         |  
         |  __init__(self, /, *args, **kwargs)
         |      Initialize self.  See help(type(self)) for accurate signature.
         |  
         |  __iter__(self, /)
         |      Implement iter(self).
         |  
         |  __next__(self, /)
         |      Implement next(self).
         |  
         |  close(self, /)
         |      Closes the cursor.
         |  
         |  execute(self, sql, parameters=(), /)
         |      Executes an SQL statement.
         |  
         |  executemany(self, sql, seq_of_parameters, /)
         |      Repeatedly executes an SQL statement.
         |  
         |  executescript(self, sql_script, /)
         |      Executes multiple SQL statements at once.
         |  
         |  fetchall(self, /)
         |      Fetches all rows from the resultset.
         |  
         |  fetchmany(self, /, size=1)
         |      Fetches several rows from the resultset.
         |      
         |      size
         |        The default value is set by the Cursor.arraysize attribute.
         |  
         |  fetchone(self, /)
         |      Fetches one row from the resultset.
         |  
         |  setinputsizes(self, sizes, /)
         |      Required by DB-API. Does nothing in sqlite3.
         |  
         |  setoutputsize(self, size, column=None, /)
         |      Required by DB-API. Does nothing in sqlite3.
         |  
         |  ----------------------------------------------------------------------
         |  Data descriptors defined here:
         |  
         |  arraysize
         |  
         |  connection
         |  
         |  description
         |  
         |  lastrowid
         |  
         |  row_factory
         |  
         |  rowcount
        
        class DataError(DatabaseError)
         |  Method resolution order:
         |      DataError
         |      DatabaseError
         |      Error
         |      builtins.Exception
         |      builtins.BaseException
         |      builtins.object
         |  
         |  Data descriptors inherited from Error:
         |  
         |  __weakref__
         |      list of weak references to the object (if defined)
         |  
         |  ----------------------------------------------------------------------
         |  Methods inherited from builtins.Exception:
         |  
         |  __init__(self, /, *args, **kwargs)
         |      Initialize self.  See help(type(self)) for accurate signature.
         |  
         |  ----------------------------------------------------------------------
         |  Static methods inherited from builtins.Exception:
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
         |  __reduce__(...)
         |      Helper for pickle.
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
        
        class DatabaseError(Error)
         |  Method resolution order:
         |      DatabaseError
         |      Error
         |      builtins.Exception
         |      builtins.BaseException
         |      builtins.object
         |  
         |  Data descriptors inherited from Error:
         |  
         |  __weakref__
         |      list of weak references to the object (if defined)
         |  
         |  ----------------------------------------------------------------------
         |  Methods inherited from builtins.Exception:
         |  
         |  __init__(self, /, *args, **kwargs)
         |      Initialize self.  See help(type(self)) for accurate signature.
         |  
         |  ----------------------------------------------------------------------
         |  Static methods inherited from builtins.Exception:
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
         |  __reduce__(...)
         |      Helper for pickle.
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
        
        class Error(builtins.Exception)
         |  Method resolution order:
         |      Error
         |      builtins.Exception
         |      builtins.BaseException
         |      builtins.object
         |  
         |  Data descriptors defined here:
         |  
         |  __weakref__
         |      list of weak references to the object (if defined)
         |  
         |  ----------------------------------------------------------------------
         |  Methods inherited from builtins.Exception:
         |  
         |  __init__(self, /, *args, **kwargs)
         |      Initialize self.  See help(type(self)) for accurate signature.
         |  
         |  ----------------------------------------------------------------------
         |  Static methods inherited from builtins.Exception:
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
         |  __reduce__(...)
         |      Helper for pickle.
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
        
        class IntegrityError(DatabaseError)
         |  Method resolution order:
         |      IntegrityError
         |      DatabaseError
         |      Error
         |      builtins.Exception
         |      builtins.BaseException
         |      builtins.object
         |  
         |  Data descriptors inherited from Error:
         |  
         |  __weakref__
         |      list of weak references to the object (if defined)
         |  
         |  ----------------------------------------------------------------------
         |  Methods inherited from builtins.Exception:
         |  
         |  __init__(self, /, *args, **kwargs)
         |      Initialize self.  See help(type(self)) for accurate signature.
         |  
         |  ----------------------------------------------------------------------
         |  Static methods inherited from builtins.Exception:
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
         |  __reduce__(...)
         |      Helper for pickle.
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
        
        class InterfaceError(Error)
         |  Method resolution order:
         |      InterfaceError
         |      Error
         |      builtins.Exception
         |      builtins.BaseException
         |      builtins.object
         |  
         |  Data descriptors inherited from Error:
         |  
         |  __weakref__
         |      list of weak references to the object (if defined)
         |  
         |  ----------------------------------------------------------------------
         |  Methods inherited from builtins.Exception:
         |  
         |  __init__(self, /, *args, **kwargs)
         |      Initialize self.  See help(type(self)) for accurate signature.
         |  
         |  ----------------------------------------------------------------------
         |  Static methods inherited from builtins.Exception:
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
         |  __reduce__(...)
         |      Helper for pickle.
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
        
        class InternalError(DatabaseError)
         |  Method resolution order:
         |      InternalError
         |      DatabaseError
         |      Error
         |      builtins.Exception
         |      builtins.BaseException
         |      builtins.object
         |  
         |  Data descriptors inherited from Error:
         |  
         |  __weakref__
         |      list of weak references to the object (if defined)
         |  
         |  ----------------------------------------------------------------------
         |  Methods inherited from builtins.Exception:
         |  
         |  __init__(self, /, *args, **kwargs)
         |      Initialize self.  See help(type(self)) for accurate signature.
         |  
         |  ----------------------------------------------------------------------
         |  Static methods inherited from builtins.Exception:
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
         |  __reduce__(...)
         |      Helper for pickle.
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
        
        class NotSupportedError(DatabaseError)
         |  Method resolution order:
         |      NotSupportedError
         |      DatabaseError
         |      Error
         |      builtins.Exception
         |      builtins.BaseException
         |      builtins.object
         |  
         |  Data descriptors inherited from Error:
         |  
         |  __weakref__
         |      list of weak references to the object (if defined)
         |  
         |  ----------------------------------------------------------------------
         |  Methods inherited from builtins.Exception:
         |  
         |  __init__(self, /, *args, **kwargs)
         |      Initialize self.  See help(type(self)) for accurate signature.
         |  
         |  ----------------------------------------------------------------------
         |  Static methods inherited from builtins.Exception:
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
         |  __reduce__(...)
         |      Helper for pickle.
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
        
        class OperationalError(DatabaseError)
         |  Method resolution order:
         |      OperationalError
         |      DatabaseError
         |      Error
         |      builtins.Exception
         |      builtins.BaseException
         |      builtins.object
         |  
         |  Data descriptors inherited from Error:
         |  
         |  __weakref__
         |      list of weak references to the object (if defined)
         |  
         |  ----------------------------------------------------------------------
         |  Methods inherited from builtins.Exception:
         |  
         |  __init__(self, /, *args, **kwargs)
         |      Initialize self.  See help(type(self)) for accurate signature.
         |  
         |  ----------------------------------------------------------------------
         |  Static methods inherited from builtins.Exception:
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
         |  __reduce__(...)
         |      Helper for pickle.
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
        
        class PrepareProtocol(builtins.object)
         |  PEP 246 style object adaption protocol type.
         |  
         |  Methods defined here:
         |  
         |  __init__(self, /, *args, **kwargs)
         |      Initialize self.  See help(type(self)) for accurate signature.
        
        class ProgrammingError(DatabaseError)
         |  Method resolution order:
         |      ProgrammingError
         |      DatabaseError
         |      Error
         |      builtins.Exception
         |      builtins.BaseException
         |      builtins.object
         |  
         |  Data descriptors inherited from Error:
         |  
         |  __weakref__
         |      list of weak references to the object (if defined)
         |  
         |  ----------------------------------------------------------------------
         |  Methods inherited from builtins.Exception:
         |  
         |  __init__(self, /, *args, **kwargs)
         |      Initialize self.  See help(type(self)) for accurate signature.
         |  
         |  ----------------------------------------------------------------------
         |  Static methods inherited from builtins.Exception:
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
         |  __reduce__(...)
         |      Helper for pickle.
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
        
        class Row(builtins.object)
         |  Methods defined here:
         |  
         |  __eq__(self, value, /)
         |      Return self==value.
         |  
         |  __ge__(self, value, /)
         |      Return self>=value.
         |  
         |  __getitem__(self, key, /)
         |      Return self[key].
         |  
         |  __gt__(self, value, /)
         |      Return self>value.
         |  
         |  __hash__(self, /)
         |      Return hash(self).
         |  
         |  __iter__(self, /)
         |      Implement iter(self).
         |  
         |  __le__(self, value, /)
         |      Return self<=value.
         |  
         |  __len__(self, /)
         |      Return len(self).
         |  
         |  __lt__(self, value, /)
         |      Return self<value.
         |  
         |  __ne__(self, value, /)
         |      Return self!=value.
         |  
         |  keys(self, /)
         |      Returns the keys of the row.
         |  
         |  ----------------------------------------------------------------------
         |  Static methods defined here:
         |  
         |  __new__(*args, **kwargs) from builtins.type
         |      Create and return a new object.  See help(type) for accurate signature.
        
        class Warning(builtins.Exception)
         |  Method resolution order:
         |      Warning
         |      builtins.Exception
         |      builtins.BaseException
         |      builtins.object
         |  
         |  Data descriptors defined here:
         |  
         |  __weakref__
         |      list of weak references to the object (if defined)
         |  
         |  ----------------------------------------------------------------------
         |  Methods inherited from builtins.Exception:
         |  
         |  __init__(self, /, *args, **kwargs)
         |      Initialize self.  See help(type(self)) for accurate signature.
         |  
         |  ----------------------------------------------------------------------
         |  Static methods inherited from builtins.Exception:
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
         |  __reduce__(...)
         |      Helper for pickle.
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
    
    FUNCTIONS
        __getattr__(name)
            # bpo-42264: OptimizedUnicode was deprecated in Python 3.10.  It's scheduled
            # for removal in Python 3.12.
        
        adapt(...)
            Adapt given object to given protocol.
        
        complete_statement(statement)
            Checks if a string contains a complete SQL statement.
        
        connect(...)
            connect(database[, timeout, detect_types, isolation_level,
                    check_same_thread, factory, cached_statements, uri])
            
            Opens a connection to the SQLite database file *database*. You can use
            ":memory:" to open a database connection to a database that resides in
            RAM instead of on disk.
        
        enable_callback_tracebacks(enable, /)
            Enable or disable callback functions throwing errors to stderr.
        
        register_adapter(type, adapter, /)
            Register a function to adapt Python objects to SQLite values.
        
        register_converter(typename, converter, /)
            Register a function to convert SQLite values to Python objects.
    
    DATA
        PARSE_COLNAMES = 2
        PARSE_DECLTYPES = 1
        SQLITE_ALTER_TABLE = 26
        SQLITE_ANALYZE = 28
        SQLITE_ATTACH = 24
        SQLITE_CREATE_INDEX = 1
        SQLITE_CREATE_TABLE = 2
        SQLITE_CREATE_TEMP_INDEX = 3
        SQLITE_CREATE_TEMP_TABLE = 4
        SQLITE_CREATE_TEMP_TRIGGER = 5
        SQLITE_CREATE_TEMP_VIEW = 6
        SQLITE_CREATE_TRIGGER = 7
        SQLITE_CREATE_VIEW = 8
        SQLITE_CREATE_VTABLE = 29
        SQLITE_DELETE = 9
        SQLITE_DENY = 1
        SQLITE_DETACH = 25
        SQLITE_DONE = 101
        SQLITE_DROP_INDEX = 10
        SQLITE_DROP_TABLE = 11
        SQLITE_DROP_TEMP_INDEX = 12
        SQLITE_DROP_TEMP_TABLE = 13
        SQLITE_DROP_TEMP_TRIGGER = 14
        SQLITE_DROP_TEMP_VIEW = 15
        SQLITE_DROP_TRIGGER = 16
        SQLITE_DROP_VIEW = 17
        SQLITE_DROP_VTABLE = 30
        SQLITE_FUNCTION = 31
        SQLITE_IGNORE = 2
        SQLITE_INSERT = 18
        SQLITE_OK = 0
        SQLITE_PRAGMA = 19
        SQLITE_READ = 20
        SQLITE_RECURSIVE = 33
        SQLITE_REINDEX = 27
        SQLITE_SAVEPOINT = 32
        SQLITE_SELECT = 21
        SQLITE_TRANSACTION = 22
        SQLITE_UPDATE = 23
        adapters = {(<class 'datetime.date'>, <class 'sqlite3.PrepareProtocol'...
        apilevel = '2.0'
        converters = {'DATE': <function register_adapters_and_converters.<loca...
        paramstyle = 'qmark'
        sqlite_version = '3.40.0'
        sqlite_version_info = (3, 40, 0)
        threadsafety = 1
        version = '2.6.0'
        version_info = (2, 6, 0)
    
    FILE
        /opt/anaconda3/envs/py/lib/python3.10/sqlite3/__init__.py
    
    


## Let's create a connection function

- we can use the function over and again as we need it
- python/db.py file contains utility functions to work with SQLite Database


```python
adict = {'a': 1, 'b': 2, 'c': 3}
```


```python
adict['e']
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    /var/folders/4f/1pkkv7h960j42p0ppgk9n4ywjr6t_b/T/ipykernel_42847/2167921426.py in <module>
    ----> 1 adict['e']
    

    KeyError: 'e'



```python
if 'd' in adict:
    print(adict['d'])
else:
    print('d not found')
```

    d not found



```python
try:
    print(adict['e'])
except KeyError as ex:
    print(ex)
```

    'e'



```python
try:
    print(1/0)
except ZeroDivisionError as ex:
    print(f'{ex}')
```

    division by zero



```python
def create_connection(db_file: str):
  """Create a database connection to a SQLite database.
  
  Args:
    db_file (str): database file
  Return:
    Connection object or None
  """
  conn = None
  try:
      conn = sqlite3.connect(db_file)
  except sqlite3.Error as e:
      print(e)

  return conn
```


```python
conn = create_connection('test.db')
```


```python
# create cursor object
# cursor object is used to execute SQL query
cur = conn.cursor()
```


```python
cur.connection == conn
```




    True




```python
# close connection
conn.close()
```

## Using python/db.py module

- python is a package provided inside Intro-Database repo folder
- empty `__init__.py` file inside a folder makes it a Python package


```python
from python import db
```


```python
help(db)
```

    Help on module python.db in python:
    
    NAME
        python.db
    
    FUNCTIONS
        close_connection(conn: sqlite3.Connection)
            Close a database connection to a SQLite database.
            Args:
              conn (Connection): Connection object
        
        create_connection(db_file: str)
            Create a database connection to a SQLite database.
            Args:
              db_file (str): database file
            Return:
              Connection object or None
        
        create_table(db_file: str, create_table_sql: str)
            Create a table from the create_table_sql statement
            Args:
              db_file (str): database file path
              create_table_sql (str): a CREATE TABLE statement
        
        insert_many_rows(db_file: str, insert_rows_sql: str, rows: list[tuple])
            Insert data into a table from the insert_data_sql statement
            Args:
              db_file (str): database file path
              insert_data_sql (str): an INSERT INTO statement
              rows (list[tuple]): list of tuples as rows to be inserted
        
        insert_one_row(db_file: str, insert_row_sql: str, row: tuple)
            Insert data into a table from the insert_data_sql statement
            Args:
              db_file (str): database file path
              insert_data_sql (str): an INSERT INTO statement
              row (tuple): row as tuple to be inserted
    
    FILE
        /Users/rbasnet/projects/Intro-Database/python/db.py
    
    



```python
conn = db.create_connection('test.db')
```


```python
db.close_connection(conn)
```

## SQLite and Python types

- SQLite natively supports the following types: NULL, INTEGER, REAL, TEXT, BLOB.

The following Python types can thus be sent to SQLite without any problem:

| Python type | SQLite type |
| ----------- | ------------|
| None        | NULL        |
| int         | INTEGER     |
| float       | FLOAT       |
| str         | TEXT        |
| bytes       | BLOB        |  

- data representation
- numbers and BLOBS are written as they're: 100, 99.99
- None and NULL are keywords written as they're
- str in python are wrapped inside 'str', "str", """str""", '''str'''
- TEXT in SQL is written wrapped inside 'text'

## Parameterized query

- in order to prevent SQL-injection attacks, you must use parameterized query
    - never use string formatting to dynamically careate SQL statement from untrusted data
- SQLite3 provides **?** placeholder for each dynamic value to be replaced with
- execute and exectuemany functions in **db** module provide parameters to pass data as arguments
    - pass in data as iterable (tuple or list of tuples) to bind values with each placeholder (?)
- https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.execute


```python

```
