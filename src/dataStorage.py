import sqlite3

from src.amazonFetcher import AmazonProduct

class DataStorage:
    def __init__(self, db_path:str = "database.db"):
        self.db_path = db_path
        self.conn = None
    
    def _connect(self):
        if self.conn is None:
            self.conn = sqlite3.connect(self.db_path)
            self.conn.row_factory = sqlite3.Row
            self.conn.execute("PRAGMA foreign_keys = 1")

    def _close(self):
        if self.conn:
            self.conn.close()
            self.conn = None

    def add_product(self, product: AmazonProduct):
        """Insert a new entry in the db.
        
        Works both to add a new item or simply insert a price into history
        """
        self._connect()
        cursor = self.conn.cursor()

        #Insert in items if not exists
        cursor.execute("""
            INSERT OR IGNORE INTO items (amazon_asin, name, url)
            VALUES (?,?,?)
        """,(product.asin, product.name, product.url))

        #Retrieve item_id
        cursor.execute("""
            SELECT id FROM items WHERE amazon_asin = ?
        """, (product.asin,))
        item_id = cursor.fetchone()["id"]

        #Insert into price history
        cursor.execute("""
            INSERT INTO price_history (item_id, price, currency, checked_at)
            VALUES (?, ?, ?, ?)
        """,(item_id, product.price, product.currency, product.datetime))

        self.conn.commit()
    
    def delete_by_asin(self, asin:str):
        """Delete an item and its entire price history"""
        
        self._connect()
        cursor = self.conn.cursor()

        cursor.execute("""
            DELETE FROM items
            WHERE amazon_asin = ?
        """,(asin,))

        self.conn.commit()

    def delete_by_id(self, id:int):
        """Delete and item and its entire price history using its id"""

        self._connect()
        cursor = self.conn.cursor()

        cursor.execute("""
            DELETE FROM items
            WHERE id = ?
        """,(id,))