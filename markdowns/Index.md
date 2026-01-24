# Database Index

- An index in a database is a data structure that enhances the speed of data retrieval operations on a table
- provides a way to quickly look up records based on the values in one or more columns
- indexes are used to optimize query performance by reducing the amount of data that needs to be scanned when searching for specific information
- instead of scanning the entire table, the database engine can use the index to locate the relevant rows efficiently
- work similar to the way an index works in a book
- the index in a book lists keywords along with the page numbers where those keywords can be found
- a database index contains values from one or more columns along with pointers to the corresponding rows in the table

## Key points about database indexes

1. **Faster Data Retrieval**: 
- indexes allow the database to avoid full-table scans and jump directly to the relevant data
- significantly speeds up query execution for frequently searched columns

2. **B-Tree Structure**:
- most database systems use a B-Tree (balanced tree) structure to store indexes efficiently
- this structure ensures that index lookups have a logarithmic time complexity

3. **Column Selection**:
- you can create indexes on one or multiple columns in a table
- the choice of which columns to index depends on the queries you frequently run

4. **Trade-Offs**: 
- while indexes improve read performance, they can slow down write operations (such as inserts, updates, and deletes) because the index needs to be updated whenever the data changes

5. **Maintenance**: 
- indexes need to be maintained as data changes
- this adds overhead during data modification operations

6. **Unique Index**: 
- a unique index enforces the uniqueness of values in a column
- tt's commonly used for primary key columns

7. **Composite Index**:
- an index that spans multiple columns
- it's useful when queries involve multiple columns together

8. **Covering Index**:
- an index that includes all the columns required to satisfy a query, allowing the query to be executed solely using the index without accessing the actual table

9. **Clustered vs. Non-Clustered**:
- some database systems differentiate between clustered and non-clustered indexes
- A clustered index determines the physical order of data in the table, while a non-clustered index is a separate structure pointing to the data



## CREATE INDEX

- https://sqlite.org/lang_createindex.html

- syntax:

```sql
CREATE INDEX index_name ON table_name(column1_name, column2_name, ...);
```

- e.g. let's create an index on employees table of chinook sqlite database

```sql
CREATE INDEX idx_last_name ON employees(LastName);
```

### CREATE UNIQUE INDEX
- uniqe indexes are contraints that prevent duplicate values in the index column(s)
- similar to UNIQE constraint on column

- e.g.,

```sql
CREATE UNIQUE INDEX idx_email ON employees(Email);
```

### CHECK IF INDEX EXISTS

```sql
SELECT *
FROM
   sqlite_master
WHERE
   type= 'index' and tbl_name = '<your_table_name>' and name = '<your_index_name>';
```


```python
from python import db
```


```python
db_file = "data/chinook.sqlite"
```


```python
sql_create_index = "CREATE UNIQUE INDEX idx_email ON employees(Email);"
```


```python
db.execute_non_query(db_file, sql_create_index)
```


```python
# Manually check if the index is created
# automatically check if index exists
```


```python
sql_select_index = "SELECT * FROM sqlite_master WHERE type='index' and name='idx_email';"
```


```python
row = db.select_one_row(db_file, sql_select_index, ())
```


```python
print(row)
# should return one row with 5 columns: type, tbl_name, rootpage, sql
```

    ('index', 'idx_email', 'employees', 874, 'CREATE UNIQUE INDEX idx_email ON employees(Email)')



```python
# assertion test
assert(row[1] == 'idx_email')
```


```python
assert(len(row) == 5)
```

### DROP INDEX

- e.g.,

```sql
DROP INDEX IF EXISTS idx_email;
```


```python
sql_drop_index = 'DROP INDEX IF EXISTS idx_email'
```


```python
db.execute_non_query(db_file, sql_drop_index)
```


```python
row = db.select_one_row(db_file, sql_select_index, ())
# should return None
```


```python
print(row)
```

    None



```python

```
