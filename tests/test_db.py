"""Test module for db.py
"""


import os
import unittest
import sqlite3
from typing import Tuple
from python import db


class TestDB(unittest.TestCase):
    """Test class for db.py
    """

    def setUp(self) -> None:
        """Setup
        """
        self.db_file = "sqlite.db"

    def tearDown(self) -> None:
        """Teardown
        """
        if os.path.exists(self.db_file):
            os.remove(self.db_file)

    def test_create_connection(self) -> None:
        """Test create_connection function.
        """
        conn = db.create_connection(self.db_file)
        self.assertIsInstance(conn, sqlite3.Connection)
        db.close_connection(conn)

    def test_close_connection(self) -> None:
        """Test close_connection function.
        """
        conn = db.create_connection(self.db_file)
        db.close_connection(conn)
        self.assertRaises(sqlite3.ProgrammingError,
                          conn.execute, "SELECT 1")

    def test_create_table(self) -> None:
        """Test create_table function.
        """
        sql = """CREATE TABLE IF NOT EXISTS test (
            id integer PRIMARY KEY,
            name text NOT NULL,
            age integer
        );"""
        db.create_table(self.db_file, sql)
        self.assertTrue(os.path.exists(self.db_file))

    def test_insert_one_row(self) -> None:
        """Test insert_one_row function.
        """
        sql = """CREATE TABLE IF NOT EXISTS test (
            id integer PRIMARY KEY,
            name text NOT NULL,
            age integer
        );"""
        db.create_table(self.db_file, sql)
        sql = """INSERT INTO test (name, age) VALUES (?, ?);"""
        data_in = ("John", 20)
        db.insert_one_row(self.db_file, sql, data_in)
        conn = db.create_connection(self.db_file)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM test")
        data_out = cursor.fetchone()
        self.assertEqual(data_in, data_out[1:])
        db.close_connection(conn)

    def test_insert_one_row_error(self) -> None:
        """Test insert_one_row function.
        """
        sql = """CREATE TABLE IF NOT EXISTS test (
            id integer PRIMARY KEY,
            name text NOT NULL,
            age integer
        );"""
        db.create_table(self.db_file, sql)
        sql = """INSERT INTO test (id, name, age) VALUES (?, ?, ?);"""
        data_in = (1, "John", 20)
        db.insert_one_row(self.db_file, sql, data_in)
        # insert again
        self.assertRaises(db.sqlite3.IntegrityError,
                          db.insert_one_row, self.db_file, sql, data_in)

    def test_insert_many_rows(self) -> None:
        """Test insert_many_rows function.
        """
        sql = """CREATE TABLE IF NOT EXISTS test (
            id integer PRIMARY KEY,
            name text NOT NULL,
            age integer
        );"""
        db.create_table(self.db_file, sql)
        sql = """INSERT INTO test (name, age) VALUES (?, ?);"""
        data_in = [("John", 20), ("Jane", 25)]
        db.insert_many_rows(self.db_file, sql, data_in)
        conn = db.create_connection(self.db_file)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM test")
        data_out = cursor.fetchall()
        self.assertEqual(data_in, [row[1:] for row in data_out])
        db.close_connection(conn)

    def test_insert_many_rows_error(self) -> None:
        """Test insert_many_rows function.
        """
        sql = """CREATE TABLE IF NOT EXISTS test (
            id integer PRIMARY KEY,
            name text NOT NULL,
            age integer
        );"""
        db.create_table(self.db_file, sql)
        sql = """INSERT INTO test (id, name, age) VALUES (?, ?, ?);"""
        data_in = [(1, "John", 20), (2, "Jane", 25)]
        db.insert_many_rows(self.db_file, sql, data_in)
        # insert again
        self.assertRaises(db.sqlite3.IntegrityError,
                          db.insert_many_rows, self.db_file, sql, data_in)

    def test_select_one_row(self) -> None:
        """Test select_one_row function.
        """
        sql = """CREATE TABLE IF NOT EXISTS test (
            id integer PRIMARY KEY,
            name text NOT NULL,
            age integer
        );"""
        db.create_table(self.db_file, sql)
        sql = """INSERT INTO test (name, age) VALUES (?, ?);"""
        data_in = [("John", 20), ("Jane", 25)]
        db.insert_many_rows(self.db_file, sql, data_in)
        sql = """SELECT * FROM test WHERE id = ?;"""
        data_out = db.select_one_row(self.db_file, sql, (1,))
        self.assertEqual(data_in[0], data_out[1:])

    def test_select_many_rows(self) -> None:
        """Test select_many_rows function.
        """
        sql = """CREATE TABLE IF NOT EXISTS test (
            id integer PRIMARY KEY,
            name text NOT NULL,
            age integer
        );"""
        db.create_table(self.db_file, sql)
        sql = """INSERT INTO test (name, age) VALUES (?, ?);"""
        data_in = [("John", 20), ("Jane", 25)]
        db.insert_many_rows(self.db_file, sql, data_in)
        sql = """SELECT * FROM test;"""
        data_out = db.select_many_rows(self.db_file, sql, ())
        self.assertEqual(data_in, [row[1:] for row in data_out])

    def test_update_one_row(self) -> None:
        """Test update_one_row function.
        """
        sql = """CREATE TABLE IF NOT EXISTS test (
            id integer PRIMARY KEY,
            name text NOT NULL,
            age integer
        );"""
        db.create_table(self.db_file, sql)
        sql = """INSERT INTO test (name, age) VALUES (?, ?);"""
        data_in_list = [("John", 20), ("Jane", 25)]
        db.insert_many_rows(self.db_file, sql, data_in_list)
        sql = """UPDATE test SET name = ? WHERE id = ?;"""
        data_in_tuple = ("John Doe", 1)
        db.update(self.db_file, sql, data_in_tuple)
        sql = """SELECT * FROM test WHERE id = ?;"""
        data_out = db.select_one_row(self.db_file, sql, (1,))
        self.assertEqual(("John Doe", 20), data_out[1:])

    def test_update_many_rows(self) -> None:
        """Test update_many_rows function.
        """
        sql = """CREATE TABLE IF NOT EXISTS test (
            id integer PRIMARY KEY,
            name text NOT NULL,
            age integer
        );"""
        db.create_table(self.db_file, sql)
        sql = """INSERT INTO test (name, age) VALUES (?, ?);"""
        data_in_list = [("John", 20), ("Jane", 25)]
        db.insert_many_rows(self.db_file, sql, data_in_list)
        sql = """UPDATE test SET name = ? WHERE age <= ?;"""
        data_in: Tuple[str, int] = ("John Doe", 25)
        db.update(self.db_file, sql, data_in)
        sql = """SELECT * FROM test;"""
        data_out = db.select_many_rows(self.db_file, sql, ())
        self.assertEqual([("John Doe", 20), ("John Doe", 25)],
                         [row[1:] for row in data_out])

    def test_delete_one_row(self) -> None:
        """Test delete_one_row function.
        """
        sql = """CREATE TABLE IF NOT EXISTS test (
            id integer PRIMARY KEY,
            name text NOT NULL,
            age integer
        );"""
        db.create_table(self.db_file, sql)
        sql = """INSERT INTO test (name, age) VALUES (?, ?);"""
        data_in = [("John", 20), ("Jane", 25)]
        db.insert_many_rows(self.db_file, sql, data_in)
        sql = """DELETE FROM test WHERE id = ?;"""
        db.delete(self.db_file, sql, (1,))
        sql = """SELECT * FROM test;"""
        data_out = db.select_many_rows(self.db_file, sql, ())
        self.assertEqual([("Jane", 25)], [row[1:] for row in data_out])
