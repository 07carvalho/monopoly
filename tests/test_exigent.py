import unittest
from src.exigent_player import ExigentPlayer
from src.property import Property


class TestExigent(unittest.TestCase):

    def setUp(self):
        self.player = ExigentPlayer(1, 300, 1, 1)
        self.prop = Property(1, 200, 60, None)

    def test_buy_property(self):
        """test a buy operation"""
        operation_ok = self.player.buy_property(self.prop)
        self.assertTrue(operation_ok)
        self.assertEqual(self.prop.owner, self.player)
        self.assertEqual(self.player.balance, 100)

    def test_low_balance(self):
        # removing player's cash
        self.player.balance = -300
        operation_ok = self.player.buy_property(self.prop)
        self.assertFalse(operation_ok)

    def test_dont_buy_property(self):
        """operation_ok must be True, but as the player didn't buy, balance still the same"""
        self.prop.rental_price = 40
        operation_ok = self.player.buy_property(self.prop)
        self.assertTrue(operation_ok)
        self.assertEqual(self.prop.owner, None)
        self.assertEqual(self.player.balance, 300)


if __name__ == '__main__':
    unittest.main()
