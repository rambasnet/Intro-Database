# Trigger

- a database object that defines a set of actions to be performed automatically in response to a specific database event, such as an INSERT, UPDATE, DELETE, or even certain DDL (Data Definition Language) statements like CREATE or ALTER
- Triggers are used to enforce business rules, maintain data integrity, and automate certain tasks without requiring manual intervention

- trigger consists of two main components: 
    - **an event** that activates the trigger and a set of actions to be executed when the trigger is activated 
    - **actions** are written in the form of SQL statements, and they can include data modification statements (INSERT, UPDATE, SELECT, DELETE) or other operations.

## CREATE TRIGGER

- syntax:

```sql
CREATE TRIGGER [IF NOT EXISTS] trigger_name
    {BEFORE | AFTER} {INSERT | UPDATE | DELETE} 
ON table_name
FOR EACH ROW
BEGIN
    -- SQL statements to be executed
END;
```

- `CREATE TRIGGER`: Indicates that you want to create a trigger.
- `trigger_name`: The name you want to give to the trigger.
- `BEFORE` or `AFTER`: Specifies whether the trigger should be fired before or after the specified event.
- `INSERT`, `UPDATE`, or `DELETE`: The event that triggers the trigger.
- `ON table_name`: The table on which the trigger should be applied.
- `FOR EACH ROW`: Specifies that the trigger should be fired for each row affected by the event.
- `BEGIN` and `END`: The block where you place the SQL statements that define the actions to be taken when the trigger is activated

- e.g., let's say you have a table named `orders` and you want to automatically update an `order_date` column whenever a new order is inserted
    - you can create a trigger like this:

```sql
CREATE TRIGGER update_order_date
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE orders
    SET order_date = CURRENT_TIMESTAMP
    WHERE order_id = NEW.order_id;
END;
```

In this example:
- `update_order_date` is the name of the trigger.
- `AFTER INSERT` specifies that the trigger should be activated after an INSERT operation.
- `NEW` is a special keyword that refers to the new row being inserted.
- The `UPDATE` statement modifies the `order_date` column for the newly inserted order using the current timestamp.

- Triggers can be powerful tools for maintaining data consistency and automating tasks, but they should be used judiciously to avoid complexity and unintended consequences.

- to trigger the update_order_date, insert a new order into orders tables
- check the oder_date value by refreshing the 

```sql
INSERT INTO orders (order_id, customer_id) values (100, 1);
```


### AFTER UPDATE TRIGGER example

- email can be important and you want to keep track of old emails when customers change their emails
- we can create a log table to keep track of every email changes using a Trigger
- create a customer_email_changes table

```sql
CREATE TABLE customer_email_changes (
    old_id integer,
    new_id integer,
	old_email text,
	new_email text,
	user_action text,
	created_at text
);
```

- let's create AFTER UPDATE Trigger

```sql
CREATE TRIGGER log_customer_after_update 
   AFTER UPDATE ON customers
   WHEN OLD.Email <> New.Email
BEGIN
	INSERT INTO customer_email_changes  (
        old_id,
        new_id,
		old_email,
		new_email,
		user_action,
		created_at
	)
    VALUES
	(
        OLD.CustomerID,
        NEW.CustomerID,
		OLD.email,
		NEW.email,
		'UPDATE',
		DATETIME('NOW')
	) ;
END;
```

- now update some customer's email

```sql
UPDATE customers set Email='newemail@gmail.com' where CustomerId=1;
```

- after executing the update statement check the customer_email_changes table


## DROP TRIGGER

- https://sqlite.org/lang_droptrigger.html
- e.g.,

```sql
DROP TRIGGER IF EXISTS log_customer_after_update;
```

## Check Trigger Information

```sql
SELECT * FROM sqlite_master WHERE type = 'trigger' and name='<trigger_name>';
```


```python
from python import db
```


```python
db_file = 'data/chinook.sqlite'
```


```python
sql_check_trigger = "SELECT * FROM sqlite_master WHERE type = 'trigger' and name='update_order_date';"
```


```python
row = db.select_one_row(db_file, sql_check_trigger, ())
```


```python
print(row)
```

    ('trigger', 'update_order_date', 'orders', 0, 'CREATE TRIGGER update_order_date\nAFTER INSERT ON orders\nFOR EACH ROW\nBEGIN\n    UPDATE orders\n    SET order_date = CURRENT_TIMESTAMP\n    WHERE order_id = NEW.order_id;\nEND')



```python

```
