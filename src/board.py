from player import Player
from property import Property


class Board:

    def __init__(self, total_players, initial_balance_per_player,
                 total_properties, prize_for_completing_round, max_rounds):
        self._total_players = total_players
        self._initial_balance_per_player = initial_balance_per_player
        self._total_properties = total_properties
        self._prize_for_completing_round = prize_for_completing_round
        self._max_rounds = max_rounds
        self.players = []
        self.properties = []

    @property
    def total_players(self):
        """get total_players"""
        return self._total_players

    @total_players.setter
    def total_players(self, total_players):
        """set total_players"""
        self._total_players = total_players

    @property
    def initial_balance_per_player(self):
        """get initial_balance_per_player"""
        return self._initial_balance_per_player

    @initial_balance_per_player.setter
    def initial_balance_per_player(self, initial_balance_per_player):
        """set initial_balance_per_player"""
        self._initial_balance_per_player = initial_balance_per_player

    @property
    def total_properties(self):
        """get total_properties"""
        return self._total_properties

    @total_properties.setter
    def total_properties(self, total_properties):
        """set total_properties"""
        self._total_properties = total_properties

    @property
    def prize_for_completing_round(self):
        """get prize_for_completing_round"""
        return self._prize_for_completing_round

    @prize_for_completing_round.setter
    def prize_for_completing_round(self, prize_for_completing_round):
        """set prize_for_completing_round"""
        self._prize_for_completing_round = prize_for_completing_round

    @property
    def max_rounds(self):
        """get max_rounds"""
        return self._max_rounds

    @max_rounds.setter
    def max_rounds(self, max_rounds):
        """set max_rounds"""
        self._max_rounds = max_rounds

    def set_properties(self):
        sale_price = 200
        rental_price = 60
        first_owner = None

        for i in self._total_properties:
            self.properties.append(Property(i, sale_price, rental_price, first_owner))


    def set_players(self):
        initial_position = 0
        initial_properties = []

        for i in self._total_players:
            self.players.append(Player(i, self._initial_balance_per_player,
                                  initial_position, initial_properties))


