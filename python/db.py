import sqlite3
from sqlite3 import Error

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
  except Error as e:
    print(e)

  return conn

def close_connection(conn: sqlite3.Connection):
  """Close a database connection to a SQLite database.
  Args:
    conn (Connection): Connection object
  """
  if conn:
    conn.close()

def create_table(db_file: str, create_table_sql: str):
  """Create a table from the create_table_sql statement
  Args:
    db_file (str): database file path
    create_table_sql (str): a CREATE TABLE statement
  """
  conn = create_connection(db_file)
  with conn:
    try:
      cursor = conn.cursor()
      cursor.execute(create_table_sql)
    except Error as e:
      print(e)
    # Successful, conn.commit() is called automatically afterwards
  # close most be called explictly
  close_connection(conn)

def insert_one_row(db_file: str, insert_row_sql: str, row: tuple):
  """Insert data into a table from the insert_data_sql statement
  Args:
    db_file (str): database file path
    insert_data_sql (str): an INSERT INTO statement
    row (tuple): row as tuple to be inserted
  """
  conn = create_connection(db_file)
  with conn:
    try:
      cursor = conn.cursor()
      cursor.execute(insert_row_sql, row)
    except Error as e:
      print(e)
    # Successful, conn.commit() is called automatically afterwards
  # close most be called explictly
  close_connection(conn)
   
def insert_many_rows(db_file: str, insert_rows_sql: str, rows: list[tuple]):
  """Insert data into a table from the insert_data_sql statement
  Args:
    db_file (str): database file path
    insert_data_sql (str): an INSERT INTO statement
    rows (list[tuple]): list of tuples as rows to be inserted for parameterized query
  """
  conn = create_connection(db_file)
  with conn:
    try:
      cursor = conn.cursor()
      cursor.executemany(insert_rows_sql, rows)
    except Error as e:
      print(e)
    # Successful, conn.commit() is called automatically afterwards
  # close most be called explictly
  close_connection(conn)

def select_one_row(db_file: str, select_row_sql: str, where: tuple):
  """Select one row from a table from the select_data_sql statement
  Args:
    db_file (str): database file path
    select_data_sql (str): an SELECT statement
    where (tuple): where clause as tuple for ? placeholder
  Return:
    row (tuple) | None : row as tuple or None
  """
  conn = create_connection(db_file)
  with conn:
    try:
      cursor = conn.cursor()
      cursor.execute(select_row_sql, where)
      row = cursor.fetchone()
      return row
    except Error as e:
      print(e)
  # close most be called explictly
  close_connection(conn)

def select_all_rows(db_file: str, select_rows_sql: str, where: tuple):
  """Select all rows from a table from the select_data_sql statement
  Args:
    db_file (str): database file path
    select_data_sql (str): an SELECT statement
    where (tuple): where clause as tuple for ? placeholder
  Return:
    rows (list[tuple]) | None: list of tuples as rows or None
  """
  conn = create_connection(db_file)
  with conn:
    try:
      cursor = conn.cursor()
      cursor.execute(select_rows_sql, where)
      rows = cursor.fetchall()
      return rows
    except Error as e:
      print(e)
  # close most be called explictly
  close_connection(conn)

def update(db_file: str, update_sql: str, where: tuple):
  """Update a table from the update_sql statement
  Args:
    db_file (str): database file path
    update_sql (str): an UPDATE statement
    where (tuple): where clause as tuple for ? placeholder
  Return:
    rows_affected (int): number of rows affected
  """
  conn = create_connection(db_file)
  with conn:
    try:
      cursor = conn.cursor()
      cursor.execute(update_sql, where)
    except Error as e:
      print(e)
    # Successful, conn.commit() is called automatically afterwards
  # close most be called explictly
  close_connection(conn)
  return cursor.rowcount

def delete(db_file: str, delete_sql: str, where: tuple):
  """Delete a table from the delete_sql statement
  Args:
    db_file (str): database file path
    delete_sql (str): a DELETE statement
    where (tuple): where clause as tuple for ? placeholder
  Return:
    rows_affected (int): number of rows affected
  """
  conn = create_connection(db_file)
  with conn:
    try:
      cursor = conn.cursor()
      cursor.execute(delete_sql, where)
    except Error as e:
      print(e)
    # Successful, conn.commit() is called automatically afterwards
  # close most be called explictly
  close_connection(conn)
  return cursor.rowcount
