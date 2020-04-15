# Created on 4/13/2020
# Created by Ethan O'Dell
# Email: eodellm@gmail.com

from .customer import Customer
from pprint import pprint

def calculate_rewards(customer_list, transactions):
    try:
        customers = {}
        with open(customer_list) as customer_list:
            for customer in customer_list:
                cid, name = customer.split(', ')
                customers[int(cid)] = Customer(int(cid),name.strip())

        with open(transactions) as transactions:
            for transaction in transactions:
                cid, _, amount = transaction.split(', ')
                customers[int(cid)].add_points(float(amount.strip()))
        return customers
    except Exception as error:
        print(error.args)
        raise error
