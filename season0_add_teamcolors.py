import json
import uuid

with open('season0/teams.json', 'r') as f:
    teams = json.load(f)

def get_team_color(teamName):
    for teamjson in teams:
        if teamjson['teamName']==teamName:
            return teamjson['teamColor']

############################

with open('season0/schedule.json', 'r') as f:
    schedule = json.load(f)

for day in schedule:
    for game in day:
        t1 = game['team1Name']
        t2 = game['team2Name']
        t1c = get_team_color(t1)
        t2c = get_team_color(t2)
        game['team1Color'] = t1c
        game['team2Color'] = t2c

with open('season0/new_schedule.json', 'w') as f:
    json.dump(schedule, f, indent=4)

############################

with open('season0/season.json', 'r') as f:
    season = json.load(f)

for day in season:
    for game in day:
        t1 = game['team1Name']
        t2 = game['team2Name']
        t1c = get_team_color(t1)
        t2c = get_team_color(t2)
        game['team1Color'] = t1c
        game['team2Color'] = t2c

with open('season0/new_season.json', 'w') as f:
    json.dump(season, f, indent=4)

############################


with open('season0/postseason.json', 'r') as f:
    postseason = json.load(f)

for series in postseason:
    for day in postseason[series]:
        for game in day:
            t1 = game['team1Name']
            t2 = game['team2Name']
            t1c = get_team_color(t1)
            t2c = get_team_color(t2)
            game['team1Color'] = t1c
            game['team2Color'] = t2c

with open('season0/new_postseason.json', 'w') as f:
    json.dump(postseason, f, indent=4)
