import os
import json

NSEASONS = 5
for iseason in range(NSEASONS):

    seasondir = "season%d"%(iseason)
    bracketfile = os.path.join(seasondir, 'bracket.json')
    newbracketfile = os.path.join(seasondir, 'newbracket.json')

    with open(bracketfile, 'r') as f:
        bracket = json.load(f)

    for series in bracket:
        miniseason = bracket[series]
        for iday, day in enumerate(miniseason):
            for game in day:
                if 'season' not in game:
                    game['season'] = iseason

    with open(newbracketfile, 'w') as f:
        json.dump(bracket, f, indent=4)
