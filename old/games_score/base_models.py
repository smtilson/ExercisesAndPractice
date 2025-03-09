from typing import Optional, Union


class Card:
    def __init__(self, value: Union[int,str], suit: Optional[str]=None) -> None:
        self.suit = suit
        self.value = value

    def __repn__(self):
        return f"Suit:{self.suit} Value: {self.value}"