from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex3.CardFactory import CardFactory


class FantasyCardFactory(CardFactory):
    def __init__(self) -> None:
        self._creatures_data = [
            {"name": "Fire Dragon", "cost": 5, "rarity": "Legendary", "attack": 7, "health": 5},  # noqa: E501
            {"name": "Goblin Warrior", "cost": 2, "rarity": "Common", "attack": 2, "health": 1},  # noqa: E501
            {"name": "Ice Wizard", "cost": 4, "rarity": "Rare", "attack": 3, "health": 4},  # noqa: E501
            {"name": "Lightning Elemental", "cost": 3, "rarity": "Uncommon", "attack": 4, "health": 2},  # noqa: E501
            {"name": "Stone Golem", "cost": 6, "rarity": "Rare", "attack": 5, "health": 8},  # noqa: E501
            {"name": "Shadow Assassin", "cost": 3, "rarity": "Uncommon", "attack": 5, "health": 2},  # noqa: E501
            {"name": "Healing Angel", "cost": 4, "rarity": "Rare", "attack": 2, "health": 6},  # noqa: E501
            {"name": "Forest Sprite", "cost": 1, "rarity": "Common", "attack": 1, "health": 1},  # noqa: E501
        ]

        self._spells_data = [
            {"name": "Lightning Bolt", "cost": 3, "rarity": "Common", "effect_type": "damage"},  # noqa: E501
            {"name": "Fireball", "cost": 4, "rarity": "Uncommon", "effect_type": "damage"},  # noqa: E501
            {"name": "Ice Shard", "cost": 2, "rarity": "Common", "effect_type": "damage"},  # noqa: E501
        ]

        self._artifacts_data = [
            {"name": "Mana Crystal", "cost": 2, "rarity": "Common", "durability": 5, "effect": "Permanent: +1 mana per turn"},  # noqa: E501
            {"name": "Ring of Wisdom", "cost": 4, "rarity": "Rare", "durability": 4, "effect": "Permanent: Draw an extra card each turn"},  # noqa: E501
            {"name": "Staff of Elements", "cost": 6, "rarity": "Legendary", "durability": 7, "effect": "Permanent: +1 spell damage"},  # noqa: E501
        ]

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, str) and (
         name_or_power in self._creatures_data):
            creature_data = self._creatures_data[name_or_power]
        return CreatureCard(
            creature_data["name"],
            creature_data["cost"],
            creature_data["rarity"],
            creature_data["attack"],
            creature_data["health"]
            )

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, str) and (
         name_or_power in self._spells_data):
            spell_data = self._spells_data[name_or_power]
        return CreatureCard(
            spell_data["name"],
            spell_data["cost"],
            spell_data["rarity"],
            spell_data["effect_type"],
            )

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        