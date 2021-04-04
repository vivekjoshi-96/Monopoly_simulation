import random


class Dices:
    def __init__(self):
        self.dice1 = 0
        self.dice2 = 0

    def roll(self):
        self.dice1 = random.randint(1, 6)
        self.dice2 = random.randint(1, 6)
        x = (self.dice1, self.dice2)
        return x
