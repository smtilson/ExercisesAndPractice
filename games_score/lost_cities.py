from base_models import Card
from typing import List, Tuple, Optional, Union


def create_deck()-> List[Card]:
    suits = LostCitiesCard.suits
    values = LostCitiesCard.values
    deck = [Card(suit=suit,value=value) for suit in suits for value in values]
    return deck


class Column:
    def __init__(self, color: str, stack:List[Card]=None) -> None:
        self.color = color
        if not stack:
            self.stack = []
        else:
            self.stack = stack

    def add_card(self, card:Card) -> None:
        if self.validate_card(card):
            self.stack.append(card)

    def validate_card(self, card) -> bool:
        # this is a bit of a mess.
        if card.suit != self.color:
            raise ValueError(f"{card} is not {self.color}.")
        elif card.value == 'bet':
            if not place_bet_card(self):
                raise ValueError(f'Cannot place {card} on {self.stack[-1]}.')
        elif isinstance(card.value, int):
            if not place_number_card(card.value, self):
                raise ValueError(f'Cannot place {card} on {self.stack[-1]}.')
        return True

    def score_col(self) -> int:
        if not self.stack:
            return 0
        bets = 0
        count = 0
        sum = 0
        for card in self.stack:
            count += 1
            if card.value == 'bet':
                bets += 1
            else:
                sum += card.value
        total = (bets+1)*(sum-20)
        if count >= 8:
            total += 20
        return total


class LostCitiesCard(Card):
    suits = ["yellow", "white", "blue", "green", "red"]
    values = ["bet", "bet", "bet", 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def __init__(self, suit:str, value: Union[str,int]) -> None:
        self.suit = self.validate_suit(suit)
        self.value = self.validate_value(value)

    def validate_suit(self, suit: str) -> str:
        if suit in self.suits:
            return suit
        raise ValueError(f"{suit} is not in {self.suits}.")

    def validate_value(self, value: str) -> Union[str,int]:
        if value == "bet":
            return value
        try:
            value = int(value)
            if value in self.values:
                return value
            else:
                raise ValueError
        except ValueError:
            raise ValueError(f"{value} is not in {self.values}.")


def place_bet_card(col: Column) -> bool:
    if not col.stack:
        return True
    elif col.stack[-1].value == 'bet' and len(col.stack) < 3:
        return True
    return False


def place_number_card(value, col: Column) -> bool:
    if not col.stack:
        return True
    elif col.stack[-1] == 'bet':
        return True
    elif value > col.stack[-1].value:
        return True
    return False


def compute_players_score() -> int:
    suits = ["yellow", "white", "blue", "green", "red"]
    score = 0
    columns = [Column(color=suit) for suit in suits]
    print(columns[0]==columns[2])
    for column in columns:
        print([f"{card.suit} {card.value}" for card in column.stack])
        print(f'Please list your {column.color} cards, from bet to 10.')
        finished = False
        while not finished:
            card, finished = record_card(column.color)
            if card:
                column.add_card(card)
            print([f"{card.suit} {card.value}" for card in column.stack])
        score += column.score_col()
        print(f"Current score: {score}.")
    return score


def record_card(suit:str) -> Tuple[Optional[Card], bool]:
    data = input("Enter bet, a number 2-10. If you are finished hit enter.")
    finished = False
    if not data.strip():
        return None, True
    try:
        card = LostCitiesCard(suit=suit, value=data)
        if card.value == 10:

            finished = True
    except ValueError:
        print(f"{data} isn't a valid value.")
        card = None
    return card, finished

