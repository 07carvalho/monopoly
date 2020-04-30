import unittest
from src.random_player import RandomPlayer
from src.property import Property


class TestRandom(unittest.TestCase):

    def setUp(self):
        self.player = RandomPlayer(1, 300, 1, 1)
        self.prop = Property(1, 200, 60, None)

    def test_buy_property(self):
        """test a buy operation. will return true if has balance"""
        operation_ok = self.player.buy_property(self.prop)
        self.assertTrue(operation_ok)

    def test_low_balance(self):
        # removing player's cash
        self.player.balance = -300
        operation_ok = self.player.buy_property(self.prop)
        self.assertFalse(operation_ok)


if __name__ == '__main__':
    unittest.main()
