from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform

if __name__ == "__main__":
    p = TournamentPlatform()
    c1 = TournamentCard("Gobelin", 1, "Common", 1, 1, rating=1000)
    c2 = TournamentCard("Dragon", 10, "Epic", 8, 8, rating=1500)
    c3 = TournamentCard("Mage", 5, "Rare", 4, 4, rating=1200)
    p.register_card(c1)
    p.register_card(c2)
    p.register_card(c3)

    leaderboard = p.get_leaderboard()

    print("CLASSEMENT :")
    for card in leaderboard:
        print(f"- {card.name}: {card.rating} pts")
