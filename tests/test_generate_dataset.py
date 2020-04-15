# Created on 4/14/2020
# Created by Ethan O'Dell
# Email: eodellm@gmail.com

from src.generate_dataset import get_random_customer_name, generate_customers, generate_transactions, generate_database
import pytest

def test_get_random_customer_name():
    name = get_random_customer_name()
    assert isinstance(name, str) and name is not ''

def test_generate_customers_10():
    # Empty the file 
    with open('customer_list', 'w') as customer_file:
        customer_file.write('')
    
    generate_customers(10)

    with open('customer_list') as customer_file:
        count = 0
        for _ in customer_file:
            count += 1
        assert count == 10
    
def test_generate_customers_1():
    # Empty the file 
    with open('customer_list', 'w') as customer_file:
        customer_file.write('')
    
    generate_customers(1)

    with open('customer_list') as customer_file:
        count = 0
        for _ in customer_file:
            count += 1
        assert count == 1

def test_generate_customers_0():
    # Empty the file 
    with open('customer_list', 'w') as customer_file:
        customer_file.write('')
    
    generate_customers(0)

    with open('customer_list') as customer_file:
        assert customer_file.read() == ''

def test_generate_transactions():
    # Empty the file 
    with open('transactions', 'w') as transaction_file:
        transaction_file.write('')
    
    generate_transactions(10, 5)

    with open('transactions') as transaction_file:
        count = 0
        for _ in transaction_file:
            count += 1
        assert count == 10

def test_generate_transactions_empty():
    # Empty the file 
    with open('transactions', 'w') as transaction_file:
        transaction_file.write('')
    
    generate_transactions(0, 5)

    with open('transactions') as transaction_file:
        assert transaction_file.read() == ''

def test_generate_database():
    # Empty the file 
    with open('customer_list', 'w') as transaction_file:
        transaction_file.write('')
    # Empty the file 
    with open('transactions', 'w') as transaction_file:
        transaction_file.write('')
    
    generate_database(10, 2)

    with open('customer_list') as customer_file:
        count = 0
        for _ in customer_file:
            count += 1
        assert count == 2

    with open('transactions') as transaction_file:
        count = 0
        for _ in transaction_file:
            count += 1
        assert count == 10
