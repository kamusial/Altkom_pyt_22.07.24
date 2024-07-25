import sqlite3

def read_entire_database(db_name):
    # Nawiązanie połączenia z bazą danych
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Pobranie listy tabel
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print(tables)
    # Dla każdej tabeli odczytanie wszystkich danych
    database_content = {}
    for table in tables:
        table_name = table[0]
        cursor.execute(f'SELECT * FROM {table_name}''')
        rows = cursor.fetchall()

        # Pobranie nazw kolumn
        cursor.execute(f"PRAGMA table_info({table_name})")
        columns = [column[1] for column in cursor.fetchall()]

        # Przechowywanie danych w słowniku
        database_content[table_name] = {
            "columns": columns,
            "rows": rows
        }

    # Zamknięcie kursora i połączenia
    cursor.close()
    conn.close()

    return database_content

# Odczytanie całej bazy danych
db_content = read_entire_database('results.db')

# Wyświetlenie zawartości bazy danych
for table, content in db_content.items():
    print(f"Table: {table}")
    print("Columns:", content["columns"])
    print("Rows:")
    for row in content["rows"]:
        print(row)
    print()
