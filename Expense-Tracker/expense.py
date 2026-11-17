# This file is used to create expenses

def create_expense(date, category, amount, description):

     expense = {
         "date": date, 
         "category": category,
         "amount": amount,
         "description": description
     }

     return expense
