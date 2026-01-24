# UPDATE

- the "U" in "CRUD" operations refers to the action of updating/modifying existing data in a DBMS
- allows you to change the values of one or more columns in one or more rows based on specified conditions
- helps you keep your database up to date by allowing you to make changes to existing data
- https://sqlite.org/lang_update.html
- syntax:

```
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```
- optional OREDER BY and LIMI clause can be used but rare
- e.g. query:

```sql
UPDATE employees
SET salary = 55000;
```
- what do you think will be the result of above query?
- NOTE: update statement is powerful tool for modifying data in a table, so be cautious when using it, especially with the WHERE clause, to ensure that you update the correct records and values
- once UPDATE is executed, you can't undo the operation

## WHERE

- optional clause but used almost all the time
- used to provide filter/search condition for rows to be updated by the query
    - WHERE clause should uniquely identify the records to be deleted 
    - Primary Key is primariy used in WHERE clause
- e.g.:

```sql
UPDATE employees
SET salary = 55000
WHERE employee_id = 123;
```

- run the following query on chinook sqlite db with DBeaver

```
UPDATE employees
SET Title = 'IT Manager'
WHERE EmployeeId = 8;
```


## UPDATE with Python

- UPDATE doesn't return records but updates values in place in the table columns
- use cursor's execute() method to update one or many records based on the WHERE clause
- use parameterized query using ? placeholder to use untrusted data as part of the query



```python
from python import db
```


```python
db_file = 'data/chinook.sqlite'
```


```python
emp_id = int(input('Enter employee id: '))
```

    Enter employee id: 1



```python
query = """
        UPDATE employees
        SET Title = 'IT Specialist'
        WHERE EmployeeId = ?;
    """
```


```python
row_count = db.update(db_file, query, (emp_id,))
```


```python
print(row_count)
```

    1



