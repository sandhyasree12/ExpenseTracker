import sqlite3
from datetime import datetime

# Function to clear all data from expenses and incomes tables
def clear_data():
    conn = sqlite3.connect('finance.db')
    cursor = conn.cursor()

    # Delete all entries in the expenses and incomes tables
    cursor.execute('DELETE FROM expenses')
    cursor.execute('DELETE FROM incomes')

    conn.commit()
    conn.close()

# Function to fix the expenses table structure if needed
def fix_expenses_table():
    conn = sqlite3.connect('finance.db')
    cursor = conn.cursor()

    # Create expenses table if not exists
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT,
            amount REAL,
            date TEXT
        )
    ''')

    conn.commit()
    conn.close()

# Function to fix the incomes table structure if needed
def fix_incomes_table():
    conn = sqlite3.connect('finance.db')
    cursor = conn.cursor()

    # Create incomes table if not exists
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS incomes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            source TEXT,
            amount REAL,
            date TEXT
        )
    ''')

    conn.commit()
    conn.close()

# Function to add expense
def add_expense(category, amount, date=None):
    conn = sqlite3.connect('finance.db')
    cursor = conn.cursor()

    # Make sure date is in the correct format (YYYY-MM-DD)
    if not date:
        date = datetime.now().strftime("%Y-%m-%d")  # Default to current date if not provided

    # Insert the expense into the expenses table
    cursor.execute('''
        INSERT INTO expenses (category, amount, date) VALUES (?, ?, ?)
    ''', (category, amount, date))

    conn.commit()
    conn.close()

# Function to add income
def add_income(source, amount, date=None):
    conn = sqlite3.connect('finance.db')
    cursor = conn.cursor()

    # Make sure date is in the correct format (YYYY-MM-DD)
    if not date:
        date = datetime.now().strftime("%Y-%m-%d")  # Default to current date if not provided

    # Insert the income into the incomes table
    cursor.execute('''
        INSERT INTO incomes (source, amount, date) VALUES (?, ?, ?)
    ''', (source, amount, date))

    conn.commit()
    conn.close()

# Clear data when the app starts to ensure a clean slate
clear_data()

# Fix the tables' structure (if necessary)
fix_expenses_table()
fix_incomes_table()
