import sqlite3



def initiate_db():
    connection = sqlite3.connect('not_telegram.db')
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    ''')
    # cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
    #                ("Zn", "Цинк+Витамин C", "100"))
    # cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
    #                ("Mg", "Магний хелат", "200"))
    # cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
    #                ("Cr", "Хром хелат", "300"))
    # cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
    #                ("D3", "Витамин D3", "400"))
    connection.commit()
    connection.close()

def get_all_products():
    connection = sqlite3.connect('not_telegram.db')
    cursor = connection.cursor()

    cursor.execute("SELECT id, title, description, price FROM Products")
    products = cursor.fetchall()

    connection.commit()
    connection.close()
    return products

initiate_db()
