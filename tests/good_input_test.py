# Created on 4/13/2019
# Created by Ethan O'Dell
# Email: eodellm@gmail.com

import pytest
from classes.calculate_rewards import calculate_rewards
from pprint import pprint

# TODO: Write unit test just for calculate_rewards()
def test_good_input():
    # 1: 0, 544, 30, 19 ->
    # 2: 15, 200 -> 250, 412 -> 674  
    # 3: 90, 198, 0
    customers = calculate_rewards('tests/good_input_test_customer_list', 'tests/good_input_test_transaction_list')
    answers = [593, 674, 288]
    for cid in customers:
        assert customers[cid].reward_points == answers[cid-1]