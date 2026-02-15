from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
import random


class Deck:
    def __init__(self) -> None:
        self.cards = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        return self.cards.pop()

    def get_deck_stats(self) -> dict:
        deck_stats: dict[str, str | int] = {
            'total_cards': 0,
            'creatures': 0,
            'artifacts': 0,
            'spells': 0,
            'avg_cost': 0
        }
        for card in self.cards:
            deck_stats['total_cards'] += 1
            if isinstance(card, CreatureCard):
                deck_stats['creatures'] += 1
                deck_stats['avg_cost'] += card.cost
            elif isinstance(card, ArtifactCard):
                deck_stats['artifacts'] += 1
                deck_stats['avg_cost'] += card.cost
            elif isinstance(card, SpellCard):
                deck_stats['spells'] += 1
                deck_stats['avg_cost'] += card.cost
        try:
            if deck_stats['total_cards'] == 0:
                raise ZeroDivisionError("no cards provid")
            deck_stats['avg_cost'] = (
                round(deck_stats['avg_cost'] / deck_stats['total_cards'], 1))
        except ZeroDivisionError as e:
            print(f"{e}")
        return deck_stats
