import random


class Game:
    """
    A class that represents a card object

    ...

    Attributes
    ----------
    no_of_players : int
        The number of players
    cards_per_player : int
        The number of cards each player should receive
    Methods
    -------
    deal_cards()

    """

    no_of_players = 0
    cards_per_player = 0

    def __init__(self, no_of_players, cards_per_player):
        self.no_of_players = no_of_players
        self.cards_per_player = cards_per_player

    def deal_cards(self) -> list:
        """
        Generates a list of lists, with each list containing cards for each player

        Parameters
        ----------
        None

        Raises
        ----------
        IndexError
            If the index is out of bounds of the deck cards.
        """
        values = range(2, 15)
        # J = 11, Q = 12, K = 13 and A = 11 (not 1).
        suits = ["diamonds", "clubs", "hearts", "spades"]
        deck = []
        for suit in suits:
            for value in values:
                deck.append(f"{value}_of_{suit}")
        cards = []
        count = 0
        total_players = self.no_of_players
        total_player_cards = self.cards_per_player
        while count < total_players:
            player_cards = []
            for n in range(total_player_cards):
                try:
                    card = random.choice(deck)
                    player_cards.append(card)
                    deck.remove(card)
                except IndexError as err:
                    print("The deck is empty")
                    return
            cards.append(player_cards)
            count += 1

        return cards
