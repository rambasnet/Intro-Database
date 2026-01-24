# CREATE

- Create in CRUD is synonums to SQL INSERT statement
- SQL INSERT statement is used to add new records or rows of data into a database table
- allows you to specify the values to be inserted into each column of the table for the new record
- INSERT statement is a key component of the "Create" (C) operation in the CRUD (Create, Read, Update, Delete) paradigm
- https://sqlite.org/lang_insert.html
- basic syntax of the SQL INSERT statement is as follows:

```sql
INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);
```

- Example:

```sql
INSERT INTO Employees (EmployeeID, FirstName, LastName, Department)
VALUES (101, 'John', 'Doe', 'Marketing');
```

- this SQL statement would insert a new record into the "Employees" table with the specified values for each column
- if the table has columns with default values, you might not need to provide a value for those columns in the INSERT statement
- if the table has an auto-incrementing primary key, you generally don't need to provide a value for that column, as the database system will automatically generate it

## Use DBeaver GUI to run insert statements

- connect chinook.db and run the collowing sql statement

```db
INSERT INTO artists (name)
VALUES('Bud Powell');
```
- because the ArtistId column is an auto-increment column, you can ignore it in the statement.


### Insert multiple rows into a table

```sql
INSERT INTO table_name (column1, column2 ,..)
VALUES 
   (value1,value2 ,...),
   (value1,value2 ,...),
    ...
   (value1,value2 ,...);
```
- each row of values represent one record or entity

```sql
INSERT INTO artists (name)
VALUES
	("Buddy Rich"),
	("Candido"),
	("Charlie Byrd");
```

### Insert default values

```sql
INSERT INTO artists DEFAULT VALUES;
```


## Use Python to insert records
- use parameterized query replacing value with ?
- provide data as a tuple
- Tuple represents one row


```python
from python import db
```


```python
help(db)
```

    Help on module python.db in python:
    
    NAME
        python.db - Sqlite Database wrapper.
    
    DESCRIPTION
        This module provides a wrapper for sqlite3 database operations.
        
        Example:
            import db
        
            # create a database connection
            conn = db.create_connection("sqlite.db")
            db.close_connection(conn)
    
    FUNCTIONS
        close_connection(conn: sqlite3.Connection) -> None
            Close a database connection to a SQLite database.
            Args:
              conn (Connection): Connection object
        
        create_connection(db_file: str) -> sqlite3.Connection
            Create sqlite3 connection and return it.
            
            Args:
                db_file (str): sqlite filename to open or create.
            
            Raises:
                err: sqlite3.Error as an exception.
            
            Returns:
                sqlite3.Connection: sqlite3 connection object.
        
        create_table(db_file: str, create_table_sql: str) -> None
            Create a table from the create_table_sql statement
            Args:
                db_file (str): database file path
                create_table_sql (str): a CREATE TABLE statement
            
            Raises:
                err: sqlite3.Error as an exception.
            
            Return:
                None
        
        delete(db_file: str, delete_sql: str, where: tuple[typing.Any]) -> int
            Delete a table from the delete_sql statement
            Args:
              db_file (str): database file path
              delete_sql (str): a DELETE statement
              where (tuple): where clause as tuple for ? placeholder
            
            Raises:
                err: sqlite3.Error as an exception.
            
            Return:
              rows_affected (int): number of rows affected
        
        insert_many_rows(db_file: str, insert_rows_sql: str, rows: list[tuple[str]]) -> int
            Insert data into a table from the insert_data_sql statement
            Args:
              db_file (str): database file path
              insert_data_sql (str): an INSERT INTO statement
              rows (list[tuple]): list of tuples as rows to be inserted for parameterized query
            
            Raises:
                err: sqlite3.Error as an exception.
            
            Return:
                row_id (int): row id of the last inserted row
        
        insert_one_row(db_file: str, insert_row_sql: str, row: tuple[typing.Any]) -> int
            Insert data into a table from the insert_data_sql statement
            Args:
              db_file (str): database file path
              insert_data_sql (str): an INSERT INTO statement
              row (tuple): row as tuple to be inserted
            
            Raises:
                err: sqlite3.Error as an exception.
            
            Return:
                row_id (int): row id of the last inserted row
        
        select_many_rows(db_file: str, select_rows_sql: str, where: tuple[typing.Any]) -> Any
            Select all rows from a table from the select_data_sql statement
            Args:
              db_file (str): database file path
              select_data_sql (str): an SELECT statement
              where (tuple): where clause as tuple for ? placeholder
            
            Raises:
                err: sqlite3.Error as an exception.
            
            Return:
              rows (Any): list of tuples as rows or None
        
        select_one_row(db_file: str, select_row_sql: str, where: tuple[str]) -> Any
            API to select one row from a table from the select_data_sql statement.
            
            Args:
                db_file (str): database file path
                select_row_sql (str): a SELECT statement
                where (tuple[str]): where clause as tuple for ? placeholder
            
            Raises:
                err: sqlite3.Error as an exception.
            
            Returns:
                tuple[str]: row as tuple or None
        
        update(db_file: str, update_sql: str, where: tuple[typing.Any]) -> int
            Update a table from the update_sql statement
            Args:
              db_file (str): database file path
              update_sql (str): an UPDATE statement
              where (tuple): where clause as tuple for ? placeholder
            
            Raises:
                err: sqlite3.Error as an exception.
            
            Return:
              rows_affected (int): number of rows affected
    
    DATA
        Any = typing.Any
            Special type indicating an unconstrained type.
            
            - Any is compatible with every type.
            - Any assumed to have all methods.
            - All values assumed to be instances of Any.
            
            Note that all the above statements are true from the point of view of
            static type checkers. At runtime, Any should not be used with instance
            or class checks.
    
    FILE
        /Users/rbasnet/projects/Intro-Database/python/db.py
    
    



```python
db_file = 'data/chinook.sqlite'
```


```python
sql = "INSERT INTO artists (name) VALUES (?);"
# must provide data as a Python tuple and there must be an extra comma if there's only one value
row = ('Jake Powell',)
```


```python
len(row)
```




    1




```python
db.insert_one_row(db_file, sql, row)
```




    332




```python
sql = 'INSERT INTO artists DEFAULT VALUES;'
db.insert_one_row(db_file, sql, ())
```




    333




```python
sql = """INSERT INTO artists (name)
        VALUES
        ("Buddy Rich"),
        ("Candido"),
        ("Charlie Byrd");
    """
```


```python
sql
```




    'INSERT INTO artists (name)\n        VALUES\n        ("Buddy Rich"),\n        ("Candido"),\n        ("Charlie Byrd");\n    '




```python
# SQL will remove extra white spaces
# we need to call insert_one_row in this case because it's a single SQL statement
db.insert_one_row(db_file, sql, ())
```




    336




```python
# if we use parameterized query, we need to use insert_many_rows
sql = """INSERT INTO artists (name) VALUES (?)"""
data = [('Night Byrd',), ('Shin Lim',), ('Maya',)]
```


```python
db.insert_many_rows(db_file, sql, data)
# check the artists table's data contents
```

## INSERT datetime

- employees table stores BirthDate and HireDate
- let's insert an new employee in the table


```python
from datetime import datetime
```


```python
sql = """
INSERT INTO Employees 
    (LastName, FirstName, Title, ReportsTo, BirthDate, HireDate, Address, City, State, Country, 
    PostalCode, Phone, Fax, Email)
VALUES (?, ?, ?, ?, ?, ?, ?,?,?,?,?,?,?,?)
"""
```


```python
datetime.now()
```




    datetime.datetime(2023, 9, 28, 20, 43, 52, 881564)




```python
hire_date = datetime.now()
```


```python
dob =  datetime.strptime('1/1/1990', '%m/%d/%Y')
```


```python
dob
```




    datetime.datetime(1990, 1, 1, 0, 0)




```python
emp = ('John', 'Doe', 'CFO', 1, dob, hire_date, '123 street', 'GJ', 'CO', 'USA', \
       '12344-234', '970-111-1111', '970-222-2222', 'john@doe.com')
```


```python
db.insert_one_row(db_file, sql, emp)
# let's check the chinook.sqlite database
```




    10



## Exercise

1. Add several playlists records to chinook db's playlists table
    - Add one playlist at a time
    - Add mulitple playlists at once
    
    
2. Add several album records to chinook db's albums table
    - Add one album at at a time
    - Add multiple albums at once


```python

```
