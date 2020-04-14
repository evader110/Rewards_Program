# Created on 4/13/2019
# Created by Ethan O'Dell
# Email: eodellm@gmail.com

from dataclasses import dataclass, field

@dataclass
class Customer:
    cid: int = field(repr=False)
    name: str
    reward_points: int = field(default=0)

    def __str__(self):
        return '%s has %d points.' % (self.name, self.reward_points)

    # Transaction -> [CID, Date, Purchase]
    # Points are calculated by 2 for each dollar above $100 and 1 for each dollar above 50
    def add_points(self, amount):
        self.reward_points += 2 * max(int(amount - 100), 0) + min(max(int(amount - 50), 0), 50)

# data = [[1, '1/11/2020', 253.23], [1, '2/3/2020', 57.00]]
# ethan = Customer(1,'Ethan')
# ethan.calculate_points(data)
# print(ethan)