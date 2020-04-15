# Created on 4/14/2020
# Created by Ethan O'Dell
# Email: eodellm@gmail.com

from src.calculate_rewards import calculate_rewards
from src.generate_dataset import generate_database
from pprint import pprint

generate_database(100000, 1000)
pprint(calculate_rewards('customer_list', 'transactions'))
