from dataclasses import dataclass
from typing import List


@dataclass
class PlayingCard:
    rank: str
    suite: str
    face_cards = ['A', 'K', 'Q', 'J']

    def __eq__(self, other):
        return self.rank == other.rank

    def __gt__(self, other):
        if self.rank in self.face_cards and other.rank in self.face_cards:
            if self.rank == 'A':
                return True
            elif other.rank == 'A':
                return False
            else:
                return ord(self.rank) > ord(other.rank)
        elif self.rank in self.face_cards and other.rank not in self.face_cards:
            return ord(self.rank) > int(other.rank)
        elif other.rank in self.face_cards and self.rank not in self.face_cards:
            return ord(other.rank) > int(self.rank)
        else:
            return int(self.rank) == int(other.rank)


@dataclass
class Deck:
    cards: List[PlayingCard]
