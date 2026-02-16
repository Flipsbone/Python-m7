from ex0.CreatureCard import CreatureCard


def play_card(
        creatures_cards: dict[str, CreatureCard],
        game_state: dict[str, int]) -> None:

    dragon = creatures_cards["fire_dragon"]
    goblin = creatures_cards["goblin_warrior"]
    if not dragon.is_playable(game_state["mana"]):
            print(f"Testing insufficient mana {game_state['mana']}")
            print("Playable: False\n")
            return

    print(f"Playing {dragon.name} with {game_state['mana']} mana available:")
    print("Playable: True")

    play_result = creatures_cards["fire_dragon"].play(game_state)
    print(f"Play result: {play_result}\n")
    print(f"{dragon.name} attacks {goblin.name}")
    attack_result = (dragon.attack_target(goblin))
    print(f"{attack_result}\n")


def creaturecard_info(creatures_cards: dict[str, CreatureCard]) -> None:
    print("Testing Abstract Base Class Design:\n")
    print("CreatureCard Info:")
    print(creatures_cards["fire_dragon"].get_card_info(), end="\n\n")


def init_game_state() -> dict[str, int]:
    game_state = {
        "mana": 8
    }
    return game_state


def create_creature() -> dict[str, CreatureCard]:
    fire_dragon_card = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    goblin_warrior_card = CreatureCard("Goblin Warrior", 2, "Common", 2, 1)
    creatures_cards = {
        "fire_dragon": fire_dragon_card,
        "goblin_warrior": goblin_warrior_card
    }
    return creatures_cards


def main() -> None:
    print("=== DataDeck Card Foundation ===\n")
    creatures_cards = create_creature()
    creaturecard_info(creatures_cards)
    game_state = init_game_state()
    play_card(creatures_cards, game_state)
    play_card(creatures_cards, game_state)
    print("Abstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
