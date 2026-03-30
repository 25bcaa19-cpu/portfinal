import sqlite3
import os
from datetime import datetime

# Database file path
DB_PATH = os.path.join(os.path.dirname(__file__), 'portfolio.db')


def get_connection():
    """Create and return a database connection"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_database():
    """Initialize the database with required tables"""
    conn = get_connection()
    cursor = conn.cursor()
    
    # Create contacts table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            message TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Create stats table for visitor count
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS stats (
            id INTEGER PRIMARY KEY,
            visitor_count INTEGER DEFAULT 0
        )
    ''')
    
    # Initialize visitor count if not exists
    cursor.execute('SELECT * FROM stats WHERE id = 1')
    if cursor.fetchone() is None:
        cursor.execute('INSERT INTO stats (id, visitor_count) VALUES (1, 0)')
    
    conn.commit()
    conn.close()
    print("Database initialized successfully!")


def add_contact(name, email, message):
    """Add a new contact message to the database"""
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO contacts (name, email, message, created_at)
            VALUES (?, ?, ?, ?)
        ''', (name, email, message, datetime.now()))
        
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Error adding contact: {e}")
        return False


def get_all_contacts():
    """Retrieve all contact messages"""
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM contacts ORDER BY created_at DESC')
        contacts = cursor.fetchall()
        
        conn.close()
        return contacts
    except Exception as e:
        print(f"Error getting contacts: {e}")
        return []


def get_visitor_count():
    """Get the current visitor count"""
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute('SELECT visitor_count FROM stats WHERE id = 1')
        result = cursor.fetchone()
        
        conn.close()
        return result['visitor_count'] if result else 0
    except Exception as e:
        print(f"Error getting visitor count: {e}")
        return 0


def increment_visitor_count():
    """Increment and return the visitor count"""
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute('UPDATE stats SET visitor_count = visitor_count + 1 WHERE id = 1')
        conn.commit()
        
        cursor.execute('SELECT visitor_count FROM stats WHERE id = 1')
        result = cursor.fetchone()
        
        conn.close()
        return result['visitor_count'] if result else 0
    except Exception as e:
        print(f"Error incrementing visitor count: {e}")
        return 0


if __name__ == '__main__':
    init_database()
    print(f"Database created at: {DB_PATH}")
