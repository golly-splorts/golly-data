import json

with open('season0/teams.json', 'r') as f:
    teams = json.load(f)

def get_team_league(teamName):
    for teamjson in teams:
        if teamjson['teamName']==teamName:
            return teamjson['league']



with open('season0/schedule.json', 'r') as f:
    schedule = json.load(f)

for day in schedule:
    for game in day:
        t1 = game['team1Name']
        league = get_team_league(t1)
        game['league'] = league

with open('season0/new_schedule.json', 'w') as f:
    json.dump(schedule, f, indent=4)




with open('season0/season.json', 'r') as f:
    schedule = json.load(f)

for day in schedule:
    for game in day:
        t1 = game['team1Name']
        league = get_team_league(t1)
        game['league'] = league

with open('season0/new_season.json', 'w') as f:
    json.dump(schedule, f, indent=4)
