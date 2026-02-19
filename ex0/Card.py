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
    def get_rarity(cls, string: str) -> "CardRarity":
        if not isinstance(string, str):
            print(f"Warning: '{string}' is not a valid rarity. "
                  "Defaulting to 'Unknown_rarity'.")
            return cls.UNKNOWN_RARITY

        key = string.upper().strip()

        if key in cls.__members__:
            return cls[key]

        print(f"Warning: '{string}' is not a valid rarity. "
              "Defaulting to 'Unknown_rarity'.")
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
            print(f"Error cost : {e}")
            self.cost = 0

        self._rarity = CardRarity.get_rarity(rarity)

    @staticmethod
    def validate_data(cost: int) -> int:
        if not isinstance(cost, int):
            raise TypeError(f"{cost} must be an integer")
        if cost < 0:
            raise ValueError(f"{cost} must be 0 or more")
        return cost

    @staticmethod
    def validate_data_health(health: int) -> int:
        if not isinstance(health, int):
            raise TypeError(f"{health} must be an integer")
        if health <= 0:
            raise ValueError(f"{health} must be positif integer")
        return health

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        if not self.is_playable(game_state.get('mana', 0)):
            return {"error": "Not enough mana"}

        game_state['mana'] -= self.cost
        return {"status": "success"}

    def get_card_info(self) -> dict:
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self._rarity.value,
        }

    def is_playable(self, available_mana: int) -> bool:
        return available_mana >= self.cost
