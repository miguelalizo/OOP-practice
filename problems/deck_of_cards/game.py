from abc import ABC, abstractmethod
from deck import RegularDeck, IDeck


class CardGame(ABC):
    def __init__(self, deck: IDeck):
        self.deck = deck

    @abstractmethod
    def play_game(self):
        pass


class BlackJack(CardGame):
    def __init__(self, deck: RegularDeck):
        self.deck = deck

    def play_game(self):
        print("Play game")


if __name__ == "__main__":
    deck = RegularDeck()
    blackjack = BlackJack(deck)

    print(blackjack.deck)
