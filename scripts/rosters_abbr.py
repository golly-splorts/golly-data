import json

with open('rosters/rosters.json', 'r') as f:
    rosters = json.load(f)

with open('season4/teams.json', 'r') as f:
    teams = json.load(f)

new_rosters = {}
for team in teams:
    team_name = team['teamName']
    team_abbr = team['teamAbbr']
    new_rosters[team_abbr] = rosters[team_name]

with open('rosters/new_rosters.json', 'w') as f:
    json.dump(new_rosters, f)
