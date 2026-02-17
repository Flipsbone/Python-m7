from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex3.CardFactory import CardFactory


class FantasyCardFactory(CardFactory):
    def __init__(self) -> None:
        self._creatures = {
            "Dragon": {"name": "Fire Dragon", "cost": 5, "rarity": "Legendary", "attack": 7, "health": 5},  # noqa: E501
            "Goblin": {"name": "Goblin Warrior", "cost": 2, "rarity": "Common", "attack": 2, "health": 1},  # noqa: E501
            "Wizard": {"name": "Ice Wizard", "cost": 4, "rarity": "Rare", "attack": 3, "health": 4},  # noqa: E501
            "Elemental": {"name": "Lightning Elemental", "cost": 3, "rarity": "Uncommon", "attack": 4, "health": 2},  # noqa: E501
            "Golem": {"name": "Stone Golem", "cost": 6, "rarity": "Rare", "attack": 5, "health": 8},  # noqa: E501
            "Assasin": {"name": "Shadow Assassin", "cost": 3, "rarity": "Uncommon", "attack": 5, "health": 2},  # noqa: E501
            "Angel": {"name": "Healing Angel", "cost": 4, "rarity": "Rare", "attack": 2, "health": 6},  # noqa: E501
            "Sprite": {"name": "Forest Sprite", "cost": 1, "rarity": "Common", "attack": 1, "health": 1},  # noqa: E501
        }

        self._spells = {
            "Bolt": {"name": "Lightning Bolt", "cost": 3, "rarity": "Common", "effect_type": "damage"},  # noqa: E501
            "Fireball": {"name": "Fireball", "cost": 4, "rarity": "Uncommon", "effect_type": "damage"},  # noqa: E501
            "Ice": {"name": "Ice Shard", "cost": 2, "rarity": "Common", "effect_type": "damage"},  # noqa: E501
        }

        self._artifacts = {
            "Crystal": {"name": "Mana Crystal", "cost": 2, "rarity": "Common", "durability": 5, "effect": "Permanent: +1 mana per turn"},  # noqa: E501
            "Ring": {"name": "Ring of Wisdom", "cost": 4, "rarity": "Rare", "durability": 4, "effect": "Permanent: Draw an extra card each turn"},  # noqa: E501
            "Staff": {"name": "Staff of Elements", "cost": 6, "rarity": "Legendary", "durability": 7, "effect": "Permanent: +1 spell damage"},  # noqa: E501
        }

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        creature_data = self._find_data(self._creatures, name_or_power)
        return CreatureCard(
            creature_data["name"],
            creature_data["cost"],
            creature_data["rarity"],
            creature_data["attack"],
            creature_data["health"]
            )

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        spell_data = self._find_data(self._spells, name_or_power)
        return SpellCard(
            spell_data["name"],
            spell_data["cost"],
            spell_data["rarity"],
            spell_data["effect_type"],
            )

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        artifact_data = self._find_data(self._artifacts, name_or_power)
        return ArtifactCard(
            artifact_data["name"],
            artifact_data["cost"],
            artifact_data["rarity"],
            artifact_data["durability"],
            artifact_data["effect"],
        )

    @staticmethod
    def _find_data(registry: dict, key: str | int | None) -> dict:
        if not registry:
            raise ValueError("Registry is empty")
        default_card = list(registry.values())[0]

        if isinstance(key, str):
            return registry.get(key.capitalize(), list(registry.values())[0])
        if isinstance(key, int):
            match = next((value for value in registry.values()
                          if value["cost"] == key), None)
            return match if match else list(registry.values())[0]
        return default_card

    def get_supported_types(self) -> dict:
        return {
            "creatures": list(self._creatures.keys()),
            "spells": list(self._spells.keys()),
            "artifacts": list(self._artifacts.keys())
        }

    def create_themed_deck(self, size: int) -> dict:
        deck = []
        for i in range(size):
            cycle_index = i % 3
            if cycle_index == 0:
                deck.append(self.create_creature())
            elif cycle_index == 1:
                deck.append(self.create_spell())
            else:
                deck.append(self.create_artifact())
        return {
            "deck_name": "Fantasy Deck",
            "cards": deck,
            "size": len(deck)
        }
