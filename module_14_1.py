"""
Цель: освоить основные команды языка SQL и использовать их в коде используя SQLite3.
"""
import sqlite3

# Создайте файл базы данных not_telegram.db и подключитесь к ней, используя встроенную библиотеку sqlite3.
# Создайте объект курсора

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

# Создайте таблицу Users, если она ещё не создана. В этой таблице должны присутствовать следующие поля:
# id - целое число, первичный ключ
# username - текст (не пустой)
# email - текст (не пустой)
# age - целое число
# balance - целое число (не пустой)

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

# Заполните её 10 записями:
# User1, example1@gmail.com, 10, 1000
# User2, example2@gmail.com, 20, 1000
# User3, example3@gmail.com, 30, 1000
# ...
# User10, example10@gmail.com, 100, 1000

for i in range(1, 11):
    age = i * 10
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
                   (f"User{i}", f"{i}example@gmail.com", f"{age}", "1000"))
connection.commit()

# Обновите balance у каждой 2ой записи начиная с 1ой на 500:

for i in range(1, 11):
    if not (i + 1) % 2:
        cursor.execute("UPDATE Users SET balance = ? WHERE username = ?", (500, f"User{i}"))
connection.commit()

# Удалите каждую 3ую запись в таблице начиная с 1ой:

for i in range(0, 10, 3):
    j = i + 1
    cursor.execute("DELETE FROM Users WHERE username = ?", (f"User{j}",))
connection.commit()

# Сделайте выборку всех записей при помощи fetchall(), где возраст не равен 60
# и выведите их в консоль в следующем формате (без id):
# Имя: <username> | Почта: <email> | Возраст: <age> | Баланс: <balance>

cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != 60")
users = cursor.fetchall()
for user in users:
    print(f"Имя: {user[0]} ", f" Почта: {user[1]} ", f" Возраст: {user[2]} ", f" Баланс: {user[3]}", sep="|")

connection.commit()
connection.close()
