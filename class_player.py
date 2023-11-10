class Player:

    def __init__(self, name, is_dealer=False):
        self.name = name
        self.is_dealer = is_dealer
        # "Hand" is a set of cards that a player have at the moment
        self.hand = []

    # deal cards to all players
    def deal(self, deck, *args):  # *args are players to deal cards in the beginning
        if self.is_dealer:
            # deal 6 cards to each player
            for player in args:
                cards_to_deal = [deck.cards.pop() for _ in range(6)]
                player.hand.append(cards_to_deal)

                # reveal the trump suit by popping one more card and putting it at the beginning of the deck
                card = deck.cards.pop()  # the card that defines trump suit

                deck.cards.insert(0, card)

        else:
            raise ValueError("Only dealer can deal cards")

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

