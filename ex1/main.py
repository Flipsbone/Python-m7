from ex0.CreatureCard import CreatureCard
from ex1 import Deck, SpellCard, ArtifactCard


def building_deck(my_deck: Deck) -> None:
    fire_dragon_card = create_creature()['fire_dragon']
    lightning_bolt_card = create_spell()['lightning_bolt']
    mana_crystal_card = create_artifact()['mana_crystal']

    my_deck.add_card(fire_dragon_card)
    my_deck.add_card(lightning_bolt_card)
    my_deck.add_card(mana_crystal_card)
    my_deck.get_deck_stats()
    print(f"Deck stats: {my_deck.get_deck_stats()}")


def create_artifact() -> dict[str, ArtifactCard]:
    mana_crystal_card = ArtifactCard(
        'Mana Crystal', 2, 'Common', 5, 'Permanent, +1 mana per turn')

    artifact_cards = {
        "mana_crystal": mana_crystal_card
    }
    return artifact_cards


def create_spell() -> dict[str, SpellCard]:
    lightning_bolt_card = SpellCard("Lightning Bolt", 3, "Common", "damage")
    spell_cards = {
        "lightning_bolt": lightning_bolt_card
    }
    return spell_cards


def create_creature() -> dict[str, CreatureCard]:
    fire_dragon_card = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    creatures_cards = {
        "fire_dragon": fire_dragon_card
    }
    return creatures_cards


def init_game_state() -> dict[str, int]:
    game_state = {
        "mana": 8
    }
    return game_state


def main():
    print("=== DataDeck Deck Builder ===")
    my_deck = Deck()
    game_state = init_game_state()
    print("Building deck with different card types...")
    building_deck(my_deck)

if __name__ == "__main__":
    main()
