# Created on 4/13/2020
# Created by Ethan O'Dell
# Email: eodellm@gmail.com

from .customer import Customer
from random import randint, randrange
import decimal


def get_random_customer_name():
    with open('first_names.txt') as names:
        return names.read().split('\n')[randint(0, 4944)].strip()

# Generate list of n customers
def generate_customers(n):
    with open('customer_list', 'w') as customers:
        for i in range(1,n+1):
            customers.write('%d, %s\n' % (i, get_random_customer_name()))

# Generate list of t transactions for n customers
def generate_transactions(t, n):
    with open('transactions', 'w') as transactions:
        for _ in range(1, t+1):
            cid = randint(1,n)
            # Data should come from the last three months ie. Jan-Mar
            month = randint(1,3)
            day = 1
            if month == 2: # February is a special case
                day = randint(1,29) # 2020 is a leap year
            else:
                day = randint(1,31) # Jan and March
            date = '%d/%d/2020' % (month, day)
            # Create a decimal object to create a transaction amount between $1 and $1000 
            purchase_amount = float(decimal.Decimal(randrange(100, 100000)) / 100)
            transactions.write('%d, %s, %f\n' % (cid, date, purchase_amount))

def generate_database(t, n):
    generate_customers(n)
    generate_transactions(t, n)
