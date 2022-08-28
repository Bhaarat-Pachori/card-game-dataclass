import deck_of_cards as deck
from yaml import load, FullLoader
from typing import List
import constants


def get_config() -> dict:
    """
    this method loads the yaml for application based configs
    :return: dict() -> app configurations
    """
    with open("game/constants.py", "r") as cfg:
        configs = load(cfg, Loader=FullLoader)
    return configs


def create_deck_of_cards() -> List:
    """
    Get Card objects created
    :return: list
    """
    cfg = get_config()
    the_deck = []
    for suite in constants.SUITES_UNICODE:
        for card in constants.TOTAL_CARDS_IN_SUITE_VAL:
            the_deck.append(deck.PlayingCard(card, suite))
    return the_deck


deck_to_play = create_deck_of_cards()
