import pandas as pd
import numpy as np 
import random
from faker import Faker
from datetime import timedelta  

# Configure faker to generate realistic data 
faker = Faker()
Faker.seed(4321)

# Define function to generate daily transactions
def generate_transactions(customers, start_date, days):
  
  # Create empty dataframe    
  transactions = pd.DataFrame(columns=['cust_id', 'txn_date', 'amount', 'store_id', 'payment_mode']) 
  
  # Iterate through dates
  for single_date in (start_date + timedelta(n) for n in range(days)):

    # Iterate through customers
    for customer in range(customers):

      # Randomly generate transaction details   
      transactions.loc[len(transactions)] = [
        customer, 
        single_date,
        round(random.uniform(10,200),2),  
        random.randint(1,5),
        random.choice(['cash','credit','debit'])
      ]

  return transactions

# Generate 12 days transaction
transactions_data = generate_transactions(1000, faker.date_object(), 12) 

print(transactions_data.head())