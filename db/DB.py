import psycopg2
import psycopg2.extras

# декоратор для серилизации ответа в словарь (обьект)
def toDict(func):
    def wrapper(*args, **kwargs):
        rows = func(*args, **kwargs)
        arr = []
        for row in rows:
            d = {}
            for key in row:
                d[key] = row[key]
            arr.append(d)
        return arr
    return wrapper

class DB:
    def __init__(self):
        try:
            self.connect = psycopg2.connect(
                database="vm31-db",
                user="vm31-user",
                password="12345678",
                host="127.0.0.1",
                port="5433"
            )
            self.cursor = self.connect.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            print('Я подключился')
        except ValueError as err:
            print("Все сдохло", err)

    def __del__(self):
        self.cursor.close()
        self.connect.close()

    @toDict
    def getAllUsers(self):
        self.cursor.execute("SELECT id, name, login FROM users")
        return self.cursor.fetchall()

    def getAllTestResults(self):
        query = "SELECT id, test, result, date FROM tests ORDER BY date"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def insertTestResult(self, name, result):
        query = "INSERT INTO tests (test, result, date) VALUES (%s, %s, now())"
        self.cursor.execute(query, (name, result))
        self.connect.commit()
        return True