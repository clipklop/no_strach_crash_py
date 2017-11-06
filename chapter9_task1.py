# ***
#
# ***


from random import randint


class Die():
    """ A class for rolling a six sided cube. """
    def __init__(self):
        self.sides = 6
        self.attempts = 10

    def roll_die(self):
        """ Method for random int choice. """
        roll = randint(1, self.sides)
        return roll

    def make_roll(self):
        """ A methond for print @self.attempts times. """
        for _ in range(0, self.attempts):
            print(self.roll_die(), end=' ')

            if self.attempts == 0:
                print("")


class DieTen(Die):
    """ A ckass for rolling a ten sided cube. """
    def __init__(self):
        super().__init__()
        self.sides = 10


class DieTwenty(Die):
    """ A ckass for rolling a twenty sided cube. """
    def __init__(self):
        super().__init__()
        self.sides = 20


rolling_deep_6 = Die()
rolling_deep_6.make_roll()
print("")
rolling_deep_10 = DieTen()
rolling_deep_10.make_roll()
print("")
rolling_deep_20 = DieTwenty()
rolling_deep_20.make_roll()