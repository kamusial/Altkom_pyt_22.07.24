import sqlite3

def read_entire_database(db_name):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    # pobranie listy tabel
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = c.fetchall()

    # dla każdej tabeli odczytanie wszystkich danych
    database_content = {}
    for table in tables:
        table_name = table[0]
        c.execute(f'SELECT * FROM {table_name}')
        rows = c.fetchall()

        # pobranie nazw kolumn
        c.execute(f'PRAGMA table_info({table_name}')
        columns = [column[1] for column in c.fetchall()]

        # przechowywanie danych w słowniku
        database_content[table_name] = {
            'columns': columns,
            'rows': rows
        }

    # zamknięcie kursora i połączenie
    c.close()
    conn.close()

    return database_content

db_content = read_entire_database('result.db')
