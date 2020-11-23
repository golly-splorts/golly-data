import json

with open('input-data/teams.json', 'r') as f:
    teams = json.load(f)

def get_team_color(teamName):
    for team in teams:
        if team['teamName'] == teamName:
            return team['teamColor']

def get_team_league(teamName):
    for team in teams:
        if team['teamName'] == teamName:
            return team['league']

with open('output-data-season-0/season.json', 'r') as f:
    season = json.load(f)

team_names = set()
for iday, day in enumerate(season):
    games = day
    for igame, game in enumerate(games):

        # Check colors
        t1 = game['team1Name']
        t1c = game['team1Color']
        if t1c != get_team_color(t1):
            raise Exception("Error in game {igame} of day {iday}: team1 color was {t1c}, should have been {get_team_color(t1)}")
        t2 = game['team1Name']
        t2c = game['team1Color']
        if t2c != get_team_color(t2):
            raise Exception("Error in game {igame} of day {iday}: team2 color was {t2c}, should have been {get_team_color(t2)}")

        team_names.add(t1)
        team_names.add(t2)

        t1s = game['team1Score']
        t2s = game['team2Score']
        if t1s==t2s:
            raise Exception("Error in game {igame} of day {iday}: game is tied! {team1Score}-{team2Score}")

        if 'map' not in game.keys():
            raise Exception("Error in game {igame} of day {iday}: game is missing a map!")
        
        gameLeague = game['league']
        t1league = get_team_league(t1)
        t2league = get_team_league(t2)
        if (t1league != gameLeague) or (t2league != gameLeague):
            raise Exception("Error in game {igame} of day {iday}: Team 1 and Team 2 leagues do not match!  {t1}:{t1league}, {t2}:{t2league}")


if len(team_names) != len(teams):
    raise Exception("Found incorrect number of teams from season container:\nwrong: {', '.join(team_names)}\nright: {', '.join([team['teamName'] for team in teams])}")

print("Everything is okay")
