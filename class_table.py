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

        # create a deck and shuffle
        self.deck = Deck()
        self.deck.shuffle()

        # find out trump suite of the game according to the number of players
        self.trump_suite = None
        if players_num == 6:
            # last card is the trump suit
            self.trump_suite = self.deck.cards[-1].suit
        else:
            # Turn up the top card of the deck to determine the trump suit
            the_card_after_dealing = players_num * 6 + 1
            card = self.deck.cards.pop()[-1 * the_card_after_dealing]
            self.trump_suite = card.suit

            # put the card to the bottom of the deck
            self.deck.cards.insert(0, card)

        # check every card in the deck and set a cards of a certain suit trump
        for card in self.deck.cards:
            card.set_trump(self.trump_suite)

        # create players
        self.players = [Player("Player " + str(i)) for i in range(self.players_num)]

        # find the 1st player to attack according to the smallest trump they have
        smallest_trump = None
        self.current_player = None
        for player in self.players:
            trumps = [x for x in player.hand if x == x.is_trump]
            if len(trumps) > 0 and min(trumps) < smallest_trump:
                smallest_trump = min(trumps)
                self.current_player = player

    def next_current_player(self):
        # if current player is the last in the list, set index of the next player to 0
        if self.players.index(self.current_player) != self.players[-1]:
            new_index = self.players.index(self.current_player) + 1
        else:
            new_index = 0
        return self.players[new_index]

    # deal cards
    def deal(self):
        # each player gets 6 cards
        for player in self.players:
            cards_to_deal = [self.deck.cards.pop() for _ in range(6)]
            player.hand.append(cards_to_deal)

    def start_game(self):
        print("Welcome to Durak!")
        print("Cards have been dealt!")
        print(f"Trump suit is {self.trump_suite}")

    def play_turn(self):
        self.current_player.display_hand()

        print(f"\n{self.current_player.name}, it's your turn.")
        print("Enter the index of the card you want to play or '0' to end your turn:")








