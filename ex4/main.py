from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def global_report(platform: TournamentPlatform) -> None:
    print("\nPlatform Report:")
    report = platform.generate_tournament_report()
    print(f"{report}\n")


def leaderboard(platform: TournamentPlatform) -> None:
    print("Tournament Leaderboard:")
    leaderboard = platform.get_leaderboard()
    for i, card_info in enumerate(leaderboard, 1):
        print(f"{i}. {card_info.name} - Rating: {card_info.rating}"
              f"({card_info.wins}-{card_info.losses})")


def match(platform: TournamentPlatform,
          id1: TournamentCard,
          id2: TournamentCard
          ) -> None:
    print("Creating tournament match...")
    match_result = platform.create_match(id1, id2)
    print(f"Match result: {match_result}\n")


def tournament_cards(platform: TournamentPlatform) -> list:
    print("Registering Tournament Cards...\n")
    list_id: list[TournamentCard] = []
    c1 = TournamentCard("Fire Dragon", cost=8, rarity="Epic",
                        attack=10, health=50, rating=1200)
    c2 = TournamentCard("Ice Wizard", cost=5, rarity="Rare",
                        attack=6, health=30, rating=1150)
    id1 = platform.register_card(c1)
    list_id.append(id1)
    id2 = platform.register_card(c2)
    list_id.append(id2)

    for card_id, card in [(id1, c1), (id2, c2)]:
        print(f"{card.name} (ID: {card_id}):")
        interfaces_str = ", ".join(card.get_interfaces())
        print(f"- Interfaces: [{interfaces_str}]")
        print(f"- Rating: {card.rating}")
        stats = card.get_tournament_stats()
        print("- Record:"
              f"{stats['wins']}-{stats['losses']}\n")

    return list_id


def main() -> None:
    print("=== DataDeck Tournament Platform ===\n")
    platform = TournamentPlatform()
    list_id = tournament_cards(platform)
    id1, id2 = list_id
    match(platform, id1, id2)
    leaderboard(platform)
    global_report(platform)
    print("=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
