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
                UPDATE users SET name = ? WHERE id = ?
                ''', (name, user_id))
        if age is not None:
            self.cursor.execute('''
                UPDATE users SET age = ? WHERE id = ?
                ''', (age, user_id))
        self.conn.commit()

    def delete_user(self, user_id):
        self.cursor.execute('''
        DELETE FROM users WHERE id = ?
        ''', (user_id,))
        self.conn.commit()

    def get_users(self):
        self.cursor.execute('SELECT * FROM users')
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()

class UserManager:
    def __init__(self, db_name):
        self.db = Database(db_name)
        self.db.create_table()

    def add_user(self, name, age):
        self.db.add_user(name, age)

    def update_user(self, user_id, name=None, age=None):
        self.db.update_user(user_id, name, age)

    def delete_user(self, user_id):
        self.db.delete_user(user_id)

    def list_users(self):
        users = self.db.get_users()
        for user in users:
            print(user)

    def close(self):
        self.db.close()

if __name__ == '__main__':
    user_manager = UserManager('example.db')

    # dodawanie użytkowników
    user_manager.add_user('Kamil', 36)
    user_manager.add_user('Basia', 20)

    # Wyświetl użytkowników
    print('All users:')
    user_manager.list_users()

    # Aktualizacja użytkownika
    user_manager.update_user(1, 'Marian')

    # Wyświetl użytkowników
    print('All users:')
    user_manager.list_users()

    # Usunięcie uzytkownika
    user_manager.delete_user(3)

    # Wyświetl użytkowników
    print('All users:')
    user_manager.list_users()

    user_manager.close()
