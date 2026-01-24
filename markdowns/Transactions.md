# Transactions

- Like many SQL-based DBMS, SQLite is a transactional database system
- meaning queries can be grouped to execute as a single transaction
- transactions have ACID properites

## Atomic

- means that a change cannot be broken down into smaller ones
- when you commit a transaction, either the entire transaction is applied or nothing is applied

## Consistent

- a transaction must ensure to change the database from one valid state to another
- when a transaction starts and executes a statement to modify data, the database becomes inconsistent; 
    - however, when the transaction is committed or rolled back, it is important that the transaction must keep the database consistent
    
## Isolation

- isolation ensures that multiple transactions can be executed concurrently without interfering with each other - - each transaction is executed in isolation from other transactions, as if it were the only transaction running on the system
- this prevents issues such as data corruption or conflicts that could arise from simultaneous access to the same data by multiple transactions

## Durability

- durability guarantees that once a transaction is successfully completed, its changes are permanently saved and will survive any subsequent system failures, crashes, or power outages
- these changes are stored in a durable medium (such as disk storage) so that they can be recovered even if the system crashes right after the transaction is completed

## Applications

- the ACID properties collectively provide a robust framework for maintaining data integrity and reliability in database management systems, making them suitable for applications where accuracy and consistency of data are paramount, such as financial systems, e-commerce platforms, and various enterprise-level applications

### Drawbacks

- it's important to note that adhering strictly to the ACID properties can sometimes impact system performance, particularly in highly concurrent environments
- some modern databases, especially those designed for specific use cases, might opt for a more relaxed consistency model to achieve better performance and scalability while still ensuring data reliability


## SQLite Transaction

- by default, SQLite operates in auto-commit mode
- meaning that for each command, SQLite starts, processes, and commits the transaction automatically
- syntax:

```sql
BEGIN TRANSACTION;

/* SQL STATEMENTS, INSERT, UPDATE, DELETE, ETC... */

[COMMIT] [ROLLBACK];
```



```python
import sqlite3
from sqlite3 import Error
```


```python
filename = './data/bank.db'
```


```python
# if conn object is used as a cotext manager
# all the statements is considered as a transaction
with sqlite3.connect(filename) as conn:
    cursor = conn.cursor()
    sqls = [
        'DROP TABLE IF EXISTS CHECKING;',
        'CREATE TABLE CHECKING (balance integer);',
        'INSERT INTO CHECKING(balance) VALUES (100);',]
    for sql in sqls:
        cursor.execute(sql)
```


```python
conn = sqlite3.connect(filename)

c = conn.cursor()
c.execute("BEGIN TRANSACTION;")
try:
    c.execute("UPDATE CHECKING SET balance = balance - 5;")
    #c.execute("UPDATE CHECKING SET saving = balance + 10;") # <-- no column name saving
    # comment the above statement and run it again
    c.execute("UPDATE CHECKING SET balance = balance - 5;")
    c.execute('SELECT balance FROM CHECKING;')
    balance = int(c.fetchone()[0])
    if balance < 0:
        print(f'{balance =}')
        raise Error(f'-ve Balance: {balance}')
    c.execute("COMMIT;")
    print('All success...')
except Error as ex:
    c.execute("ROLLBACK;")
    print("Fail! Rolling back...", ex)
finally:
    conn.close()
```

    All success...



```python
from python import db
sql = 'SELECT BALANCE FROM CHECKING;'
rows = db.select_many_rows(filename, sql, ())
print(rows)
```

    [(90,)]



```python

```
