# This file is used to save expenses

import json

def save_expenses(expenses):

     with open("expenses.json", "w") as file:
         json.dump(expenses, file, indent=4)

     print("Expenses saved sucessfully!")
