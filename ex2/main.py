from ex2.EliteCard import EliteCard
from ex0.CreatureCard import CreatureCard


def create_creature() -> dict[str, CreatureCard]:
    enemy_card = CreatureCard("Enemy", 5, "Legendary", 5, 5)
    goblin_warrior_card = CreatureCard("Goblin Warrior", 2, "Common", 2, 1)
    creatures_cards = {
        "enemy": enemy_card,
        "goblin_warrior": goblin_warrior_card
    }
    return creatures_cards


def playing_arcane(card: EliteCard) -> None:
    print(f"Playing {card.name} ({card.__class__.__name__}):\n")
    print("Combat phase:")
    creatures_cards = create_creature()
    player2 = creatures_cards["enemy"]
    attack_res = card.attack(player2)
    print(f"Attack result: {attack_res}")

    incoming_damage = player2.attack
    defend_res = card.defend(incoming_damage)
    print(f"Defense result: {defend_res}")

    print("\nMagic phase:")
    spell_res = card.cast_spell("Fireball", ["Enemy1", "Enemy2"])
    print(f"Spell cast: {spell_res}")
    channel_res = card.channel_mana(3)
    print(f"Mana channel: {channel_res}\n")


def elitecard_capabilities(card_class: EliteCard) -> None:
    print("EliteCard capabilities:")
    interfaces = ["Card", "Combatable", "Magical"]
    for base in card_class.__bases__:
        if base.__name__ in interfaces:
            methods = []
            for name in dir(base):
                if name[0] != "_" and name not in (
                        "validate_data", "validate_data_health"):
                    methods.append(name)
            methods.sort()
            print(f"- {base.__name__}: {methods}")
    print()


def main() -> None:
    print("=== DataDeck Ability System === \n")
    Arcane_Warrior_card = EliteCard("Arcane Warrior", 5, "Legendary",
                                    7, 5, 3, 4)
    elitecard_capabilities(EliteCard)
    playing_arcane(Arcane_Warrior_card)
    print("Multiple interface implementation successful!")


if __name__ == "__main__":
    main()
