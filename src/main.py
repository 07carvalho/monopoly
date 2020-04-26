from board import Board
from player import Player
from property import Property

def start_game():
    total_players = 4
    initial_balance_per_player = 300
    total_properties = 20
    prize_for_completing_round = 100
    max_rounds = 10
    actual_round = 1

    # initializing
    board = Board(total_players,
                  initial_balance_per_player,
                  total_properties,
                  prize_for_completing_round,
                  max_rounds,
                  actual_round)

    board.set_players()
    board.set_properties()


    players = board.players
    print(players)

    while (board.actual_round < board.max_rounds):
        for player in players:
            if board.game_still_running():
                # player rolls dice
                num = player.roll_the_dice()
                # move to property
                board.move_player(player, num)
                print(player.position)

    # verify if property has owner
    # if has owner, pay rent
    #     get cash from player
    #     verify if player is failed
    #     put cash in owner property balance
    # if not decides if buy



if __name__ == '__main__':
    start_game()