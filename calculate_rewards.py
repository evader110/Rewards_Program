# Created on 4/13/2019
# Created by Ethan O'Dell
# Email: eodellm@gmail.com

from classes.customer import Customer
import pandas as pd
customers = {}
with open('customer_list', 'r') as customer_list:
    cid, name = customer_list.readline().split(', ')
    customers[int(cid)] = Customer(cid,name)
print(customers)
