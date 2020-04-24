import unittest
from src.player import Player


class TestPlayer(unittest.TestCase):
	"""Testing Player class"""
	# def __init__(self):

	def test_increase_balance(self):
		"""Verify balance"""
		self.p1 = Player(1, 300, 0, [])
		self.p1.balance = 40
		self.assertEqual(self.p1.balance, 340)


	def test_decrease_balance(self):
		"""Verify balance"""
		self.p1 = Player(1, 300, 0, [])
		self.p1.balance = -100
		self.assertEqual(self.p1.balance, 200)


	def test_roll_dice_and_walk(self):
		"""Verify walk"""
		self.p1 = Player(1, 300, 0, [])
		dice_number = self.p1.roll_the_dice()
		self.p1.walk(dice_number)
		self.assertEqual(self.p1.position, dice_number)


if __name__ == '__main__':
    unittest.main()