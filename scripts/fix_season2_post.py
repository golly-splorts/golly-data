from golly_python import pylife
import json

with open('season2/postseason.json', 'r') as f:
    post = json.load(f)

for series in ['LDS', 'LCS']:
    miniseason = post[series]
    for iD, day in enumerate(miniseason):
        for iG, game in enumerate(day):
            if game['team1Score']<10 and game['team2Score']<10:
                print(f"Starting on game {iG+1} of day {iD+1} of series {series}...")
                r = game['map']['rows']
                c = game['map']['columns']
                s1 = game['map']['initialConditions1']
                s2 = game['map']['initialConditions2']
                gol = pylife.GOL(s1=s1, s2=s2, rows=r, columns=c)
                while gol.running:
                    live_counts = gol.next_step()
                results = gol.get_live_counts()
                game['team1Score'] = results['liveCells1']
                game['team2Score'] = results['liveCells2']
                game['generations'] = results['generation']

                print(f"Finished with game {iG+1} of day {iD+1} of series {series}!")
                with open('season2/new_postseason.json', 'w') as f:
                    json.dump(post, f, indent=4)
            else:
                print(f"Skipping game {iG+1} of day {iD+1} of series {series}, it seems okay...")

with open('season2/new_postseason.json', 'w') as f:
    json.dump(post, f, indent=4)
