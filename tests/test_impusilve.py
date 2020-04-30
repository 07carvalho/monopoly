import unittest
from src.impulsive_player import ImpulsivePlayer
from src.property import Property


class TestImpulsive(unittest.TestCase):

    def setUp(self):
        self.player = ImpulsivePlayer(1, 300, 1, 1)
        self.prop = Property(1, 200, 60, None)

    def test_buy_property(self):
        """test a buy operation. will return true if has balance"""
        operation_ok = self.player.buy_property(self.prop)
        self.assertTrue(operation_ok)
        self.assertEqual(self.prop.owner, self.player)
        self.assertEqual(self.player.balance, 100)

    def test_low_balance(self):
        # removing player's cash
        self.player.balance = -300
        operation_ok = self.player.buy_property(self.prop)
        self.assertFalse(operation_ok)


if __name__ == '__main__':
    unittest.main()
