"""Setup and Play the Game between two players

The module contains the following functions:

- `start_game(players_hand: dict, players_total: int)` - starts the game.
- `setup_game()` - Set up the game before playing.
"""
import constants
from deck_of_cards import PlayingCard
from game_setup import GameSetup
from play_game import PlayGame


def check_last_two_cards(last_two_cards: list) -> bool:
    if last_two_cards[0] == last_two_cards[1]:
        return True


def start_game(player_hands: dict, players_total: int) -> None:
    """
    this method is responsible for the game start, play and stop
    :param player_hands: each player's cards
    :param players_total: total number of players in the game
    :return: None
    """
    on_table: list[PlayingCard] = []
    pg = PlayGame(players=player_hands, players_count=players_total)
    player = pg.do_toss()
    print(f"Player {player} won the toss!")
    total_cards = constants.TOTAL_CARDS_COUNT
    turn = 1
    hand_won = False
    # for turn in range(total_cards // players_total):
    while turn:
        if hand_won:
            hand_won = False
        status = pg.get_detail_status()
        if not (status['player1_cards_count'] and status['player2_cards_count']):
            # celebrate the winner
            pg.print_winner()
            break
        print(f"Turn {turn}:")
        if player == 1:
            while player <= players_total:
                input(f"\tPlayer {player} turn, press key to play")
                on_table.append(pg.player_draw_card(player))
                # if len(on_table) > 2:
                if len(on_table) >= 2 and check_last_two_cards(on_table[-2:]):
                    pg.update_player_score(player=player, cards_won_count=len(on_table))
                    player = player
                    hand_won = True
                    print(f"Player {player} takes {len(on_table)} cards")
                    on_table.clear()
                    break
                player += 1
        else:
            while player > 0:
                input(f"\tPlayer {player} turn, press key to play")
                on_table.append(pg.player_draw_card(player))
                if len(on_table) >= 2 and check_last_two_cards(on_table[-2:]):
                    pg.update_player_score(player=player, cards_won_count=len(on_table))
                    player = player
                    hand_won = True
                    print(f"Player {player} takes {len(on_table)} cards")
                    on_table.clear()
                    break
                player -= 1
            # continue

        # the value of player could be 0 or 3 coming out of the above if-else
        # assign player the right value, which either 1 or 2
        if player == 3 and not hand_won:  # represents that player 1 started the game
            player = 2
        if player == 0 and not hand_won:  # represents that player 2 started the game.
            player = 1
        turn += 1
        if bool(on_table) and check_last_two_cards(on_table[-2:]):
            #     print(f"\U0001f514It's a match\U0001f514")
            pg.update_player_score(player=player, cards_won_count=len(on_table))
            print(f"Player {player} takes {len(on_table)} cards")
            hand_won = True
            # reset the table of cards_won_count
            on_table.clear()
        else:
            if not hand_won:
                player = 1 if player == 2 else 2
            continue


def setup_game() -> tuple[dict[int, list], int]:
    """
    This method set up the game to be played
    :return: None
    """
    total_players = 2
    start = 0
    # total_turns = constants.TOTAL_CARDS_COUNT // total_players

    game_setup = GameSetup(total_players)
    game_setup.shuffle_deck()
    end = game_setup.cards_per_player()
    player_hand = {}

    for itr in range(total_players):
        player_hand[itr+1] = game_setup.deal_cards(start, end)
        start = end
        end += end

    print(f"Player 1 hand {player_hand[1]}")
    print(f"Player 2 hand {player_hand[2]}")
    return player_hand, total_players


if "__main__" == __name__:
    hands, player_count = setup_game()
    start_game(hands, player_count)
