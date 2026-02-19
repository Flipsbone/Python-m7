from ex0.Card import Card
from ex0.Card import CardType


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int) -> None:
        super().__init__(name, cost, rarity)
        try:
            self.attack = Card.validate_data(attack)
        except (TypeError, ValueError) as e:
            print(f"Invalid attack : {e}. Using defaults attack = 0 ")
            self.attack = 0
        try:
            self.health = self.validate_data_health(health)
        except (TypeError, ValueError) as e:
            print(f"Invalid health: {e}. Using defaults health = 1")
            self.health = 1

        self.card_type = CardType.CREATURE

    @staticmethod
    def validate_data_health(health: int) -> int:
        if not isinstance(health, int):
            raise TypeError(f"{health} must be an integer")
        if health <= 0:
            raise ValueError(f"{health} must be positif integer")
        return health

    def play(self, game_state: dict) -> dict:
        if not self.is_playable(game_state.get('mana', 0)):
            return {"error": "Not enough mana"}
        game_state['mana'] -= self.cost
        play_result = {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield"
        }
        return play_result

    def attack_target(self, target) -> dict[str, str | int]:
        target.health -= self.attack
        if target.health < 0:
            target.health = 0
        attack_result: dict[str, str | int] = {
            "attacker": self.name,
            "target": target.name,
            "damage_dealt": self.attack,
            "combat_resolved": True
        }
        return attack_result

    def get_card_info(self) -> dict:
        card_info: dict[str, str | int] = super().get_card_info()
        card_info['type'] = self.card_type.value
        card_info['attack'] = self.attack
        card_info['health'] = self.health
        return card_info
