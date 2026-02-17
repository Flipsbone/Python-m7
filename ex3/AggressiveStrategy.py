from ex0.Card import CardType
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellType
from ex1.SpellCard import SpellCard
from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def __init__(self, mana: int = 10):
        self.mana = mana

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        current_mana: int = self.mana
        cards_played_names: list[Card] = []
        total_damage: int = 0

        creatures: list[CreatureCard] = [creature for creature
                                         in hand if creature.card_type
                                         == CardType.CREATURE]

        spells: list[SpellCard] = [spell for spell in hand
                                   if spell.card_type == CardType.SPELL
                                   and spell.effect_type == SpellType.DAMAGE]

        creatures.sort(key=lambda creature: creature.cost)
        spells.sort(key=lambda spell: spell.cost, reverse=True)

        if creatures:
            cheapest_creature = creatures[0]
            if cheapest_creature.cost <= current_mana:
                cards_played_names.append(cheapest_creature.name)
                current_mana -= cheapest_creature.cost
                total_damage += cheapest_creature.attack

        if spells:
            best_spell = spells[0]
            if best_spell.cost <= current_mana:
                cards_played_names.append(best_spell.name)
                current_mana -= best_spell.cost
                total_damage += best_spell.damage

        targets = self.prioritize_targets(battlefield)
        target_name = targets[0] if targets else "Enemy Player"

        report = {
            "strategy": self.get_strategy_name(),
            "actions": {
                "cards_played": cards_played_names,
                "mana_used": self.mana - current_mana,
                "targets_attacked": [target_name],
                "damage_dealt": total_damage
            }
        }
        return report

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        others = [target for target in available_targets
                  if target != "Enemy Player"]
        if others:
            return others
        else:
            return available_targets
