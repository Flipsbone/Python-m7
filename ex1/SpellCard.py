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
    def get_type(cls, string: str) -> "SpellType":
        if not isinstance(string, str):
            print(f"Warning: '{string}' is not a valid spell "
                  "Defaulting to 'Unknown_spell'.")
            return cls.UNKNOWN_SPELL

        key = string.upper().strip()

        if key in cls.__members__:
            return cls[key]

        print(f"Warning: '{string}' is not a valid spell. "
              "Defaulting to 'Unknown_spell'.")
        return cls.UNKNOWN_SPELL


class SpellCard(Card):

    def __init__(self, name: str, cost: int, rarity: str,
                 effect_type: str) -> None:
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type
        self._spell_type = SpellType.get_type(self.effect_type)
        self._card_type = CardType.SPELL

    def play(self, game_state: dict) -> dict:
        result = super().play(game_state)
        if "error" in result:
            return result

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

    def get_card_info(self) -> dict:
        card_info: dict[str, str | int] = super().get_card_info()
        card_info.update({
            "type": self._card_type.value,
            "spell type": self._spell_type.value,
        })
        return card_info
