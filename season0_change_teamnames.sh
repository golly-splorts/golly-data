#!/bin/bash

sed -e 's/Washington Footballteam/Forth Worth Piano Tuners/g' \
    -e 's/Phoenix Good-At-Maths/Seattle Sneakernets/g' \
    season0/teams.json > season0/new_teams.json

sed -e 's/Washington Footballteam/Forth Worth Piano Tuners/g' \
    -e 's/Phoenix Good-At-Maths/Seattle Sneakernets/g' \
    season0/season.json > season0/new_season.json

sed -e 's/Washington Footballteam/Forth Worth Piano Tuners/g' \
    -e 's/Phoenix Good-At-Maths/Seattle Sneakernets/g' \
    season0/postseason.json > season0/new_postseason.json
