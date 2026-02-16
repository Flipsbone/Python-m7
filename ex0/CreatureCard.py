from ex0.Card import Card
from ex0.Card import CardType


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int) -> None:
        super().__init__(name, cost, rarity)
        try:
            CreatureCard.validate_data(attack, health)
        except (TypeError, ValueError) as e:
            print({e})
            attack, health = 0, 1
        self.attack = attack
        self.health = health
        self.card_type = CardType.CREATURE

    @staticmethod
    def validate_data(attack: int, health: int) -> None:
        if not isinstance(attack, int):
            raise TypeError(f"Error :{attack} must be an integer")
        if attack < 0:
            raise ValueError(f"Error :{attack} must be 0 or more")

        if not isinstance(health, int):
            raise TypeError(f"Error :{health} must be integer")
        if health <= 0:
            raise ValueError(f"Error :{health} must be positif integer")

    def play(self, game_state: dict) -> dict:
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
