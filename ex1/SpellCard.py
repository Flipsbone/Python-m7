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
    def safe_get(cls, string: str):
        mapping = {
            "damage": cls.DAMAGE,
            "heal": cls.HEAL,
            "buff": cls.BUFF,
            "debuff": cls.DEBUFF
        }

        lower_string = string.lower()
        for keyword, s_type in mapping.items():
            if keyword in lower_string:
                return s_type
        print(f"{string} of {cls.__name__} is not a define type so "
              "it would automatically transform into : 'Unknown_spell'")
        return cls.UNKNOWN_SPELL


class SpellCard(Card):

    def __init__(self, name: str, cost: int, rarity: str,
                 effect_type: str) -> None:
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type
        self._spell_type = SpellType.safe_get(self.effect_type)
        self.card_type = CardType.SPELL

    def play(self, game_state: dict) -> dict:
        game_state['mana'] -= self.cost
        play_result = {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect_type": self.effect_type
        }
        return play_result

    def resolve_effect(self, targets: list) -> dict:
        return {
            "effect_resolution": f"{self.name} cast on {targets}",
            }
