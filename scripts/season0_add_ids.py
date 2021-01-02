import json
import uuid

with open('season0/season.json', 'r') as f:
    season = json.load(f)

for day in season:
    for game in day:
        game['id'] = str(uuid.uuid4())

with open('season0/new_season.json', 'w') as f:
    json.dump(season, f, indent=4)

with open('season0/postseason.json', 'r') as f:
    postseason = json.load(f)

for series in postseason:
    for day in postseason[series]:
        for game in day:
            game['id'] = str(uuid.uuid4())

with open('season0/new_postseason.json', 'w') as f:
    json.dump(postseason, f, indent=4)
