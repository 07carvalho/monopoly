from collections import Counter, OrderedDict
from statistics import mean


class Simulation:
    """This class get data from the simulation"""
    
    def __init__(self):
        self._round_per_game = []
        self._winner = []

    @property
    def round_per_game(self) -> list:
        """get round per game"""
        return self._round_per_game

    @round_per_game.setter
    def round_per_game(self, final_round: int):
        """set round per game"""
        self._round_per_game.append(final_round)

    @property
    def winner(self) -> list:
        """get winner"""
        return self._winner

    @winner.setter
    def winner(self, player: str):
        """set winner"""
        self.winner.append(player)

    def count_round_per_game(self, value: int) -> int:
        """return the number of times a value appear in round_per_game attribute"""
        return self.round_per_game.count(value)

    def count_victories_per_player(self) -> dict:
        """return a object with the number of victories per player"""
        winners_dict = dict(Counter(self.winner))
        return {strategy: value for strategy, value in sorted(winners_dict.items(),
                                        key=lambda item: item[1], reverse=True)}

    def round_avg(self) -> float:
        """return the average of rounds"""
        return mean(self.round_per_game) 

