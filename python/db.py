"""Sqlite Database wrapper.

This module provides a wrapper for sqlite3 database operations.

Example:
    import db

    # create a database connection
    conn = db.create_connection("sqlite.db")
    db.close_connection(conn)

"""

import sys
import sqlite3
from sqlite3 import Error
from typing import Any

def create_connection(db_file: str) -> sqlite3.Connection:
    """Create sqlite3 connection and return it.

    Args:
        db_file (str): sqlite filename to open or create.

    Raises:
        e: sqlite3.Error as an exception.

    Returns:
        sqlite3.Connection: sqlite3 connection object.
    """

    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e, file=sys.stderr)
        raise e


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
    """
    conn = create_connection(db_file)
    with conn:
        try:
            cursor = conn.cursor()
            cursor.execute(create_table_sql)
        except Error as e:
            print(e, file=sys.stderr)
        # Successful, conn.commit() is called automatically afterwards
    # close most be called explictly
    close_connection(conn)


def insert_one_row(db_file: str, insert_row_sql: str, row: tuple[Any]) -> None:
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
            print(e, file=sys.stderr)
        # Successful, conn.commit() is called automatically afterwards
    # close most be called explictly
    close_connection(conn)


def insert_many_rows(db_file: str, insert_rows_sql: str, rows: list[tuple[str]]) -> None:
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
            print(e, file=sys.stderr)
        # Successful, conn.commit() is called automatically afterwards
    # close most be called explictly
    close_connection(conn)


def select_one_row(db_file: str, select_row_sql: str, where: tuple[str]) -> Any:
    """_summary_

    Args:
        db_file (str): _description_
        select_row_sql (str): _description_
        where (tuple[str]): _description_

    Raises:
        e: _description_

    Returns:
        tuple[str]: _description_
    """
    conn = create_connection(db_file)
    with conn:
        try:
            cursor = conn.cursor()
            cursor.execute(select_row_sql, where)
            row = cursor.fetchone()
            return row
        except Error as e:
            print(e, file=sys.stderr)
            raise e
        finally:
            # close most be called explictly
            close_connection(conn)


def select_all_rows(db_file: str, select_rows_sql: str, where: tuple[Any]) -> Any:
    """Select all rows from a table from the select_data_sql statement
    Args:
      db_file (str): database file path
      select_data_sql (str): an SELECT statement
      where (tuple): where clause as tuple for ? placeholder
    Return:
      rows (Any): list of tuples as rows or None
    """
    conn = create_connection(db_file)
    with conn:
        try:
            cursor = conn.cursor()
            cursor.execute(select_rows_sql, where)
            rows = cursor.fetchall()
            return rows
        except Error as e:
            print(e, file=sys.stderr)
            raise e
        finally:
            # close most be called explictly
            close_connection(conn)


def update(db_file: str, update_sql: str, where: tuple[Any]) -> int:
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
            return cursor.rowcount
        except Error as e:
            print(e)
            raise e
        finally:
            # close most be called explictly
            close_connection(conn)
    

def delete(db_file: str, delete_sql: str, where: tuple[Any]) -> int:
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
            return cursor.rowcount
        except Error as e:
            print(e, file=sys.stderr)
            raise e
        finally:
            # close most be called explictly
            close_connection(conn)

    
