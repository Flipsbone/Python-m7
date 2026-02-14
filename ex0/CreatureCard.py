from ex0.Card import Card
from typing import Dict, Union


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int) -> None:
        super().__init__(name, cost, rarity)
        stats = {"attack": attack, "health": health}
        for stat, value in stats.items():
            if not isinstance(value, int):
                raise TypeError(f"Error :{stat} must be positif integer")
            if value <= 0:
                raise ValueError(f"Error :{stat} must be positif integer")
        self.attack = attack
        self.health = health

    def play(self, game_state: Dict) -> Dict:
        print()
        if not self.is_playable(game_state["mana"]):
            print(f'\nTesting insufficient mana {game_state["mana"]}')
            print("Playable: False\n")
            return {}

        print(f"Playing {self.name} with {game_state['mana']} mana available:")
        print("Playable: True")
        game_state['mana'] -= self.cost
        play_result = {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield"
        }
        return play_result

    def attack_target(self, target) -> Dict[str, str | int]:
        print(f"{self.name} attacks {target.name}")
        target.health -= self.attack
        if target.health < 0:
            target.health = 0
        attack_result: Dict[str, str | int] = {
            "attacker": self.name,
            "target": target.name,
            "damage_dealt": self.attack,
            "combat_resolved": True
        }
        return attack_result

    def get_card_info(self) -> Dict:
        print("CreatureCard Info:")
        card_info: Dict[str, Union[str, int]] = super().get_card_info()
        card_info['type'] = "Creature"
        card_info['attack'] = self.attack
        card_info['health'] = self.health
        print(f"{card_info}")
        return card_info
