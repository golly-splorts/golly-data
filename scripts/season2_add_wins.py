import json


with open('season2/teams.json', 'r') as f:
    teams = json.load(f)
team_names = [t['teamName'] for t in teams]

#############
# postseason:
with open('season2/postseason.json', 'r') as f:
    postseason = json.load(f)

# postseason wins/losses
pwins = {}
plosses = {}

# init
for team in team_names:
    pwins[team] = 0
    plosses[team] = 0

# populate postseason wl as we go
for series in postseason:
    # series wins/losses
    swins = {}
    slosses = {}
    for team in team_names:
        swins[team] = 0
        slosses[team] = 0
    for day in postseason[series]:
        for game in day:
            # populate wl and series wl before counting this game
            t1 = game['team1Name']
            t2 = game['team2Name']
            game['team1PostseasonWinLoss'] = [pwins[t1], plosses[t1]]
            game['team2PostseasonWinLoss'] = [pwins[t2], plosses[t2]]
            game['team1SeriesWinLoss'] = [swins[t1], slosses[t1]]
            game['team2SeriesWinLoss'] = [swins[t2], slosses[t2]]
            if game['team1Score'] > game['team2Score']:
                pwins[t1] += 1
                swins[t1] += 1
                plosses[t2] += 1
                slosses[t2] += 1
            else:
                pwins[t2] += 1
                swins[t2] += 1
                plosses[t1] += 1
                slosses[t1] += 1

with open('season2/new_postseason.json', 'w') as f:
    json.dump(postseason, f, indent=4)
