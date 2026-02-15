from ex0.Card import Card


class ArtifactCard(Card):

    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str) -> None:
        super().__init__(name, cost, rarity)
        if not isinstance(durability, int):
            raise TypeError(f"Error :{durability} must be positif integer")
        if durability <= 0:
            raise ValueError(f"Error :{durability} must be positif integer")
        self.durability = durability
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        print()
        if not self.is_playable(game_state["mana"]):
            print(f'\nTesting insufficient mana {game_state["mana"]}')
            print("Playable: False\n")
            return {}

        game_state['mana'] -= self.cost

        play_result = {
            "card_played": self.name,
            "mana_used": self.cost,
            "durability": self.durability,
            "effect": self.effect
        }
        return play_result

    def activate_ability(self) -> dict:
        if self.durability > 0:
            self.durability -= 1
            return {
                "artifact": self.name,
                "effect": self.effect,
                "new_durability": self.durability
            }
        else:
            return {
                "activation_failed": "No durability"
            }
