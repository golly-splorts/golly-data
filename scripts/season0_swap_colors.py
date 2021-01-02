import json

# Swap colors for the SF Boat Shoes and the Alewife Arsonists

def color_correct(colorstr):
    if colorstr=="#ff1717":
        return "#e7d7c1"
    elif colorstr=="#e7d7c1":
        return "#ff1717"
    else:
        return colorstr


############################

with open('season0/schedule.json', 'r') as f:
    schedule = json.load(f)

for day in schedule:
    for game in day:
        game['team1Color'] = color_correct(game['team1Color'])
        game['team2Color'] = color_correct(game['team2Color'])

with open('season0/new_schedule.json', 'w') as f:
    json.dump(schedule, f, indent=4)

with open('season0/season.json', 'r') as f:
    season = json.load(f)

for day in season:
    for game in day:
        game['team1Color'] = color_correct(game['team1Color'])
        game['team2Color'] = color_correct(game['team2Color'])

with open('season0/new_season.json', 'w') as f:
    json.dump(season, f, indent=4)



##############################


with open('season0/postseason.json', 'r') as f:
    postseason = json.load(f)

for series in postseason:
    for day in postseason[series]:
        for game in day:
            game['team1Color'] = color_correct(game['team1Color'])
            game['team2Color'] = color_correct(game['team2Color'])

with open('season0/new_postseason.json', 'w') as f:
    json.dump(postseason, f, indent=4)
