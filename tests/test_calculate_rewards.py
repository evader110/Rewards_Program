# Created on 4/13/2019
# Created by Ethan O'Dell
# Email: eodellm@gmail.com

from src.calculate_rewards import calculate_rewards
from pytest import raises

def test_good_transaction_input():
    customers = calculate_rewards('tests/good_input_test_customer_list', 'tests/good_input_test_transaction_list')
    answers = [593, 939, 288]

    assert customers[1].reward_points == answers[0]
    assert customers[2].reward_points == answers[1]
    assert customers[3].reward_points == answers[2]

def test_bad_transaction_input():
    with raises(ValueError):
        calculate_rewards('tests/bad_transaction_test_customer_list', 'tests/bad_transaction_test_transaction_list')
