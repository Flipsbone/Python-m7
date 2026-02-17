from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable

class TournamentCard(Card, Combatable, Rankable):
    def play(self, game_state: dict) -> dict:
    def attack(self, target) -> dict:
    def calculate_rating(self) -> int:
    def get_tournament_stats(self) -> dict:
    def update_wins(self, wins: int) -> None:
    def update_losses(self, losses: int) -> None:
    def get_rank_info(self) -> dict:
    def defend(self, incoming_damage: int) -> dict:
    def get_combat_stats(self) -> dict: