from abc import ABC, abstractmethod
from enum import Enum


class CardRarity(Enum):
    COMMON = "Common"
    UNCOMMON = "Uncommon"
    RARE = "Rare"
    EPIC = "Epic"
    LEGENDARY = "Legendary"
    UNKNOWN_RARITY = "Unknown_rarity"

    @classmethod
    def safe_get(cls, value: str):
        try:
            return cls(value)
        except ValueError:
            print(f"{value} of {cls.__name__} is not a define type so"
                  "it would automatically transform into rarity:"
                  "'Unknown_rarity'")
            return cls.UNKNOWN_RARITY


class CardType(Enum):
    CREATURE = "Creature"
    SPELL = "Spell"
    ARTIFACT = "Artifact"
    ELITE = "Elite"


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self.name = name
        try:
            Card.validate_data(cost)
            self.cost = cost
        except (TypeError, ValueError) as e:
            print({e})
            self.cost = 0

        self.rarity = CardRarity.safe_get(rarity)

    @staticmethod
    def validate_data(cost: int) -> None:
        if not isinstance(cost, int):
            raise TypeError(f"Error :{cost} must be an integer")
        if cost < 0:
            raise ValueError(f"Error :{cost} must be 0 or more")

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
