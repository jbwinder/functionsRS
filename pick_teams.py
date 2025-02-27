# John Winder
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

