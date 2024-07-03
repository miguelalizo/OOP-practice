from random import shuffle
from abc import ABC, abstractmethod
from typing import List, Optional
from card import Card
from suit import Suit


class IDeck(ABC):
    def __init__(self):
        self.deck: List[Card] = self._create_deck()

    def shuffle(self):
        """
        Shuffles the cards in the deck
        """
        shuffle(self.deck)

    def deal_card(self) -> Optional[Card]:
        """
        Deal top card form the deck
        """
        if not self.deck:
            print("No cards left in the deck")
            return None
        return self.deck.pop()

    @staticmethod
    @abstractmethod
    def _create_deck() -> List[Card]:
        """
        Returns a List of Cards, one of each number for each Suit
        """
        pass

    def __str__(self):
        res = ""
        for card in self.deck:
            res += card.__str__() + "\n"
        return res


class RegularDeck(IDeck):
    def __init__(self):
        super().__init__()

    @staticmethod
    def _create_deck() -> List[Card]:
        """
        Returns a List of Cards, one of each number for each Suit
        """
        deck = []
        for suit in Suit:
            for i in range(1, 14):
                deck.append(Card(suit, i))
        return deck


if __name__ == "__main__":
    deck = RegularDeck()

    deck.shuffle()

    print(deck)

    for i in range(53):
        print(deck.deal_card())
