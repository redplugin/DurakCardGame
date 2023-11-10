import random
from class_card import Card


class Deck:
    def __init__(self, trump_suit):
        ranks = ["6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.cards = [Card(rank, suit, is_trump=(suit == trump_suit)) for rank in ranks for suit in suits]

    def shuffle(self):
        random.shuffle(self.cards)
