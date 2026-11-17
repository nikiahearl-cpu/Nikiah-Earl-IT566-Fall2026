#Expense Manager
#This file helps manage all expenses

def add_expense(expenses, expense):
     expenses.append(expense) 
     print("Expense added!")


def view_expenses(expenses):
     if len(expenses) == 0:
         print("No expenses have been added yet.")
     else:
         print("\nYour Expenses:")
         for expense in expenses:
            print(expense)

# Filter expenses by category

def filter_by_category(expenses):

    category = input("Enter category to search: ")

    print("\nMatching Expenses:")

    for expense in expenses:

        if expense["category"].lower() == category.lower():
            print(expense)

# Filter expenses by date range

def filter_by_date(expenses):

    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")

    print("\nExpenses Within Date Range:")

    for expense in expenses:

        if start_date <= expense["date"] <= end_date:
            print(expense)
