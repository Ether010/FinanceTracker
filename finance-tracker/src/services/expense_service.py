from database.connection import create_connection
from database.models import Expense

def fetch_expenses():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()
    expenses = []
    for row in rows:
        expenses.append(Expense(*row))
    connection.close()
    return expenses

def create_expense(amount, category, date, description):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO expenses (amount, category, date, description) VALUES (?, ?, ?, ?)",
                   (amount, category, date, description))
    connection.commit()
    connection.close()

def remove_expense(expense_id):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
    connection.commit()
    connection.close()