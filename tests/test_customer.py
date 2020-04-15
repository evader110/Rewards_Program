# Created on 4/14/2019
# Created by Ethan O'Dell
# Email: eodellm@gmail.com

from src.customer import Customer
from pytest import raises

def test_add_points():
    test_customer = Customer(1, 'Ethan')
    
    test_customer.add_points(-3)
    assert test_customer.reward_points == 0
    
    test_customer.add_points(0.0000)
    assert test_customer.reward_points == 0

    test_customer.add_points(153.242424)
    assert test_customer.reward_points == 156
    
    test_customer.add_points(56)
    assert test_customer.reward_points == 162

    test_customer.add_points(1000)
    assert test_customer.reward_points == 2012

    test_customer.add_points(23)
    assert test_customer.reward_points == 2012

    with raises(TypeError):
        test_customer.add_points('\n')