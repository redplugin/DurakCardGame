import random
from class_card import Card


class Deck:
    def __init__(self):
        ranks = ["6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        suits = ["♥️", "♦️", "♣️", "♠️"]  # hearts, diamonds, clubs, spades
        self.cards = [Card(rank, suit) for rank in ranks for suit in suits]

    def shuffle(self):
        random.shuffle(self.cards)