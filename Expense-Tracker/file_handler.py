# This file is used to save expenses

import json
import csv

def save_expenses(expenses):

        with open("expenses.json", "w") as file:
           json.dump(expenses, file, indent=4)

        print("Expenses saved sucessfully!")


def load_expenses():

    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)

        print("Expenses load successfully!")
        return expenses

    except FileNotFoundError:
        print("No saved expenses found.")
        return []    


# Export expenses to a CSV file

def export_to_csv(expenses):

    with open("expenses.csv", "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(["Date", "Category", "Amount", "Description"])

        for expense in expenses:
            writer.writerow([
                expense["date"],
                expense["category"],
                expense["amount"],
                expense["description"]
            ])

    print("Expenses exported to CSV successfully!")
