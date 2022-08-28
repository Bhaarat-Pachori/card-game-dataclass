"""Play the card game
Modules exported by this package:

- `constants`: Provide module level constants
- `create_cards`: Creates card as object
- `deck_of_cards`: Creates the deck of the cards
- `game_setup`: Provides the game setup
- `main`: Provides interface for playing game
- `play_game`: Provides the functionality to play game

This module is a simple card game created to use and understand
dataclasses in Python. The game is simple and played with two
players.

- `How game ends?`
    If one or both the player(s) have exhausted all the cards.
- `Who Wins?`
    Player who have more #cards at the end of the game wins.

Steps:
    1. The game start with a toss to decide the which player get to
       play his hand first.
    2. The player plays his/her first card on the table revealing the
       card.
    3. The second player do exactly as first and play his/her hand.
    4. Once both the players have the cards on the table, a decision
       has to be made for the winner. The winner takes all the cards
       on the table.

- `How the winner for the ongoing turn is decided?`
    Once both the players have played there hands, a comparison
    is done on the rank of the cards. If the cards rank matches then
    the player who had played the last hand wins and takes all the
    cards on the table.

    If the cards rank doesn't match then the game continues as
    previously where the players play their hands and again a
    comparison is done on the card ranks and the winner is decided,
    if any. An important thing to look for is when there is no winner
    for a turn then the last card on the table serves as the first card.
    To understand this please follow the demo below.

### Which is the bigger card?
    The cards in deck assign themselves a weight. The face value
    is the weight. The suite to which the card belongs carries no
    weight.
###
`For example consider below the list of cards`

*['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']*

* `Ace` weight is 1

* `2  ` weight is 2

* `King` weight is 13 and is the biggest card.

## A small demo below:
Turn 1:
    Player 1: 4 ❤️‍

    Player 2: K ♠

    Result:

        No winner, in this turn, as the cards rank do not match.
        Total cards on the table now is 2.

Turn 2:
    Player 1: K ♣

    Player 2: Q ♦

    Result:

        No winner, in this turn too, as the cards rank do not match.
        Total cards on the table now is 4.

Turn 3:
    Player 1: Q ♣

    Player 2: None

    Result:

        As the Player 1's card rank now matches the rank of the
        card from turn 2 so Player is the winner and takes all
        the 5 cards on the table.

Turn 4:
    Player 2: Q ♣

    Player 1: K ♣

    Result:
        In this turn Player 2 starts the turn because the player 2
        didn't get the chance to play the hand in turn 3. No one wins
        this turn as the rank of the cards do not match. Now, there are
        only 2 cards on the table.
"""