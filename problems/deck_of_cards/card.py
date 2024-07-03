from suit import Suit


class Card:
    """
    Card class. Each card will have a Suit and a number.

    The number must be between 1 and 13 inclusive, enforced
    in the copnstructor
    """

    def __init__(self, suit: Suit, number: int):
        self.suit = suit
        self.number = Card._set_number(number)

    @staticmethod
    def _set_number(number: int) -> int:
        """
        Raises ValueError if number is oputside the range [1, 13] inclusive
        """
        if number not in range(0, 14):
            raise ValueError("Card number must be between 1 and 13 inclusive")
        return number

    def __str__(self) -> str:
        val = str(self.number)
        if self.number == 1:
            val = "Ace"
        elif self.number == 11:
            val = "Jack"
        elif self.number == 12:
            val = "Queen"
        elif self.number == 13:
            val = "King"

        return f"{val} of {self.suit}"
