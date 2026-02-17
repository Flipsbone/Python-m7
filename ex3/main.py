from ex3.GameEngine import GameEngine
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy


def main():
    engine = GameEngine()
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()

    engine.configure_engine(factory, strategy)
    print(f"Factory: {factory.__class__.__name__}")
    print(f"Strategy: {strategy.get_strategy_name()}")
    print(f"Available types: {factory.get_supported_types()}")

    report = engine.simulate_turn()
    print("\nSimulating aggressive turn...")
    hand = report.get("current_hand", [])
    display_hand = [f"{c.name} ({c.cost})" for c in hand]
    print(f"Hand: [{', '.join(display_hand)}]")

    print("Turn execution:")
    print(f"Strategy: {report['strategy']}")
    print(f"Actions: {report['actions']}\n")
    print(f"Game Report:\n {engine.get_engine_status()}")


if __name__ == "__main__":
    main()
