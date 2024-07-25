import sqlite3

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER)
        ''')
        self.conn.commit()

    def add_user(self, name, age):
        self.cursor.execute('''
        INSERT INTO users (name, age) VALUES (?, ?)
        ''', (name, age))
        self.conn.commit()

    def update_user(self, user_id, name=None, age=None):
        if name is not None:
            self.cursor.execute('''
                UPDATE users SET name = ?, WHERE id = ?
                ''', (name, user_id))
        if age is not None:
            self.cursor.execute('''
                UPDATE users SET age = ?, WHERE id = ?
                ''', (age, user_id))
        self.conn.commit()
