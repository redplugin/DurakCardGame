class Player:

    def __init__(self, name, is_dealer=False):
        self.name = name
        self.is_dealer = is_dealer
        # "Hand" is a set of cards that a player have at the moment
        self.hand = []

    def draw(self, deck):
        # if the deck is empty or the player have more than 6 cards - return
        if len(deck.cards) > 0 or len(self.hand) >= 6:
            return

        missing_cards_num = 6 - len(self.hand)
        # when deck (list) is empty it will return IndexError exception
        while len(deck.cards) > 0 and missing_cards_num > 0:
            try:
                card = deck.cards.pop()
                self.hand.append(card)
            except IndexError:
                return

    def display_hand(self):
        print(f"Player {self.name}'s hand:", end=" ")
        for card in self.hand:
            print(card, end=" ")
