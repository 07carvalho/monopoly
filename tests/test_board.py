import unittest
from src.board import Board


class TestBoard(unittest.TestCase):
    """Testing Board class"""

    def test_actual_round(self):
        """Verify actual round"""
        board = Board(4, 300, 20, 100, 1000, 1)
        board.actual_round = 2
        self.assertEqual(board.actual_round, 2)
        board.actual_round = 1
        self.assertEqual(board.actual_round, 2)


    def test_game_still_running(self):
        """Verify game still running"""
        board = Board(4, 300, 20, 100, 1000, 1)
        board.actual_round = 999
        self.assertEqual(board.game_still_running(), True)
        board.actual_round = 1000
        self.assertEqual(board.game_still_running(), False)


if __name__ == '__main__':
    unittest.main()
    