def create_connection():
    import sqlite3
    from sqlite3 import Error

    conn = None
    try:
        conn = sqlite3.connect('expenses.db')
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return conn