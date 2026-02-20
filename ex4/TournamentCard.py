from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int, armor: int) -> None:
        super().__init__(name, cost, rarity)

        self.wins: int = 0
        self.losses: int = 0
        self.rating: int = 1200

        try:
            self.attack_value = Card.validate_data(attack)
        except (TypeError, ValueError) as e:
            print(f"Invalid attack : {e}. Using defaults attack = 0 ")
            self.attack = 0
        try:
            self.health_point = Card.validate_data_health(health)
        except (TypeError, ValueError) as e:
            print(f"Invalid health: {e}. Using defaults health = 1")
            self.health_point = 1
        try:
            self.armor_value = Card.validate_data(armor)
        except (TypeError, ValueError) as e:
            print(f"Invalid armor : {e}. Using defaults armor = 0 ")
            self.armor_value = 0

    def play(self, game_state: dict) -> dict:
        game_state['mana'] -= self.cost
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Tournament Card enters the battlefield"
        }

    def attack(self, target) -> dict:
        damage = self.attack_value
        defense_info = target.defend(damage)

        attack_result: dict[str, str | int] = {
            "attacker": self.name,
            "target": target.name,
            "damage_dealt": defense_info["damage_taken"],
            "combat_type": "melee"
        }
        return attack_result

    def calculate_rating(self) -> int:
        base_rating = 1200
        self.rating = base_rating + (self.wins * 16) - (self.losses * 16)
        return self.rating

    def get_tournament_stats(self) -> dict:
        return {
            "rating": self.rating,
            "wins": self.wins,
            "losses": self.losses,
         }

    def update_wins(self, wins: int) -> None:
        self.wins += wins

    def update_losses(self, losses: int) -> None:
        self.losses += losses

    def get_rank_info(self) -> dict:
        return {
            "name": self.name,
            "rating": self.rating,
            "games_stats": (self.wins-self.losses)
        }

    def defend(self, incoming_damage: int) -> dict:
        damage_blocked = min(incoming_damage, self.armor_value)
        damage_taken = incoming_damage - damage_blocked
        self.health_point -= damage_taken
        if self.health_point < 0:
            self.health_point = 0

        defend_result: dict[str, str | int] = {
            "defender": self.name,
            "damage_taken": damage_taken,
            "damage_blocked": damage_blocked,
            "still_alive": self.health_point > 0
        }
        return defend_result

    def get_combat_stats(self) -> dict:
        return {
            "health": self.health_point,
            "attack": self.attack_value,
            "armor": self.armor_value
        }

    @classmethod
    def get_interfaces(cls) -> list:
        return [base.__name__ for base in cls.__bases__]
