# My Expense Tracker

expenses = []

# This program will help me keep track of expenses 

print("My Expense Tracker")

print("1. Add Expense")
print("2. View Expenses") 
print("3. Exit")

choice = input("Enter your choice: ")

print("You picked:", choice)

if choice =="1":
	date = input("Enter the date: ")
	category = input("Enter the category: ")
	amount = input("Enter the amount: ")
	description = input("Enter a description: ")

	expense = {
		"date": date,
		"category": category,
		"amount": amount, 
		"description": description
	}

	expenses.append(expense) 

	print("Expense added!")

elif choice == "2":
	print(expenses)

elif choice == "3":
	print("Goodbye!")

else:
	print("Invalid choice")
