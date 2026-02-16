from ex2.EliteCard import EliteCard
from ex0.CreatureCard import CreatureCard


def create_creature() -> dict[str, CreatureCard]:
    fire_dragon_card = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    goblin_warrior_card = CreatureCard("Goblin Warrior", 2, "Common", 2, 1)
    creatures_cards = {
        "fire_dragon": fire_dragon_card,
        "goblin_warrior": goblin_warrior_card
    }
    return creatures_cards


def playing_arcane(card: EliteCard) -> None:
    print(f"Playing {card.name} ({card.__class__.__name__}):\n")
    print("Combat phase:")
    creatures_cards = create_creature()
    target = creatures_cards["fire_dragon"]
    attack_res = card.attack(target)
    print(f"Attack result: {attack_res}")


def elitecard_capabilities(card_class: EliteCard) -> None:
    print("EliteCard capabilities:")
    interfaces = ["Card", "Combatable", "Magical"]
    for base in card_class.__bases__:
        if base.__name__ in interfaces:
            methods = []
            for name in dir(base):
                if name[0] != "_" and name != "validate_data":
                    methods.append(name)
            methods.sort()
            print(f"- {base.__name__}: {methods}")
    print()


def main() -> None:
    print("=== DataDeck Ability System === \n")
    Arcane_Warrior_card = EliteCard("Arcane Warrior", 5, "Legendary",
                                    7, 5, 3, 0)
    elitecard_capabilities(EliteCard)
    playing_arcane(Arcane_Warrior_card)


if __name__ == "__main__":
    main()
