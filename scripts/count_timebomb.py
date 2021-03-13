import os
import json


for season in [13, 14]:

    seasondir = f'season{season}'
    schedfile = os.path.join(seasondir, 'schedule.json')
    bracketfile = os.path.join(seasondir, 'bracket.json')

    with open(schedfile, 'r') as f:
        sched = json.load(f)
    
    wh = 0
    whr = 0
    for day in sched:
        for game in day:
            if game['patternName'] == 'timebomb':
                wh += 1
            elif game['patternName'] == 'timebombredux':
                whr += 1
    
    with open(bracketfile, 'r') as f:
        brack = json.load(f)
    
    post_wh = 0
    post_whr = 0
    for day in sched:
        for game in day:
            if game['patternName'] == 'timebomb':
                post_wh += 1
            elif game['patternName'] == 'timebombredux':
                post_whr += 1
    
    print(f"Season {season+1} Total:")
    print(f"  {wh+post_wh} West Hellmouth maps")
    print(f"  {whr+post_whr} West Hellmouth Revenge maps")
