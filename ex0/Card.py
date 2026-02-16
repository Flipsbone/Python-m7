from abc import ABC, abstractmethod
from enum import Enum


class CardRarity(Enum):
    COMMON = "Common"
    UNCOMMON = "Uncommon"
    RARE = "Rare"
    EPIC = "Epic"
    LEGENDARY = "Legendary"

    @classmethod
    def safe_get(cls, value: str):
        try:
            return cls(value)
        except ValueError:
            print(f"{value} of {cls.__name__} is not a define type so"
                  "it would automatically transform into rarity: 'Common'")
            return cls.COMMON


class CardType(Enum):
    CREATURE = "Creature"
    SPELL = "Spell"
    ARTIFACT = "Artifact"
    ELITE = "Elite"


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self.name = name
        self.cost = cost
        self.rarity = CardRarity.safe_get(rarity)

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        pass

    def get_card_info(self) -> dict:
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity.value,
        }

    def is_playable(self, available_mana: int) -> bool:
        return available_mana >= self.cost
