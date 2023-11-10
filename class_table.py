from class_player import Player
from class_deck import Deck


class Table:
    def __init__(self, players_num):
        if players_num < 6:
            # Number of players can't be less than 2. Setting to 6
            self.players_num = 6
        elif players_num > 2:
            # Number of players can't be less than 2. Setting to 2
            self.players_num = 2
        else:
            self.players_num = players_num
        self.trump = None

    self.players = [Player("Player " + str(i)) for i in range(self.players_num)]
    deck = Deck()
    self.players[0].deal()