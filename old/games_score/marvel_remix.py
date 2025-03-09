from typing import List, Tuple, Optional, Union
from base_models import Card


class MarvelRemix(Card):
    def __init__(self,name:str,suit: str, value: int, tags: List[str], body: str):
        self.name = name
        #maybe use descriptors to control when things are transformed or blanked?
        self._suit = suit
        self._value = value
        self._tags = tags
        self._body = body
        self.blanked = False
    def blank(self):
        self.blanked = True
