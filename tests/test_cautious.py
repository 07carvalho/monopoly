import unittest
from src.cautious_player import CautiousPlayer
from src.property import Property


class TestCautious(unittest.TestCase):

    def setUp(self):
        self.player = CautiousPlayer(1, 300, 1, 1)
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

    def test_dont_buy_property(self):
        """operation_ok must be True, but as the player didn't buy, balance still the same"""
        self.prop.sale_price = 250
        operation_ok = self.player.buy_property(self.prop)
        self.assertTrue(operation_ok)
        self.assertEqual(self.prop.owner, None)
        self.assertEqual(self.player.balance, 300)


if __name__ == '__main__':
    unittest.main()
