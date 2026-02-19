from ex0.Card import Card
from ex0.Card import CardType
from ex0.CreatureCard import CreatureCard
from ex2.Magical import Magical
from ex2.Combatable import Combatable


class EliteCard(Card, Combatable, Magical):

    def __init__(
            self, name: str, cost: int,
            rarity: str, attack: int = 0,
            health: int = 1, armor: int = 0,
            initial_mana: int = 0,
            ) -> None:
        super().__init__(name, cost, rarity)

        try:
            self.attack_power = Card.validate_data(attack)
        except (TypeError, ValueError) as e:
            print(f"Invalid attack : {e}. Using defaults attack = 0 ")
            self.attack = 0
        try:
            self.health = Card.validate_data_health(health)
        except (TypeError, ValueError) as e:
            print(f"Invalid health: {e}. Using defaults health = 1")
            self.health = 1
        try:
            self.armor_value = Card.validate_data(armor)
        except (TypeError, ValueError) as e:
            print(f"Invalid armor : {e}. Using defaults armor = 0 ")
            self.armor_value = 0
        try:
            self.mana_pool = Card.validate_data(initial_mana)
        except (TypeError, ValueError) as e:
            print(f"Invalid initial_mana: {e}.Using defaults initial_mana = 0")
            self.mana_pool = 0

        self._spells = {"Fireball": 4, "Heal": 3, "Shield": 2}
        self._card_type = CardType.ELITE

    def play(self, game_state: dict) -> dict:
        result = super().play(game_state)
        if "error" in result:
            return result

        play_result = {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": ("Elite card entered the battlefield with"
                       "combat and magic abilities")
        }
        return play_result

    def attack(self, target: "EliteCard | CreatureCard") -> dict:
        damage = self.attack_power
        if isinstance(target, Combatable):
            defense_info = target.defend(damage)
            damage_dealt = defense_info["damage_taken"]
        else:
            previous_health = target.health
            target.health -= damage
            if target.health < 0:
                target.health = 0
            damage_dealt = previous_health - target.health

        attack_result: dict[str, str | int] = {
            "attacker": self.name,
            "target": target.name,
            "damage": damage_dealt,
            "combat_type": "melee"
        }
        return attack_result

    def defend(self, incoming_damage: int) -> dict:
        damage_blocked = min(incoming_damage, self.armor_value)
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
            "defense": self.armor_value,
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

    def get_card_info(self) -> dict:
        card_info: dict[str, str | int] = super().get_card_info()
        card_info.update({
            "type": self._card_type.value,
            "attack": self.attack_power,
            "health": self.health,
            "armor": self.armor_value,
            "mana_pool": self.mana_pool
        })
        return card_info
