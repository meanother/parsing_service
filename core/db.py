import os
from typing import Dict, List, Tuple

import sqlite3

conn = sqlite3.connect(os.path.join("db", "parsing.db"))
cursor = conn.cursor()


def _init_db():
    """Инициализирует БД"""
    with open("../sql/create_table.sql", "r") as f:
        sql = f.read()
    cursor.executescript(sql)
    conn.commit()


def check_db_exists():
    """Проверяет, инициализирована ли БД, если нет — инициализирует"""
    cursor.execute("SELECT name FROM sqlite_master "
                   "WHERE type='table' AND name='pulse_parser'")
    table_exists = cursor.fetchall()
    if table_exists:
        return
    _init_db()


def check_create_tables():
    """Проверяет, инициализирована ли БД, если нет — инициализирует"""
    cursor.execute("SELECT count(*) FROM sqlite_master "
                   "WHERE type='table'")
    table_exists = cursor.fetchall()[0][0]
    if int(table_exists) == 2:
        return
    _init_db()


def insert(table: str, column_values: Dict):
    columns = ', '.join(column_values.keys())
    values = [tuple(column_values.values())]
    placeholders = ", ".join("?" * len(column_values.keys()))
    cursor.executemany(
        f"INSERT INTO {table} "
        f"({columns}) "
        f"VALUES ({placeholders})",
        values)
    conn.commit()


# check_db_exists()
check_create_tables()