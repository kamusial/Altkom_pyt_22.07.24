import mysql.connector

class Database:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conn = None
        self.cursor = None

    def connect(self):
        self.conn = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.conn.cursor()
        print("połączono")

    def close(self):
        if self.conn:
            self.cursor.close()
            self.conn.close()

    def commit(self):
        if self.conn:
            self.conn.commit()

