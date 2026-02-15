from ex0.CreatureCard import CreatureCard


def play_card(
        creatures_cards: dict[str, CreatureCard],
        game_state: dict[str, int]) -> None:
    play_result = creatures_cards["fire_dragon"].play(game_state)
    print(f"{play_result}\n")
    attack_result = (
        creatures_cards["fire_dragon"].attack_target(
            creatures_cards["goblin_warrior"])
        )
    print(f"{attack_result}\n")
    if game_state["mana"] < creatures_cards["fire_dragon"].cost:
        print(f"Testing insufficient mana ({game_state["mana"]} available)")
        print("Playable: False\n")


def creaturecard_info(creatures_cards: dict[str, CreatureCard]) -> None:
    print("Testing Abstract Base Class Design:")
    creatures_cards["fire_dragon"].get_card_info()


def init_game_state() -> dict[str, int]:
    game_state = {
        "mana": 8
    }
    return game_state


def created_creature() -> dict[str, CreatureCard]:
    fire_dragon_card = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    goblin_warrior_card = CreatureCard("Goblin Warrior", 2, "Common", 2, 1)
    creatures_cards = {
        "fire_dragon": fire_dragon_card,
        "goblin_warrior": goblin_warrior_card
    }
    return creatures_cards


def main() -> None:
    print("=== DataDeck Card Foundation ===\n")
    creatures_cards = created_creature()
    creaturecard_info(creatures_cards)
    game_state = init_game_state()
    play_card(creatures_cards, game_state)
    print("Abstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
