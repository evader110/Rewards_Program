# Created on 4/13/2020
# Created by Ethan O'Dell
# Email: eodellm@gmail.com

from dataclasses import dataclass, field

@dataclass
class Customer:
    cid: int = field(repr=False)
    name: str
    reward_points: int = field(default=0)

    # Points are calculated by 2 for each dollar above $100 and 1 for each dollar above 50
    # It is at this time not confirmed what behavior should be taken when ValueErrors occur
    # It will simply print the error as of now
    def add_points(self, amount):
        try:
            self.reward_points += 2 * max(int(amount - 100), 0) + min(max(int(amount - 50), 0), 50)
        except TypeError as error:
            raise TypeError('Bad Input was recieved', error.args)
