import sqlite3
import argparse
from datetime import datetime
from expenses import Expense


con = sqlite3.connect("expenses.db")

cur = con.cursor()


cur.execute("""CREATE TABLE IF NOT EXISTS expenses(
                category text,
                amount int,
                date text
            )""")


def insert_expense(expense):
    with con:
        cur.execute("INSERT INTO expenses VALUES (:category, :amount, :date)", 
        {"category": expense.category, "amount": expense.amount, "date": expense.date})


def remove_expense(expense):
    with con:
        cur.execute("DELETE from expenses WHERE id = :id AND date = :date",
        {"id": expense.id, "date": expense.date})



cur.execute("SELECT * FROM expenses")
print(cur.fetchall())

con.commit()
con.close()

"""
Parser CLI
"""

parser = argparse.ArgumentParser(prog="My Expense Tracker")

parser.add_argument('--version', action='version', version='%(prog)s 2.0')
parser.add_argument("amount", help="Enter the amount in dollars",
                    type=int)
parser.add_argument("-d", "--date", type=str, default=datetime.today().strftime("%d-%m-%Y"), 
                    help="Enter the date in DD/MM/YYYY format")
parser.add_argument("-c", "--category", type=str, default="Others", 
                    help="Enter the category")

args = parser.parse_args()

exp = Expense(args.category, args.amount, args.date)
print(exp)