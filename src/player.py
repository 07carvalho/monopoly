import random


class Player:
    """This class represents a Monopoly player"""
    def __init__(self, number, balance, position, properties):
        self.number = number
        self._balance = balance
        self._position = position
        self._properties = properties

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
    def properties(self):
        """get player's properties"""
        return self._properties

    @properties.setter
    def properties(self, house):
        """set a new house"""
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
