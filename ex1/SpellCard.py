from ex0.Card import Card
from ex0.Card import CardType
from enum import Enum


class SpellType(Enum):
    DAMAGE = "Damage"
    HEAL = "Heal"
    BUFF = "Buff"
    DEBUFF = "Debuff"
    UNKNOWN_SPELL = "Unknown_spell"

    @classmethod
    def safe_get(cls, value: str):
        try:
            return cls(value)
        except ValueError:
            print(f"{value} of {cls.__name__} is not a define type so"
                  "it would automatically transform into : 'Unknown_spell'")
            return cls.UNKNOWN_SPELL


class SpellCard(Card):

    def __init__(self, name: str, cost: int, rarity: str,
                 effect_type: str) -> None:
        super().__init__(name, cost, rarity)
        self.effect_type = SpellType.safe_get(effect_type)
        self.card_type = CardType.SPELL

    def play(self, game_state: dict) -> dict:
        game_state['mana'] -= self.cost
        play_result = {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": self.effect_type
        }
        return play_result

    def resolve_effect(self, targets: list) -> dict:
        return {
            "effect_resolution": f"{self.name} cast on {targets}",
            }
