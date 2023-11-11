class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.is_trump = False

    def __repr__(self):
        return f"{self.rank} {self.suit}" + (" (Trump)" if self.is_trump else "")

    def rank_value(self):
        if self.rank == "J":
            return 11
        elif self.rank == "Q":
            return 12
        elif self.rank == "K":
            return 13
        elif self.rank == "A":
            return 14
        else:
            return int(self.rank)

    def compare(self, other_card):
        # Compare trumps separately
        if self.is_trump and not other_card.is_trump:
            return 1
        elif not self.is_trump and other_card.is_trump:
            return -1

        # If both cards are trumps or of the same suits, compare based on rank values:
        self_value = self.rank_value()
        other_value = other_card.rank_value()

        if self_value == other_value:
            return 0  # equal
        elif self_value < other_value:
            return -1  # other card is more powerful
        else:
            return 1  # this card is more powerful

    def set_trump(self, trump_suit):
        if self.suit == trump_suit:
            self.is_trump = True
