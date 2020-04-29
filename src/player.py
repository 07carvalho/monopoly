import random


class Player:
    """This class represents a Monopoly player"""
    def __init__(self, number, balance, position, actual_round, properties, strategy, is_playing=True):
        self._number = number
        self._balance = balance
        self._position = position
        self._actual_round = actual_round
        self._properties = properties
        self._strategy = strategy
        self._is_playing = is_playing

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
    def properties(self, prop):
        """set a new house to properties list"""
        self._properties.append(prop)

    @property
    def is_playing(self):
        """get playting status"""
        return self._is_playing

    @is_playing.setter
    def is_playing(self, status):
        """set is playting status"""
        self._is_playing = status

    def roll_the_dice(self):
        """generate a random number as a dice"""
        dice_number = random.randint(1, 6)
        print('Player {0} rolled the dice and get {1}'.format(
                    self.number, dice_number))
        return dice_number

    def walk(self, board, dice_number):
        """go to a new position according to a dice number"""
        new_position = self.position + dice_number
        if new_position > board.total_properties:
            self.position = dice_number - (board.total_properties - self.position)
            self.actual_round = self.actual_round + 1
            self.balance = board._prize_for_completing_round

            if self.actual_round > board.actual_round:
                board.actual_round = self.actual_round

            print('Player {0} is in the round {1} with balance {2}'.format(
                        self.number, self.actual_round, self.balance))
        else:
            self.position = new_position
        return self.position

    def has_cash_to_operation(self, value):
        return (self.balance - value) >= 0

    def buy_property(self, prop):
        """buy a property if has cash"""
        if self.has_cash_to_operation(prop.sale_price):
            self.balance = -prop.sale_price
            prop.owner = self
            print('Player {0} bought the Property {1} and now has {2}'.format(
                        self.number, prop.position, self.balance))
            self.properties.append(prop)
            return True
        return False


    def pay_rent_to_owner(self, prop):
        """player pays rent to the property owner"""
        if self.has_cash_to_operation(prop.sale_price):
            rental_price = prop.rental_price
            self.balance = rental_price*(-1)
            prop.owner.balance = rental_price
            print('Player {0} paid {1} for rent to Player {2} and now has {3}'.format(
                        self.number, rental_price, prop.owner.number, self.balance))
            return True
        return False


    def loose_all(self):
        """verify player balance and if """
        # if not self.is_playing():
        for prop in self._properties:
            prop.owner = None
        self._properties = []
        self._is_playing = False
        print('Player {0} is out of cash and out of game!'.format(self.number))
