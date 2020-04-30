import unittest
from src.player import Player
from src.property import Property


class TestProperty(unittest.TestCase):
    """Testing Property class"""

    def test_actual_round(self):
        """Verify actual round"""
        prop = Property(1, 100, 50, None)
        player = Player(1, 300, 0, 1)
        prop.owner = player
        self.assertEqual(prop.has_owner(), True)


if __name__ == '__main__':
    unittest.main()
    