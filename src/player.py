import random


class Player:
    """This class represents a Monopoly player"""
    def __init__(self, number, balance, position, actual_round, properties):
        self._number = number
        self._balance = balance
        self._position = position
        self._actual_round = actual_round
        self._properties = properties

    def __str__(self):
        return self._number


    @property
    def number(self):
        """get number"""
        return self._number

    @number.setter
    def number(self, number):
        """set number"""
        self._number = number

    @property
    def balance(self):
        """get balance"""
        return self._balance

    @balance.setter
    def balance(self, cash):
        """set balance"""
        self._balance = self._balance + cash

    @property
    def position(self):
        """get position"""
        return self._position

    @position.setter
    def position(self, position):
        """set position"""
        self._position = position

    @property
    def actual_round(self):
        """get player's actual round"""
        return self._actual_round

    @actual_round.setter
    def actual_round(self, actual_round):
        """set actual round"""
        self._actual_round = actual_round

    @property
    def properties(self):
        """get player's properties"""
        return self._properties

    @properties.setter
    def properties(self, house):
        """set a new house to properties list"""
        self._properties.append(house)

    def is_playing(self):
        """check if is playing (balance higher or equal than 0)"""
        return self.balance >= 0

    def roll_the_dice(self):
        """generate a random number as a dice"""
        return random.randint(1, 6)

    def walk(self, dice_number):
        """go to a new position according to a dice number"""
        self.position = self.position + dice_number
