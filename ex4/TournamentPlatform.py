from ex4.TournamentCard import TournamentCard


class TournamentPlatform ():
    def __init__(self) -> None:
        self.registry_id: dict[str, TournamentCard] = {}
        self.match_count: int = 0
        self.counter: int = 0
        self.status: str = "active"

    def register_card(self, card: TournamentCard) -> str:
        self.counter += 1
        card_id = f"{card.name.lower()}_{self.counter:03}"
        self.registry_id[card_id] = card
        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        self.match_count += 1
        card1 = self.registry_id.get(card1_id, None)
        card2 = self.registry_id.get(card2_id, None)

        if card1 is None or card2 is None:
            return {"error": "Card not found"}

        health_card1 = card1.health_point
        health_card2 = card2.health_point

        attacker, defender = card1, card2

        while attacker.health_point > 0 and defender.health_point > 0:
            attacker.attack(defender)
            if defender.health_point > 0:
                attacker, defender = defender, attacker

        if card1.health_point > 0:
            winner, loser = card1, card2
            winner_id, loser_id = card1_id, card2_id
        else:
            winner, loser = card2, card1
            winner_id, loser_id = card2_id, card1_id

        winner.update_wins(1)
        winner.calculate_rating()
        loser.update_losses(1)
        loser.calculate_rating()

        card1.health_point = health_card1
        card2.health_point = health_card2
        return {
            'winner': winner_id,
            'loser': loser_id,
            'winner_rating': winner.rating,
            'loser_rating': loser.rating
        }

    def get_leaderboard(self) -> list:
        ranking_list: list[TournamentCard] = list(self.registry_id.values())

        lenght_list = len(ranking_list)
        for i in range(lenght_list):
            for j in range(i + 1, lenght_list):
                if ranking_list[i].rating < ranking_list[j].rating:
                    temp = ranking_list[i]
                    ranking_list[i] = ranking_list[j]
                    ranking_list[j] = temp
        return ranking_list

    def generate_tournament_report(self) -> dict:
        all_cards = list(self.registry_id.values())
        total_cards = len(all_cards)

        if total_cards > 0:
            avg_rating = int(
                sum(card.rating for card in all_cards) / total_cards)
            self.status = "active"
        else:
            avg_rating = 0
            self.status = "waiting_for_cards"

        return {
            "total_cards": total_cards,
            "matches_played": self.match_count,
            "avg_rating": avg_rating,
            "platform_status": self.status
        }
