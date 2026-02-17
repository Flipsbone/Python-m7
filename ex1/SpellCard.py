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
        power = self.cost
        logs: list[str] = []

        for target in targets:
            try:
                target_name = target.name
            except AttributeError:
                target_name = str(target)
            try:
                if self._spell_type == SpellType.DAMAGE:
                    target.health = max(0, target.health - power)
                    logs.append(f"{target_name}: -{power} HP")
                elif self._spell_type == SpellType.HEAL:
                    target.health += power
                    logs.append(f"{target_name}: +{power} HP")
                elif self._spell_type == SpellType.BUFF:
                    target.attack += power
                    target.health += power
                    logs.append(f"{target_name}: +{power} Stats")
                elif self._spell_type == SpellType.DEBUFF:
                    target.attack = max(0, target.attack - power)
                    logs.append(f"{target_name}: -{power} Stats")
                else:
                    logs.append(f"{target_name}: No effect")
            except AttributeError:
                print(f"{target_name} Error No Pv or attack")
        return {"spell": self.name, "results": logs}
