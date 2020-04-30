import random
from src.cautious_player import CautiousPlayer
from src.exigent_player import ExigentPlayer
from src.impulsive_player import ImpulsivePlayer
from src.random_player import RandomPlayer
from src.player import Player
from src.property import Property
from typing import Tuple


class Board:

    def __init__(self, total_players: int, initial_balance_per_player: int,
                 total_properties: int, prize_for_completing_round: int,
                 max_rounds: int, actual_round: int):
        self._total_players = total_players
        self._initial_balance_per_player = initial_balance_per_player
        self._total_properties = total_properties
        self._prize_for_completing_round = prize_for_completing_round
        self._max_rounds = max_rounds
        self._actual_round = actual_round
        self.players = []
        self.properties = []

    @property
    def total_players(self) -> int:
        """get total_players"""
        return self._total_players

    @total_players.setter
    def total_players(self, total_players: int):
        """set total_players"""
        self._total_players = total_players

    @property
    def initial_balance_per_player(self) -> int:
        """get initial_balance_per_player"""
        return self._initial_balance_per_player

    @initial_balance_per_player.setter
    def initial_balance_per_player(self, initial_balance_per_player: int):
        """set initial_balance_per_player"""
        self._initial_balance_per_player = initial_balance_per_player

    @property
    def total_properties(self) -> int:
        """get total_properties"""
        return self._total_properties

    @total_properties.setter
    def total_properties(self, total_properties: int):
        """set total_properties"""
        self._total_properties = total_properties

    @property
    def prize_for_completing_round(self) -> int:
        """get prize_for_completing_round"""
        return self._prize_for_completing_round

    @prize_for_completing_round.setter
    def prize_for_completing_round(self, prize_for_completing_round: int):
        """set prize_for_completing_round"""
        self._prize_for_completing_round = prize_for_completing_round

    @property
    def max_rounds(self) -> int:
        """get max_rounds"""
        return self._max_rounds

    @max_rounds.setter
    def max_rounds(self, max_rounds: int):
        """set max_rounds"""
        self._max_rounds = max_rounds

    @property
    def actual_round(self) -> int:
        """get max_rounds"""
        return self._actual_round

    @actual_round.setter
    def actual_round(self, num: int):
        """set actual_round"""
        if num > self._actual_round:
            self._actual_round = num

    def set_properties(self):
        """set all the properties of the board"""

        # setting low prices as the initial balance of each player
        sale_price = random.choice(range(60, 120))
        rental_price = random.choice(range(10, 60))
        first_owner = None

        for i in range(1, self._total_properties + 1):
            self.properties.append(Property(i, sale_price, rental_price, first_owner))

    def set_players(self):
        """setting all players"""
        initial_position = 0
        initial_round = 1
        players = [ImpulsivePlayer, ExigentPlayer, CautiousPlayer, RandomPlayer]

        for i in range(1, self._total_players + 1):
            player = players[i - 1]
            self.players.append(player(i, self._initial_balance_per_player,
                                       initial_position, initial_round))

    def game_still_running(self) -> bool:
        """verify if max rounds number was not reached"""
        return self._actual_round < self._max_rounds

    def get_property_by_position(self, position: int) -> Property:
        """return the property according to the position in properties list"""
        return self.properties[position - 1]

    def at_least_two_playing(self) -> bool:
        """verify if at least two players still playing"""
        count = 0
        for player in self.players:
            if player.is_playing:
                count += 1
        return count >= 2

    def remove_player_properties(self, player: Player):
        """remove all properties"""
        for prop in self.properties:
            if prop.owner is player:
                prop.owner = None

        player.is_playing = False
        # print('!!! Player {0} is out of cash and out of game !!!'.format(player.number))

    def declare_winner(self) -> Tuple[str, int]:
        """
        Declare who won the game
        - The tiebreaker criterion is the players' turn order in this match.
        - So, in the end, the first element in Players List that still playing
          is the winner
        """
        for player in self.players:
            if player.is_playing:
                # print('Player {0} won the game in the round number {1}'.format(
                #         player.strategy, self.actual_round))
                return player.strategy, self.actual_round
