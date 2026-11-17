# My Expense Tracker

from expense import create_expense
from expense_manager import add_expense, view_expenses

expenses = []

# This program will help me keep track of expenses 

print("My Expense Tracker")

while True:

    print("\nMy Expense Tracker")
    print("1. Add Expense")
    print("2. View Expenses") 
    print("3. Exit")

    choice = input("Enter your choice: ")

    print("You picked:", choice)

    if choice == "1":

        date = input("Enter the date (YYYY-MM-DD): ")
        category = input("Enter the category: ")
        amount = input("Enter the amount: ")
        description = input("Enter a description: ")

        expense = create_expense(date, category, amount, description)

        add_expense(expenses, expense)

    elif choice == "2":
        view_expenses(expenses)

    elif choice == "3":

        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
