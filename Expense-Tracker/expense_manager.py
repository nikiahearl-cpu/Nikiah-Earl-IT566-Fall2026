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
