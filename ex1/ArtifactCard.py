from ex0.Card import Card
from ex0.Card import CardType


class ArtifactCard(Card):

    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str) -> None:
        super().__init__(name, cost, rarity)
        if not isinstance(durability, int):
            raise TypeError(f"Error :{durability} must be positif integer")
        if durability <= 0:
            raise ValueError(f"Error :{durability} must be positif integer")
        self.durability = durability
        self.effect = effect
        self.card_type = CardType.ARTIFACT

    def play(self, game_state: dict) -> dict:
        game_state['mana'] -= self.cost
        play_result = {
            "card_played": self.name,
            "mana_used": self.cost,
            "durability": self.durability,
            "effect": self.effect
        }
        return play_result

    def activate_ability(self) -> dict:
        if self.durability > 0:
            self.durability -= 1
            return {
                "artifact": self.name,
                "effect": self.effect,
                "new_durability": self.durability
            }
        else:
            return {
                "activation_failed": "No durability"
            }
