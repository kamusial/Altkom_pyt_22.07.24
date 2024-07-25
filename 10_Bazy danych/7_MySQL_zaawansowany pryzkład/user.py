from sqlalchemy.engine import row

from database import Database

class User:
    def __init__(self, db, name=None, age=None, user_id=None):
        self.db = db
        self.id = user_id
        self.name = name
        self.age = age

    def save(self):
        if self.id is None:
            self.db.execute(
                'INSERT INTO users (name, age) VALUES (%s, %s)',
                (self.name, self.age)
            )
            self.db.commit()
            self.id = self.db.lastrowid
        else:
            self.db.execute(
                'UPDATE users SET name = %s, age = %s WHERE id = %s',
                (self.name, self.age, self.id)
            )
            self.db.commit()

    def delete(self):
        if self.id is not None:
            self.db.execute('DELETE FROM users WHERE id = %s', (self.id,))
            self.db.commit()
            self.id = None

    @staticmethod
    def get(db, user_id):
        db.execute('SELECT id, name, age FROM users WHERE id = %s', (user_id,))
        result = db.fetchone()
        if result:
            return User(db, name=result[1], age=result[2], user_id=result[0])
        return None

    @staticmethod
    def all(db):
        db.execute('SELECT id, name, age FROM users')
        results = db.fetchall()
        return [User(db, name=row[1], age=row[2], user_id=row[0]) for row in results]