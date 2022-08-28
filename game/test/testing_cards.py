from game import deck_of_cards


def test_playing_cards():
    card = deck_of_cards.PlayingCard('J', 'Spade')
    assert card.rank == "J"
    assert card.suite == "Spade"


def test_deck():
    j_s = deck_of_cards.PlayingCard('J', 'Spade'),
    j_h = deck_of_cards.PlayingCard('J', 'Heart'),
    j_c = deck_of_cards.PlayingCard('J', 'Club'),
    j_d = deck_of_cards.PlayingCard('J', 'Diamond')

    deck = deck_of_cards.Deck([j_s, j_h, j_c, j_d, ])
    assert deck is not None
    assert str(j_d) == "PlayingCard(rank='J', suite='Diamond')"
    assert str(j_s) == "(PlayingCard(rank='J', suite='Spade'),)"
    assert str(j_h) == "(PlayingCard(rank='J', suite='Heart'),)"
    assert str(j_c) == "(PlayingCard(rank='J', suite='Club'),)"
