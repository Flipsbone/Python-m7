from ex0.Card import Card
from ex0.Card import CardType
from ex0.CreatureCard import CreatureCard
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):

    def __init__(
            self, name: str, cost: int,
            rarity: str, attack: int = 0,
            health: int = 1, defend: int = 0,
            initial_mana: int = 0,
            ) -> None:
        super().__init__(name, cost, rarity)

        try:
            self.attack_power = EliteCard.validate_data(attack)
            self.health = EliteCard.validate_data_health(health)
            self.defend_resistance = EliteCard.validate_data(defend)
            self.mana_pool = EliteCard.validate_data(initial_mana)
        except (TypeError, ValueError) as e:
            print(f"Invalid data: {e}. Using defaults.")
            self.attack_power = 0
            self.defend_resistance = 0
            self.health = 1
            self.mana_pool = 0

        self._spells = {"Fireball": 4, "Heal": 3, "Shield": 2}
        self.type = CardType.ELITE

    @staticmethod
    def validate_data(value: int) -> int:
        if not isinstance(value, int):
            raise TypeError(f"Error :{value} must be an integer")
        if value < 0:
            raise ValueError(f"Error :{value} must be positif integer")
        return value

    @staticmethod
    def validate_data_health(health: int) -> int:
        if not isinstance(health, int):
            raise TypeError(f"Error :{health} must be an integer")
        if health <= 0:
            raise ValueError(f"Error :{health} must be more than 0")
        return health

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
        defense_info = target.defend(damage)

        attack_result: dict[str, str | int] = {
            "attacker": self.name,
            "target": target.name,
            "damage_dealt": defense_info["damage_taken"],
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
