# DELETE

- the "D" in "CRUD" operations refers to the action of deleting existing records in a DBMS
- allows you to delete one or more rows based on the specified conditions
- helps you keep your database up to date by allowing you to delete records that are no longer needed
- https://sqlite.org/lang_update.html
- syntax:

```
DELETE FROM table_name
WHERE condition;
```

- optional OREDER BY and LIMI clause can be used but rarely
- e.g. query:

```sql
DELETE FROM employees;
```

- what do you think will be the result of above query?
- NOTE: delete statement is powerful tool for deleting records in a table, so be cautious when using it, especially with the WHERE clause, to ensure that you delete the correct records and values
- once DELETE is executed, you can't undo the operation

## WHERE

- optional clause but used almost all the time with DELETE
- used to provide filter/search condition for rows to be deleted by the query
    - WHERE clause should uniquely identify the records to be deleted 
    - Primary Key is primariy used in WHERE clause
- e.g.:

```sql
DELETE employees
WHERE EmployeeId = 8;
```

- run the above query on chinook sqlite db with DBeaver

## DELETE with Python

- DELETE doesn't return records but deletes rows from the table
- use cursor's execute() method to delete one or more records based on the WHERE clause
- must use parameterized query using ? placeholder to use untrusted data as part of the query


```python
from python import db
```


```python
db_file = 'data/chinook.sqlite'
```


```python
emp_id = int(input('Enter employee id: '))
```

    Enter employee id: 9



```python
query = """
        DELETE FROM employees
        WHERE EmployeeId = ?;
    """
```


```python
row_count = db.delete(db_file, query, (emp_id,))
```


```python
print(row_count)
```

    0



