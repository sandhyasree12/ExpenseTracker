from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from database import add_expense, add_income, clear_data, fix_expenses_table, fix_incomes_table

app = Flask(__name__)

# Clear all data and fix tables on app startup
clear_data()
fix_expenses_table()
fix_incomes_table()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_expense', methods=['POST'])
def add_expense_route():
    category = request.form['category']
    amount = float(request.form['amount'])
    date = request.form['date'] or None  # Default to None if no date is entered

    add_expense(category, amount, date)
    return redirect(url_for('index'))

@app.route('/add_income', methods=['POST'])
def add_income_route():
    source = request.form['source']
    amount = float(request.form['amount'])
    date = request.form['date'] or None  # Default to None if no date is entered

    add_income(source, amount, date)
    return redirect(url_for('index'))

@app.route('/analytics')
def analytics():
    conn = sqlite3.connect('finance.db')
    cursor = conn.cursor()

    # Get total expenses by category
    cursor.execute('''
        SELECT category, SUM(amount) FROM expenses GROUP BY category
    ''')
    expense_data = cursor.fetchall()

    # Get total income
    cursor.execute('''
        SELECT SUM(amount) FROM incomes
    ''')
    total_income = cursor.fetchone()[0] or 0

    # Get total expenses
    cursor.execute('''
        SELECT SUM(amount) FROM expenses
    ''')
    total_expenses = cursor.fetchone()[0] or 0

    # Calculate remaining income
    remaining_income = total_income - total_expenses

    conn.close()

    return render_template('analytics.html', expense_data=expense_data, total_income=total_income, total_expenses=total_expenses, remaining_income=remaining_income)

if __name__ == '__main__':
    app.run(debug=True)
