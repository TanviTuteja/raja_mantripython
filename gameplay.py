import random

players = ["player1", "player2", "player3", "player4"]
roles = ["raja", "mantri", "chor", "sipahi"]
scores = {player: 0 for player in players}

def assign_roles():
    random.shuffle(roles)
    return dict(zip(players, roles))

def play_round():
    print("\n--- New Round ---")
    assigned = assign_roles()

    for player in players:
        print(f"{player} ka role: {'**' if assigned[player] == 'chor' else assigned[player]}")

    sipahi = [p for p, r in assigned.items() if r == "sipahi"][0]
    chor = [p for p, r in assigned.items() if r == "chor"][0]

    guess = input(f"\n{sipahi}, guess who is the chor (type player name): ").strip()

    if guess == chor:
        print("Sahi pakda!")
        scores[sipahi] += 500
    else:
        print(f"Galat! Chor tha: {chor}")
        scores[chor] += 500

    # Points for Raja & Mantri
    for player, role in assigned.items():
        if role == "raja":
            scores[player] += 1000
        elif role == "mantri":
            scores[player] += 800

    # Show current scores
    print("\nScores:")
    for player in players:
        print(f"{player}: {scores[player]}")

# Game chalayen — 3 rounds
for i in range(3):
    play_round()

# Final scores
print("\nFinal Scores:")
for player, score in scores.items():
    print(f"{player}: {score}")