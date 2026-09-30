# Built-In
import random
import copy

# Internal
from systems import Card

# Deck Class
class Deck:
    def __init__(self, types, suits, ranks) -> None:
        self.card_types = types
        self.card_suits = suits
        self.card_ranks = ranks

        self.cards: list[Card] = []
        self.standard_cards: list[Card] = [
            Card(type, suit, rank)
            for type in self.card_types
            for suit in self.card_suits
            for rank in self.card_ranks
        ]

        self.shuffle()
        
    def shuffle(self) -> None:
        self.cards = copy.deepcopy(self.standard_cards)

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card: Card) -> None:
        self.cards.remove(card)

    def draw_card(self) -> Card:
        if len(self.cards) == 0:
            self.shuffle()

        card = random.choice(self.cards)
        self.remove_card(card)

        if len(self.cards) == 0:
            self.shuffle()
        
        return card