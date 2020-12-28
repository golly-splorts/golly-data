import json


write = True
dcs = 'Delaware Corporate Shells'
dcscol = '#a0e7e8'


with open('season3/teams.json', 'r') as f:
    teams = json.load(f)

for team in teams:
    if team['teamName']==dcs:
        team['teamColor'] = dcscol

if write:
    with open('season3/teams.json', 'w') as f:
        json.dump(teams, f, indent=4)


with open('season3/bracket.json', 'r') as f:
    bracket = json.load(f)

for series in bracket:
    miniseason = bracket[series]
    for day in miniseason:
        for game in day:
            if game['team1Name']==dcs:
                game['team1Color']=dcscol
            if game['team2Name']==dcs:
                game['team2Color']=dcscol

if write:
    with open('season3/bracket.json', 'w') as f:
        json.dump(bracket, f, indent=4)


with open('season3/postseason.json', 'r') as f:
    postseason = json.load(f)

for series in postseason:
    miniseason = postseason[series]
    for day in miniseason:
        for game in day:
            if game['team1Name']==dcs:
                game['team1Color']=dcscol
            if game['team2Name']==dcs:
                game['team2Color']=dcscol

if write:
    with open('season3/postseason.json', 'w') as f:
        json.dump(postseason, f, indent=4)


with open('season3/schedule.json', 'r') as f:
    schedule = json.load(f)

for day in schedule:
    for game in day:
        if game['team1Name']==dcs:
            game['team1Color']=dcscol
        if game['team2Name']==dcs:
            game['team2Color']=dcscol

if write:
    with open('season3/schedule.json', 'w') as f:
        json.dump(schedule, f, indent=4)


with open('season3/season.json', 'r') as f:
    season = json.load(f)

for day in season:
    for game in day:
        if game['team1Name']==dcs:
            game['team1Color']=dcscol
        if game['team2Name']==dcs:
            game['team2Color']=dcscol

if write:
    with open('season3/season.json', 'w') as f:
        json.dump(season, f, indent=4)

