# Taylor Wall
# Display an introduction to the game explaining rules and prompt for their name and display that in the welcome message
# Return the name to the main program and store it in variable so it can be used throughout the program.

def intro(name):
    name = input("Please enter your name: ")

    print (f"""\nHello {name}, welcome to this soccer season!
    In this game, you will select your team and the teams you will play.
    Scores will be generated and your team's wins and loses will be recorded.
    Press 1 to continue. \n """)


    userDesc = int(input("Enter your choice: "))

    if userDesc == 1:
        pick_teams.py()

    else: 
        print (f"Goodbye!") 
        quit()
