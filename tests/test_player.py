import unittest
from src.player import Player


class TestPlayer(unittest.TestCase):
    """Testing Player class"""

    def test_increase_balance(self):
        """Verify balance"""
        p1 = Player(1, 300, 0, 1)
        p1.balance = 40
        self.assertEqual(p1.balance, 340)

    def test_decrease_balance(self):
        """Verify balance"""
        p1 = Player(1, 300, 0, 1)
        p1.balance = -100
        self.assertEqual(p1.balance, 200)


if __name__ == '__main__':
    unittest.main()
    