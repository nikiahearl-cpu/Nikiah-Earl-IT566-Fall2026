# My Expense Tracker

from expense import create_expense

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

        expenses.append(expense) 
        
        print("Expense added!")

    elif choice == "2":

        if len(expenses) == 0:
            print("No expenses have been added yet.")

        else:
            print("\nYour Expenses:")

            for expense in expenses:
                print(expense)

    elif choice == "3":

        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
