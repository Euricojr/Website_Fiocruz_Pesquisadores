"""
database.py - SQLite database setup and connection management.
Uses native sqlite3 to manage the users table for authentication.
"""
import sqlite3
import os

DB_DIR = "data"
DB_PATH = os.path.join(DB_DIR, "users.db")

def init_db():
    """
    Initializes the SQLite database.
    Creates the data directory if it doesn't exist and sets up the users table.
    """
    os.makedirs(DB_DIR, exist_ok=True)
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            hashed_password TEXT NOT NULL,
            name TEXT,
            is_active BOOLEAN DEFAULT 1
        )
    ''')
    
    conn.commit()
    conn.close()

def get_db_connection():
    """
    Returns a new connection to the SQLite database.
    Should be used with context managers or closed explicitly.
    """
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn
