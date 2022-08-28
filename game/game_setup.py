import random

import constants
import create_cards as cc


class GameSetup:
    def __init__(self, num_of_players: int):
        self.deck: list = cc.create_deck_of_cards()
        self.players: int = num_of_players
        self.cards_per_player_count = None

    def shuffle_deck(self):
        """
        this method shuffle the deck of the cards in place
        :return: None
        """
        random.shuffle(self.deck)

    def cards_per_player(self) -> int:
        """
        this method is used to find out how many cards should each
        player get
        :return: number of cards each player gets
        """
        self.cards_per_player_count: int = constants.TOTAL_CARDS_COUNT // self.players
        return self.cards_per_player_count

    def deal_cards(self, st: int, last: int) -> list:
        """
        this method deal the equal number of cards to each player
        after the deck has been shuffled.
        :param st: start index to pick cards from
        :param last: end index to pick card to
        :return: the cards from start to end index
        """
        return self.deck[st:last]

    def deal_cards_round_robin(self, from_idx: int, to_idx: int) -> list:
        """
        this method deal the equal number of cards to each player
        after the deck has be shuffled.
        :param from_idx: start index to pick cards from
        :param to_idx: end index to pick card to
        :return: the cards from start to end index
        """
        pass

    def get_deck(self) -> list:
        """
        this method returns the whole deck of cards
        :return:
        """
        return self.deck
