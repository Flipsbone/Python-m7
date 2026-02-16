from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical

class EliteCard(Card, Combatable, Magical):

    def __init__(self, name: str, cost: int, rarity: str, attack: int, health: int, defend: int, mana_power: int) -> None:
        super().__init__(name, cost, rarity)
        stats = {"attack": attack, "health": health, "defend": defend, "mana_power": mana_power}
        for stat, value in stats.items():
            if not isinstance(value, int):
                raise TypeError(f"Error :{stat} must be positif integer")
            if value <= 0:
                raise ValueError(f"Error :{stat} must be positif integer")
        self.attack_power = attack
        self.defend_resistance = defend
        self.health = health
        self.mana_power = mana_power
        self._spells = {"Fireball": 4, "Heal": 3, "Shield": 2}

    def play(self, game_state: dict) -> dict:
        pass

    def attack(self, target) -> dict:
        damage = self.attack_power
        
        target.health -= damage
        if target.health < 0:
            target.health = 0
        attack_result: dict[str, str | int] = {
            "attacker": self.name,
            "target": target.name,
            "damage_dealt": damage,
            "combat_type": "melee"
        }
        return attack_result
    
    def defend(self, incoming_damage) -> dict:
        damage_blocked = min(incoming_damage, self.defend_resistance)
        damage_taken = incoming_damage - damage_blocked
        self.health -= damage_taken
        if self.health < 0:
            self.health = 0
        
        defend_result: dict[str, str | int] = {
            "defender": self.name,
            "damage_taken": damage_taken,
            "damage_blocked": damage_blocked,
            "still_alive": self.health > 0
        }
        return defend_result
    
    def cast_spell(self, spell_name: str, targets: list) -> dict:
        mana_cost = self._spells.get(spell_name, 0)
        spell_result: dict[str, str | int] = {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets
            "mana_used": mana_cost
        }