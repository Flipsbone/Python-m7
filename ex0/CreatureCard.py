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
            self.health = Card.validate_data_health(health)
        except (TypeError, ValueError) as e:
            print(f"Invalid health: {e}. Using defaults health = 1")
            self.health = 1

        self._card_type = CardType.CREATURE

    def play(self, game_state: dict) -> dict:
        result = super().play(game_state)
        if "error" in result:
            return result

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
        card_info.update({
            "type": self._card_type.value,
            "attack": self.attack,
            "health": self.health
        })
        return card_info
