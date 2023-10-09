"""Sqlite Database wrapper.

This module provides a wrapper for sqlite3 database operations.

Example:
    import db

    # create a database connection
    conn = db.create_connection("sqlite.db")
    db.close_connection(conn)

"""


import sqlite3
from sqlite3 import Error
from typing import Any, Optional, Tuple, List


def create_connection(db_file: str) -> sqlite3.Connection:
    """Create sqlite3 connection and return it.

    Args:
        db_file (str): sqlite filename to open or create.

    Raises:
        err: sqlite3.Error as an exception.

    Returns:
        sqlite3.Connection: sqlite3 connection object.
    """

    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as err:
        raise err


def close_connection(conn: sqlite3.Connection) -> None:
    """Close a database connection to a SQLite database.
    Args:
      conn (Connection): Connection object
    """
    if conn:
        conn.close()


def create_table(db_file: str, create_table_sql: str) -> None:
    """Create a table from the create_table_sql statement
    Args:
        db_file (str): database file path
        create_table_sql (str): a CREATE TABLE statement

    Raises:
        err: sqlite3.Error as an exception.

    Return:
        None
    """
    conn = create_connection(db_file)
    # with conn:
    try:
        cursor = conn.cursor()
        cursor.execute(create_table_sql)
        conn.commit()
    except Error as err:
        raise err
    # Successful, conn.commit() is called automatically afterwards
    finally:
        # close most be called explictly
        close_connection(conn)


def insert_one_row(db_file: str, insert_row_sql: str,
                   row: Tuple[Any, ...]) -> Optional[int]:
    """Insert data into a table from the insert_data_sql statement
    Args:
      db_file (str): database file path
      insert_data_sql (str): an INSERT INTO statement
      row (tuple): row as tuple to be inserted

    Raises:
        err: sqlite3.Error as an exception.

    Return:
        row_id (int): row id of the last inserted row
    """
    conn = create_connection(db_file)

    try:
        cursor = conn.cursor()
        cursor.execute(insert_row_sql, row)
        conn.commit()
        return cursor.lastrowid
    except Error as err:
        raise err
    # Successful, conn.commit() is called automatically afterwards
    finally:
        # close most be called explictly
        close_connection(conn)


def insert_many_rows(db_file: str, insert_rows_sql: str,
                     rows: List[Any]) -> Optional[int]:
    """Insert data into a table from the insert_data_sql statement
    Args:
      db_file (str): database file path
      insert_data_sql (str): an INSERT INTO statement
      rows (list[tuple]): list of tuples as rows to be inserted

    Raises:
        err: sqlite3.Error as an exception.

    Return:
        row_id (int): row id of the last inserted row
    """
    conn = create_connection(db_file)
    try:
        cursor = conn.cursor()
        cursor.executemany(insert_rows_sql, rows)
        conn.commit()
        return cursor.lastrowid
    except Error as err:
        raise err
    # Successful, conn.commit() is called automatically afterwards
    finally:
        # close most be called explictly
        close_connection(conn)


def select_one_row(db_file: str, select_row_sql: str,
                   where: Tuple[Any, ...]) -> Any:
    """API to select one row from a table from the select_data_sql statement.

    Args:
        db_file (str): database file path
        select_row_sql (str): a SELECT statement
        where (tuple[str]): where clause as tuple for ? placeholder

    Raises:
        err: sqlite3.Error as an exception.

    Returns:
        tuple[str]: row as tuple or None
    """
    conn = create_connection(db_file)
    with conn:
        try:
            cursor = conn.cursor()
            cursor.execute(select_row_sql, where)
            return cursor.fetchone()
        except Error as err:
            raise err


def select_many_rows(db_file: str, select_rows_sql: str,
                     where: Tuple[Any, ...]) -> Any:
    """Select all rows from a table from the select_data_sql statement
    Args:
      db_file (str): database file path
      select_data_sql (str): an SELECT statement
      where (tuple): where clause as tuple for ? placeholder

    Raises:
        err: sqlite3.Error as an exception.

    Return:
      rows (Any): list of tuples as rows or None
    """
    conn = create_connection(db_file)
    with conn:
        try:
            cursor = conn.cursor()
            cursor.execute(select_rows_sql, where)
            return cursor.fetchall()
        except Error as err:
            raise err


def update(db_file: str, update_sql: str,
           where: Tuple[Any, ...]) -> Optional[int]:
    """Update a table from the update_sql statement
    Args:
      db_file (str): database file path
      update_sql (str): an UPDATE statement
      where (tuple): where clause as tuple for ? placeholder

    Raises:
        err: sqlite3.Error as an exception.

    Return:
      rows_affected (int): number of rows affected
    """
    conn = create_connection(db_file)
    with conn:
        try:
            cursor = conn.cursor()
            cursor.execute(update_sql, where)
            return cursor.rowcount
        except Error as err:
            raise err


def delete(db_file: str, delete_sql: str, where: Tuple[Any]) -> int:
    """Delete a table from the delete_sql statement
    Args:
      db_file (str): database file path
      delete_sql (str): a DELETE statement
      where (tuple): where clause as tuple for ? placeholder

    Raises:
        err: sqlite3.Error as an exception.

    Return:
      rows_affected (int): number of rows affected
    """
    conn = create_connection(db_file)
    with conn:
        try:
            cursor = conn.cursor()
            cursor.execute(delete_sql, where)
            return cursor.rowcount
        except Error as err:
            raise err
