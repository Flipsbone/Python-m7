from ex3.GameEngine import GameEngine
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy


def main():
    print("=== DataDeck Game Engine ===\n")
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
    display_hand = [f"{card.name} ({card.cost})" for card in hand]
    print(f"Hand: [{', '.join(display_hand)}]\n")

    print("Turn execution:")
    print(f"Strategy: {report['strategy']}")
    print(f"Actions: {report['actions']}\n")
    print(f"Game Report:\n {engine.get_engine_status()}")
    print("\nAbstract Factory + Strategy Pattern:"
          "Maximum flexibility achieved!")


if __name__ == "__main__":
    main()
