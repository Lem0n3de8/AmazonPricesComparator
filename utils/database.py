import sqlite3

"""
##### SQL SCHEMA ####

# items table to store each unique item

CREATE TABLE IF NOT EXISTS items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amazon_asin TEXT UNIQUE NOT NULL,
    name TEXT NOT NULL,
    url TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);   

# price_history table to store the price and associated timestamp for the items

CREATE TABLE IF NOT EXISTS price_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    item_id INTEGER NOT NULL,
    price REAL NOT NULL,
    currency TEXT DEFAULT 'EUR',
    checked_at DATETIME NOT NULL,
    FOREIGN KEY (item_id) REFERENCES items(id)
);
"""

class DatabaseCreate:
    """Use this class to generate the required tables.

    Use it when you need to create the tables
    Initialize a database and create the two tables used in this project:
        - items table : to store each unique item
        - price_history table : to store the prices (one price associated with a timestamp)
    """
    def __init__(self, db_path:str = "database.db"):
        self.db_path = db_path
        self.conn = None

    def _connect(self):
        if self.conn is None:
            self.conn = sqlite3.connect(self.db_path)
            self.conn.row_factory = sqlite3.Row
            self.conn.execute("PRAGMA foreign_keys = 1")
    
    def close(self):
        if self.conn:
            self.conn.close()
            self.conn = None
    
    def create_tables(self):
        self._connect()
        cursor = self.conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                amazon_asin TEXT UNIQUE NOT NULL,
                name TEXT NOT NULL,
                url TEXT NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            );        
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS price_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                item_id INTEGER NOT NULL,
                price REAL NOT NULL,
                currency TEXT DEFAULT 'EUR',
                checked_at DATETIME NOT NULL,
                FOREIGN KEY (item_id) REFERENCES items(id),
                UNIQUE(item_id, checked_at)
            );
        """)

        self.conn.commit()