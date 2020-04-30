from src.board import Board
from src.simulation import Simulation


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
                        # if no owner, decides if buy property
                        operation_ok = player.buy_property(prop)
                    else:
                        # if has another owner, pay rent
                        operation_ok = player.pay_rent_to_owner(prop)

                    if not operation_ok:
                        board.remove_player_properties(player)

                    if not board.at_least_two_playing():
                        break


    # print("\nGame Over!")
    return board.declare_winner()

if __name__ == '__main__':
    simulation = Simulation()
    simulations_qty = 1000
    
    for game in range(simulations_qty):
        print('Starting Simulation {}'.format(game))
        winner, final_round = start_game()
        simulation.winner = winner
        simulation.round_per_game = final_round

    print('\n\n\n\n\nResumo:')

    time_out_qty = simulation.count_round_per_game(1000)
    print('{0} partidas terminam por time out (1000 rodadas).'.format(time_out_qty))

    round_avg = simulation.round_avg()
    print('Uma partida demora em media {:.1f} rodadas.'.format(round_avg))

    print('Vitorias por jogador:')
    victories_count_dict = simulation.count_victories_per_player()
    for player, qty in victories_count_dict.items():
        percentage = (qty*100)/simulations_qty
        print('- O jogador {} venceu {:.1f}% das partidas.'.format(player, percentage))

    print('O comportamento que mais vence eh o {}!'.format(next(iter(victories_count_dict))))
