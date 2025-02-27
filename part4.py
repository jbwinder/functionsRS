'''
Play the game receiving both team names. Generate random scores without ties. Return W or L.
Input home & away teams.
Output return dictionary
'''
# Create custom function. Input home team and away team name.
def determineWinner(homeTeam, awayTeam):
    # Import random to randomize team scores later.
    import random
    # Set wins and loses record to 0 to start.
    wins = 0
    loses = 0
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
        loses += 1
    # Create a dictionary to keep track of all game stats.
    stats = {
        'Home Team': homeTeam, 
        'Away Team': awayTeam, 
        'Home Score': homeScore, 
        'Away Score': awayScore, 
        'Result': results,
        'Wins' : wins,
        'Loses' : loses
        }
    # Return the dictionary of stats.
    return stats