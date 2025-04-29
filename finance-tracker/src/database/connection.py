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

def create_table(conn):
    create_expenses_table = """
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount REAL NOT NULL,
        category TEXT NOT NULL,
        date TEXT NOT NULL,
        description TEXT,
        user_id INTEGER NOT NULL
    );
    """

    try:
        cursor = conn.cursor()
        cursor.execute(create_expenses_table)
        print("Expenses table created successfully")
    except Error as e:
        print(f"The error '{e}' occurred")