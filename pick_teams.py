# Taylor Wall
# Display an introduction to the game explaining rules and prompt for their name and display that in the welcome message
# Return the name to the main program and store it in variable so it can be used throughout the program.

def intro():
    name = input("Please enter your name: ")

    print (f"\nHello {name}, welcome to this soccer season!")
    print("In this game, you will select your team and the teams you will play.")
    print("Scores will be generated and your team's wins and loses will be recorded.")
    return name

#2. Display of menu and return choice. 
# Store in variable and use this value to determine which function to call next.
def callmenu () :
    print("\n Menu")
    print("Option 1: Start a new season")
    print("Option 2: Exit")
    Choice = int(input("Please input your choice:  1 or 2 "))
    return Choice


# John Winder, Nathan Blatter, Rachel McMullin, Taylor Wall, Jakob Kahler
# Takes list of teams and checks for home team. After that display names of available teams and prompt user
# to select a team return their choice


def pick_teams(exclude_team = None):
    # set list of teams and then see if there is a team that needs to be removed from the list.
    teams = ["BYU", "Utah", "Utah State","UVU", "SUU", "Utah Tech"]
    if exclude_team != None:
        teams.remove(exclude_team)

    # print available teams for user to choose between.
    print("\nAvailable Teams:\n")
    
    for team in teams:
        print(team)
    print()

    # ask user to type the name of a team as seen above. If name does not match team in list then make them do ti again.
    # When typed name correctly return the name.
    while True:
        choice = input("Write name of team you are choosing. Make sure to write name correctly with the correct capitalization. ").strip()
        if choice in teams:
            return choice
        else:
            print("\n Name not in list. Make sure to write name correctly\n")

#nathan blatter

# Rachel McMullin- Part 4
# Input home & away teams.
# Output return dictionary
# Create custom function. Input home team and away team name.
def determineWinner(homeTeam, awayTeam, wins, losses):
    # Import random to randomize team scores later.
    import random
    # Set wins and loses record to 0 to start.
    homeScore = 0
    awayScore = 0
    # Loop to randomly generate scores so their isn't ties.
    while homeScore == awayScore:
        homeScore = random.randrange(0,50)
        awayScore = random.randrange(0,50)
    # Loop to keep track of wins and loses.
    if homeScore > awayScore:
        results = 'Win'
        wins += 1
    else: 
        results = 'Lost'
        losses += 1
    # Create a dictionary to keep track of all game stats.
    stats = {
        'Home Team': homeTeam, 
        'Away Team': awayTeam, 
        'Home Score': homeScore, 
        'Away Score': awayScore, 
        'Result': results,
        'Wins' : wins,
        'Loses' : losses
        }
    # Return the dictionary of stats.
    return stats


# Jakob Kahler
# Part 5 of Functions Are US
# Display the final record for a team. Receive the home team data and display information.


def display_final_record(stats):
# Display the final record for a team
    for game in stats:
        print(f"\nFinal season record for {stats['Home Team']}: {stats['wins']}-{stats['losses']}")
# Receive home team data and display their season results
        win_percentage = wins / (wins + losses)
        if win_percentage >= 0.75:
            print("Qualified for the NCAA Women's Soccer Tournament")
        elif win_percentage >= 0.50:
            print("You had a good season")
        else:
            print("Your team needs to practice!")

# main function
name = intro()
wins = 0
losses = 0
choice = callmenu()
if choice == 1:
    print("Pick a home team:")
    home_team = pick_teams()
    print("Pick an away team:")
    away_team = pick_teams(home_team)
else:
    exit()
stats = determineWinner(home_team, away_team, wins, losses)
display_final_record(stats)