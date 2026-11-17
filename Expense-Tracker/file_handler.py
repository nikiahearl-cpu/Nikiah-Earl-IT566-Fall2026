# This file is used to save expenses

import json


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
