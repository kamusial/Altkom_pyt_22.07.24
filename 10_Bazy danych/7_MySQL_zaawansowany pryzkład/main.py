from database import Database
from user import User

def main():
    db = Database(host='localhost', user='username', password='yourpassword', database='yourdatabase')
    db.connect()

    # Tworzenie tabeli
    db.execute('''
                CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255),
                age INT
                )
             ''')
    db.commit()

    # Dodanie uzytkownika
    user1 = User(db, name='Kamil', age=36)
    user1.save()
    print(f'Dodano uzytkownika {user1.name}, {user1.age}, ID: {user1.id}')

    # pobieranie użytkownika po ID
    user2 = User.get(db, user1)
    if user2:
        print(f'przechwycono {user2.name}, {user2.age}, {user2.id}')

    # aktualizacja
    user2.age = 31
    user2.save()

    # pobrać wsyzstkich
    users = User.all(db)
    for user in users:
        print(f'{user.name}, {user.age}, {user.id}')

    # Usuwanie
    user2.delete()

    # zamykanie [połączenia
    db.close()


if __name__ == '__main__':
    main()