from ex0.Card import Card
from ex0.Card import CardType


class SpellCard(Card):

    def __init__(self, name: str, cost: int, rarity: str,
                 effect_type: str) -> None:
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type
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
