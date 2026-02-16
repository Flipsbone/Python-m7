from ex0.Card import Card
from ex0.Card import CardType
from ex0.CreatureCard import CreatureCard
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):

    def __init__(
            self, name: str, cost: int,
            rarity: str, attack: int,
            health: int, defend: int,
            initial_mana: int,
            ) -> None:
        super().__init__(name, cost, rarity)

        try:
            EliteCard.validate_data(attack, health, defend, initial_mana)
        except (TypeError, ValueError) as e:
            print({e})
            attack, health, defend, initial_mana = 0, 1, 0, 0

        self.attack_power = attack
        self.health = health
        self.defend_resistance = defend
        self.mana_pool = initial_mana
        self._spells = {"Fireball": 4, "Heal": 3, "Shield": 2}
        self.type = CardType.ELITE

    @staticmethod
    def validate_data(
            attack: int, health: int, defend: int, initial_mana: int) -> None:
        stats = {
            "attack": attack, "defend": defend, "mana": initial_mana
            }
        for stat, value in stats.items():
            if not isinstance(value, int):
                raise TypeError(f"Error :{stat} must be an integer")
            if value < 0:
                raise ValueError(f"Error :{stat} must be 0 or more")

        if not isinstance(health, int):
            raise TypeError(f"Error :{stat} must be integer")
        if health <= 0:
            raise ValueError(f"Error :{stat} must be positif integer")

    def play(self, game_state: dict) -> dict:
        game_state['mana'] -= self.cost
        play_result = {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": ("Elite card entered the battlefield with"
                       "combat and magic abilities")
        }
        return play_result

    def attack(self, target: "EliteCard | CreatureCard") -> dict:
        damage = self.attack_power

        target.health -= damage
        if target.health < 0:
            target.health = 0
        attack_result: dict[str, str | int] = {
            "attacker": self.name,
            "target": target.name,
            "damage": damage,
            "combat_type": "melee"
        }
        return attack_result

    def defend(self, incoming_damage: int) -> dict:
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

    def get_combat_stats(self) -> dict:
        return {
            "damage": self.attack_power,
            "defense": self.defend_resistance,
            "health": self.health
            }

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        mana_cost = self._spells.get(spell_name, 0)
        spell_result: dict[str, str | int] = {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": mana_cost
        }
        return spell_result

    def channel_mana(self, amount: int) -> dict:
        self.mana_pool += amount
        if self.mana_pool > 10:
            self.mana_pool = 10
        channel_mana_result = {
            "channeled": amount,
            "total_mana": self.mana_pool
        }
        return channel_mana_result

    def get_magic_stats(self) -> dict:
        return {"mana_pool": self.mana_pool}
