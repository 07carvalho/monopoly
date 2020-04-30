import random
from src.property import Property


class Player:
    """This class represents a Monopoly player"""
    def __init__(self, number: int, balance: int, position: int, actual_round: int, is_playing=True):
        self._number = number
        self._balance = balance
        self._position = position
        self._actual_round = actual_round
        self._is_playing = is_playing

    def __str__(self):
        return str(self._number)

    @property
    def number(self) -> int:
        """get number"""
        return self._number

    @number.setter
    def number(self, number: int):
        """set number"""
        self._number = number

    @property
    def balance(self) -> int:
        """get balance"""
        return self._balance

    @balance.setter
    def balance(self, cash: int):
        """set balance"""
        self._balance = self._balance + cash

    @property
    def position(self) -> int:
        """get position"""
        return self._position

    @position.setter
    def position(self, position: int):
        """set position"""
        self._position = position

    @property
    def actual_round(self) -> int:
        """get player's actual round"""
        return self._actual_round

    @actual_round.setter
    def actual_round(self, actual_round: int):
        """set actual round"""
        self._actual_round = actual_round

    @property
    def is_playing(self) -> bool:
        """get playing status"""
        return self._is_playing

    @is_playing.setter
    def is_playing(self, status: bool):
        """set is playing status"""
        self._is_playing = status

    @staticmethod
    def roll_the_dice() -> int:
        """generate a random number as a dice"""
        dice_number = random.randint(1, 6)
        # print('Player {0} rolled the dice and get {1}'.format(
        #             self.number, dice_number))
        return dice_number

    def walk(self, board, dice_number: int) -> int:
        """go to a new position according to a dice number"""
        new_position = self.position + dice_number
        if new_position > board.total_properties:
            # it true, player completed a new round
            self.actual_round = self.actual_round + 1
            board.actual_round = self.actual_round
            # receive prize
            self.balance = board.prize_for_completing_round

            self.position = dice_number - (board.total_properties - self.position)
            # print('+++ Player {0} is in the round {1} with balance {2} +++'.format(
            #             self.number, self.actual_round, self.balance))
        else:
            self.position = new_position
        return self.position

    def has_cash_to_operation(self, value: int):
        """verify if player has cash enough to pay"""
        return (self.balance - value) >= 0

    def buy_property(self, prop: Property) -> bool:
        """buy a property if has cash"""
        if self.has_cash_to_operation(prop.sale_price):
            self.balance = -prop.sale_price
            prop.owner = self
            # print('$$$ Player {0} bought the Property {1} and now has {2} $$$'.format(
            #             self.number, prop.position, self.balance))
            return True
        return False

    def pay_rent_to_owner(self, prop: Property) -> bool:
        """player pays rent to the property owner"""
        if self.has_cash_to_operation(prop.sale_price):
            rental_price = prop.rental_price
            self.balance = rental_price*(-1)
            prop.owner.balance = rental_price
            # print('$$$ Player {0} paid {1} for rent to Player {2} and now has {3} $$$'.format(
            #             self.number, rental_price, prop.owner.number, self.balance))
            return True
        return False
