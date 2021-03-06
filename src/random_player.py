import random
from src.player import Player
from src.property import Property


class RandomPlayer(Player):

    strategy = 'Aleatorio'

    def buy_property(self, prop: Property) -> bool:
        """player buys a house according to his strategy"""
        if self.has_cash_to_operation(prop.sale_price):
            if random.choice([True, False]):
                self.balance = -prop.sale_price
                prop.owner = self
                # print('$$$ Player {0} bought the Property {1} and now has {2} $$$'.format(
                #             self.number, prop.position, self.balance))
                return True
            # print('$$$ Player {0} decided not to buy the Property {1} $$$'.format(
            #             self.number, prop.position))
            return True
        return False
