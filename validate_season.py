import os
import json


for seasondir in ['season0', 'season1']:


    #####################
    # load team data

    teamsfile = os.path.join(seasondir, 'teams.json')

    with open(teamsfile, 'r') as f:
        teams = json.load(f)

    # -----------
    # team function defs

    def get_team_color(teamName):
        for team in teams:
            if team['teamName'] == teamName:
                return team['teamColor']

    def get_team_league(teamName):
        for team in teams:
            if team['teamName'] == teamName:
                return team['league']


    #####################
    # check games

    # -----------
    # game function defs

    def check_name_color_match(game):
        """For a given game ensure the team name matches the team color"""
        t1 = game['team1Name']
        t1c = game['team1Color']
        if t1c != get_team_color(t1):
            raise Exception(f"Error in game {game['id']} of day {game['day']}: team1 color was {t1c}, should have been {get_team_color(t1)}")
        t2 = game['team1Name']
        t2c = game['team1Color']
        if t2c != get_team_color(t2):
            raise Exception(f"Error in game {game['id']} of day {game['day']}: team2 color was {t2c}, should have been {get_team_color(t2)}")

    def check_score(game):
        t1s = game['team1Score']
        t2s = game['team2Score']
        if t1s==t2s:
            raise Exception(f"Error in game {game['id']} of day {game['day']}: game is tied! {team1Score}-{team2Score}")
        if t1s < 0 or t2s < 0:
            raise Exception(f"Error in game {game['id']} of day {game['day']}: negative score ({t1s})-({t2s})")

    def check_league(game):
        league = game['league']
        t1 = game['team1Name']
        t2 = game['team2Name']
        t1lea = get_team_league(t1)
        t2lea = get_team_league(t2)
        if (t1lea!=league) or (t2lea!=league):
            raise Exception(f"Error in game {game.id} of day {game.day}: league information does not match: {t1}:{t1lea}, {t2}:{t2lea}")

    def check_id(game):
        if 'id' not in game.keys():
            print(game)
            raise Exception(f"Error in game on day {game.day}: no id found")

    def check_pattern(game):
        if 'patternName' not in game.keys():
            raise Exception(f"Error in game {game['id']} of day {game['day']}: game is missing a map!")

    def check_map(game):
        if 'map' not in game.keys():
            raise Exception(f"Error in game {game['id']} of day {game['day']}: game is missing a map!")
        mapp = game['map']
        # required keys that must be present
        req_keys = [
            'mapName',
            'mapZone1Name',
            'mapZone2Name',
            'mapZone3Name',
            'mapZone4Name',
            'initialConditions1',
            'initialConditions2',
            'rows',
            'columns',
            'cellSize',
            'patternName'
        ]
        # unused keys that should not be present
        unreq_keys = [
            'url',
            'patternId'
        ]

        for rk in req_keys:
            if rk not in mapp:
                raise Exception("Error in game {game['id']} of day {game['day']}: game map is missing key \"{rk}\"!")
        #for urk in unreq_keys:
        #    if urk in mapp:
        #        raise Exception("Error in game {game['id']} of day {game['day']}: game map should not have key \"{urk}\"!")

    # -----------
    # schedule

    schedfile = os.path.join(seasondir, 'schedule.json')

    print("***************************")
    print(f"Now checking {schedfile}")

    with open(schedfile, 'r') as f:
        sched = json.load(f)

    sched_team_names = set()
    for iday, day in enumerate(sched):
        games = day
        for igame, game in enumerate(games):
            t1 = game['team1Name']
            t2 = game['team1Name']

            check_name_color_match(game)
            check_league(game)
            check_pattern(game)

            sched_team_names.add(t1)
            sched_team_names.add(t2)

    if len(sched_team_names) != len(teams):
        raise Exception(f"Error: number of teams found in schedule was {len(sched_team_names)}, number of teams is {len(teams)}")

    for team in teams:
        if team['teamName'] not in sched_team_names:
            raise Exception(f"Error: team name {team['teamName']} not found in schedule.json")


    # -----------
    # season

    seasonfile = os.path.join(seasondir, 'season.json')

    print("***************************")
    print(f"Now checking {seasonfile}")

    with open(seasonfile, 'r') as f:
        season = json.load(f)

    season_team_names = set()
    for iday, day in enumerate(season):
        games = day
        for igame, game in enumerate(games):
            t1 = game['team1Name']
            t2 = game['team1Name']

            check_name_color_match(game)
            check_score(game)
            check_league(game)
            check_map(game)

            season_team_names.add(t1)
            season_team_names.add(t2)

    if len(season_team_names) != len(teams):
        raise Exception(f"Error: number of teams found in season was {len(season_team_names)}, number of teams is {len(teams)}")

    for team in teams:
        if team['teamName'] not in season_team_names:
            raise Exception(f"Error: team name {team['teamName']} not found in season.json")


    # -----------
    # postseason

    postseasonfile = os.path.join(seasondir, 'postseason.json')

    print("***************************")
    print(f"Now checking {postseasonfile}")

    postseason_team_names = set()
    with open(postseasonfile, 'r') as f:
        postseason = json.load(f)

    for series in postseason:
        miniseason = postseason[series]
        for iday, day in enumerate(miniseason):
            games = day
            for igame, game in enumerate(games):
                t1 = game['team1Name']
                t2 = game['team1Name']

                check_id(game)
                check_name_color_match(game)
                check_score(game)
                if series != 'WS':
                    check_league(game)
                check_map(game)

                postseason_team_names.add(t1)
                postseason_team_names.add(t2)

    team_names = set()
    for team in teams:
        team_names.add(team['teamName'])
    for postseason_team_name in postseason_team_names:
        if postseason_team_name not in team_names:
            raise Exception(f"Error: invalid team name {postseason_team_name} found in postseason.json")

    # Verify series are the correct lengths
    ldslen = len(postseason['LDS'])
    if ldslen>5 or ldslen<3:
        raise Exception(f"Error: postseason LDS length is invalid: {ldslen} games")

    lcslen = len(postseason['LCS'])
    if lcslen>5 or lcslen<3:
        raise Exception(f"Error: postseason LCS length is invalid: {lcslen} games")

    wslen = len(postseason['WS'])
    if wslen>7 or wslen<4:
        raise Exception(f"Error: postseason WS length is invalid: {wslen} games")


print("***************************")
print("Everything is okay")

# TODO: postseason
