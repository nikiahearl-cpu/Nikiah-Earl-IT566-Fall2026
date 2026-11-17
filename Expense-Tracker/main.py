# My Expense Tracker

from expense import create_expense
from expense_manager import add_expense, view_expenses, filter_by_category
from file_handler import save_expenses, load_expenses

expenses = load_expenses()

# This program will help me keep track of expenses 

print("My Expense Tracker")

while True:

    print("\nMy Expense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Save Expenses") 
    print("4. Filter by Category")
    print("5. Exit")

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
        save_expenses(expenses)
    
    elif choice == "4":
        filter_by_category(expenses)

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
