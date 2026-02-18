from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    def __init__(self) -> None:
        self._factory: CardFactory | None = None
        self._strategy: GameStrategy | None = None
        self._turns_simulated = 0
        self._total_damage = 0
        self._cards_created = 0

    def configure_engine(
            self, factory: CardFactory, strategy: GameStrategy) -> None:

        self._factory = factory
        self._strategy = strategy
        print("Configuring Fantasy Card Game...")

    def simulate_turn(self) -> dict:
        if not self._factory or not self._strategy:
            raise ValueError(
                "Engine must be configured with a factory and strategy.")
        hand = [
            self._factory.create_creature("dragon"),
            self._factory.create_creature("goblin"),
            self._factory.create_spell("bolt")
        ]
        self._cards_created += len(hand)

        enemy_player = type(
            'Target', (),
            {'name': 'Enemy Player', 'attack': 1, 'health': 30})()
        battlefield = [enemy_player]

        turn_report = self._strategy.execute_turn(hand, battlefield)
        turn_report["current_hand"] = hand

        self._turns_simulated += 1
        self._total_damage += turn_report.get(
            "actions", {}).get("damage_dealt", 0)

        return turn_report

    def get_engine_status(self) -> dict:
        return {
            "turns_simulated": self._turns_simulated,
            "strategy_used": (self._strategy.get_strategy_name()
                              if self._strategy else None),
            "total_damage": self._total_damage,
            "cards_created": self._cards_created
        }
