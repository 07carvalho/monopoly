from board import Board
from player import Player
from property import Property

def start_game():
    total_players = 4
    initial_balance_per_player = 300
    total_properties = 20
    prize_for_completing_round = 100
    max_rounds = 1000

    # initializing
    board = Board(total_players,
                  initial_balance_per_player,
                  total_properties,
                  prize_for_completing_round,
                  max_rounds)



if __name__ == '__main__':
    start_game()