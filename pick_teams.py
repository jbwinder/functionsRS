# Part 1- Taylor Wall
# Create a function that explains the game and returns the users name.
def intro():
    name = input("Please enter your name: ")
    print (f"\nHello {name}, welcome to this soccer season!")
    print("In this game, you will select your team and the teams you will play.")
    print("Scores will be generated and your team's wins and loses will be recorded.\n")
    return name

# Part 2- Nathan Blatter
# Create a function that displays a menu and returns choice that determines what function to call next.
def callmenu () :
    print("\n Menu")
    print("Option 1: Start a new game")
    print("Option 2: Exit")
    Choice = int(input("Please input your choice (1 or 2): "))
    return Choice

# Part 3- John Winder
# Create a function that displays a list of teams. Prompt user to pick a team and return their choice.
def pick_teams(exclude_team = None):
    # set list of teams and then see if there is a team that needs to be removed from the list.
    teams = ["BYU", "Utah", "Utah State","UVU", "SUU", "Utah Tech"]
    if exclude_team != None:
        teams.remove(exclude_team)
    # print available teams for user to choose between.
    for team in teams:
        print(team)
    print()

    print("Available Teams:")
    
    for team in teams:
        print(team)
    # ask user to type the name of a team as seen above. If name does not match team in list then make them do ti again.
    # When typed name correctly return the name.
    while True:
        choice = input("Write name of team you are choosing: ")
        if choice in teams:
            return choice
        else:
            print("\n Name not in list. Make sure to write name correctly\n")


# Part 4- Rachel McMullin
# Create a custom function. Input home & away teams. Output return win-lose results.
def determine_winner(home_team, away_team):
    import random
    homeScore = 0
    awayScore = 0
    while homeScore == awayScore:
        homeScore = random.randrange(0,10)
        awayScore = random.randrange(0,10)
    if homeScore > awayScore:
        results = "W"
    else: 
        results = "L"
    print(f"{home_team}: {homeScore}    {away_team}: {awayScore}")
    return results

# Part 5- Jakob Kahler
# Create a function that displays the final record for a team.
def display_final_record(win_loss_log):
# find how many wins and losses the home team has
    wins= 0
    losses = 0
    for game in win_loss_log:
        if game == "W":
            wins += 1
        else:
            losses += 1
    print(f"\nFinal season record for {home_team}: {wins}-{losses}")
# Decide how good the season was depending on win percentage.
    win_percentage = wins / (wins + losses)
    if win_percentage >= 0.75:
        print("Qualified for the NCAA Women's Soccer Tournament")
    elif win_percentage >= 0.50:
        print("You had a good season")
    else:
        print("Your team needs to practice!")

# main function
# set list of W's and L's
win_loss_log = []
name = intro()
print("Pick a home team:")
home_team = pick_teams()
# Set Loop to only break if they ask to leave loop
# pick a home team and away team
loop = True
while loop == True:
    choice = callmenu()
    if choice == 1:
        print("\nPick an away team:")
        away_team = pick_teams(home_team)
# append the W or L to the list of win_loss_log
        results = determine_winner(home_team, away_team)
        win_loss_log.append(results)
    else:
        loop = False
display_final_record(win_loss_log)