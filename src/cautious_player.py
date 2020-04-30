from src.player import Player

class CautiousPlayer(Player):

    def buy_property(self, prop):
        """player buys a house according to his strategy"""
        if self.has_cash_to_operation(prop.sale_price):
            if (self.balance - prop.sale_price) >= 80:
                self.balance = -prop.sale_price
                prop.owner = self
                print('$$$ Player {0} bought the Property {1} and now has {2} $$$'.format(
                            self.number, prop.position, self.balance))
                return True
            print('$$$ Player {0} decided not to buy the Property {1} $$$'.format(
                        self.number, prop.position))
            return True
        return False
        