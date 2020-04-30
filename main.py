from src.board import Board


def start_game():
    total_players = 4
    initial_balance_per_player = 300
    total_properties = 20
    prize_for_completing_round = 100
    max_rounds = 1000
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

    while (board.game_still_running() and board.at_least_two_playing()):
        for player in players:
            if player.is_playing:
                # player rolls dice
                dice_number = player.roll_the_dice()
                # move to property
                new_position = player.walk(board, dice_number)
                prop = board.get_property_by_position(new_position)
                
                # verify if player own property
                if prop.owner is not player:
                    operation_ok = False
                    if prop.owner is None:
                        # if not, decides if buy
                        operation_ok = player.buy_property(prop)
                        # if has another owner, pay rent
                    else:
                        operation_ok = player.pay_rent_to_owner(prop)

                    if not operation_ok:
                        board.remove_player_properties(player)

                    if not board.at_least_two_playing():
                        break


    print("end")
    board.declare_winner()

if __name__ == '__main__':
    start_game()