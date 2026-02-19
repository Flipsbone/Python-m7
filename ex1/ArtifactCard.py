from ex0.Card import Card
from ex0.Card import CardType


class ArtifactCard(Card):

    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str) -> None:
        super().__init__(name, cost, rarity)
        try:
            self.durability = Card.validate_data(durability)
        except (TypeError, ValueError) as e:
            print(f"Invalid durability : {e}. Using defaults durability = 0 ")
            self.durability = 0
        self.effect = effect
        self._card_type = CardType.ARTIFACT

    def play(self, game_state: dict) -> dict:
        result = super().play(game_state)
        if "error" in result:
            return result

        play_result = {
            "card_played": self.name,
            "mana_used": self.cost,
            "durability": self.durability,
            "effect": self.effect
        }
        return play_result

    def activate_ability(self) -> dict:
        if self.durability <= 0:
            return {"activation_failed": "No durability left"}

        self.durability -= 1

        effect_lower = self.effect.lower()
        action_data: dict[str, int | str] = {}

        if "mana" in effect_lower:
            action_data = {
                "action": "add_mana",
                "value": 1,
                "target": "player"
            }

        elif "attack" in effect_lower:
            val = 2 if "2" in effect_lower else 1
            action_data = {
                "action": "buff_attack",
                "value": val,
                "target": "equipped_creature"
            }

        elif "health" in effect_lower:
            val = 3 if "3" in effect_lower else 1
            action_data = {
                "action": "buff_health",
                "value": val,
                "target": "all_friendly_creatures"
            }

        elif "draw" in effect_lower:
            action_data = {
                "action": "draw_card",
                "value": 1,
                "target": "player"
            }

        elif "cost" in effect_lower:
            action_data = {
                "action": "reduce_cost",
                "value": 1,
                "target": "hand"
            }

        else:
            return {
                "action": "new_activation",
                "description": self.effect
            }

        return {
                "artifact": self.name,
                "effect": action_data,
                "new_durability": self.durability
            }

    def get_card_info(self) -> dict:
        card_info: dict[str, str | int] = super().get_card_info()
        card_info.update({
            "type": self._card_type.value,
            "durability": self.durability,
            "effect": self.effect
        })
        return card_info
