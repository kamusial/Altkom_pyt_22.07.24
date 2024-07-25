import sqlite3

conn = sqlite3.connect('test.db')
c = conn.cursor()

# Tworzenie tabeli
c.execute('''
            CREATE TABLE IF NOT EXISTS users
            (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)
            ''')

c.execute('''
        INSERT INTO users (name, age) 
        VALUES ('Kamil', 36)
        ''')

c.execute('''
        INSERT INTO users (name, age) 
        VALUES ('Marta', 26)
        ''')

c.execute('DELETE FROM users WHERE id = 1')

# Zatwierdzanie zmian
conn.commit()

# Pobieranie danych
c.execute('SELECT * FROM users')
print(c.fetchall())

conn.close()

