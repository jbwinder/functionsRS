# Jakob Kahler
# Part 5 of Functions Are US
# Display the final record for a team. Receive the home team data and display information.


def display_final_record(home_team, results):
# Display the final record for a team
    wins = sum(1 for game in results if game["Result"] == "W")
    losses = len(results) - wins
    print(f"\nFinal season record for {home_team}: {wins}-{losses}")
# Receive home team data and display their season results
    win_percentage = wins / len(results) if results else 0
    if win_percentage >= 0.75:
        print("Qualified for the NCAA Women's Soccer Tournament")
    elif win_percentage >= 0.50:
        print("You had a good season")
    else:
        print("Your team needs to practice!")