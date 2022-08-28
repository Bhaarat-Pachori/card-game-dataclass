import random
from collections import defaultdict

from deck_of_cards import PlayingCard


class PlayGame:
    """
    This is the PlayGame class which handles the game features
    """

    def __init__(self, players: dict = None, players_count: int = None):
        self.players = players
        self.players_count = players_count
        self.track_winner = defaultdict(int)
        self.toss_winner: int = 0
        self.status_report = {}

    def player_draw_card(self, player: int) -> PlayingCard:
        """
        this method returns the card drawn by the player
        :param player: which player's turn to draw card
        :return: PlayingCard object
        """
        card_drawn = random.choice(range(len(self.players[player])))
        print(
            f"\tPlayer {player} draw: {self.players[player][card_drawn].rank} {self.players[player][card_drawn].suite}")
        draw = self.players[player][card_drawn]
        del self.players[player][card_drawn]
        return draw

    def update_player_score(self, player: int, cards_won_count: int) -> None:
        """
        this method keep tracks of the wins of each player
        :param player: which player won
        :return: None
        """
        # if not player:
        #     self.track_winner[1] += 1
        #     self.track_winner[2] += 1
        # else:
        self.track_winner[player] += cards_won_count

    def print_winner(self):
        """
        this is a wrapper method which calls banner() method
        :return: None
        """
        if self.track_winner[1] > self.track_winner[2]:
            self.banner("Player 1")
        elif self.track_winner[1] < self.track_winner[2]:
            self.banner("Player 2")
        else:
            self.banner("")

    def banner(self, player: str = None):
        """
        this method prepares the winner banner and looser banner
        for the display
        :param player: which player won
        :return: None
        """
        player_1_cards = self.track_winner[1]
        player_2_cards = self.track_winner[2]
        cards_on_table = 52 - (self.track_winner[1] + self.track_winner[2])

        if player:
            result = f"\t\t\U0001f389 {player} won\U0001f389\nGame Stats:\nCards Count:\n\tPlayer 1 cards: {player_1_cards}"
            result += f"\n\tPlayer 2 cards: {player_2_cards}"
            result += f"\n\tCards on table: {cards_on_table}"
        else:
            result = f"\t\tIt is a tie!"
            result = f"\t\tGame Stats:\nCards Count:\n\tPlayer 1 cards: {player_1_cards}"
            result += f"\n\tPlayer 2 cards: {player_2_cards}"
            result += f"\n\tCards on table: {cards_on_table}"

        print(result)

    def do_toss(self) -> int:
        self.toss_winner = random.randrange(1, 11)
        return 1 if self.toss_winner % 2 == 0 else 2
        # 8349100032180888
        # 855- 757-7328

    def get_detail_status(self) -> dict:
        # if len(self.players[0]) and len(self.players[1]):
        # get each player's cards count
        self.status_report['player1_cards_count'] = len(self.players[1])
        self.status_report['player2_cards_count'] = len(self.players[2])

        # get which player is currently leading in the game
        if self.track_winner[2] > self.track_winner[1]:
            self.status_report['leading_player'] = [self.track_winner[2], "Player 2"]
        else:
            self.status_report['leading_player'] = [self.track_winner[1], "Player 1"]

        # get how many cards left in the game
        self.status_report['cards_on_table'] = 52 - (len(self.players[1]) + len(self.players[2]) + self.status_report['leading_player'][0])

        return self.status_report
