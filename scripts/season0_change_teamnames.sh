#!/bin/bash

sed -e 's/Washington Footballteam/Ft. Worth Piano Tuners/g' \
    -e 's/Forth Worth/Ft. Worth/g' \
    -e 's/Phoenix Good-At-Maths/Seattle Sneakers/g' \
    -e 's/Seattle Sneakernets/Seattle Sneakers/g' \
    season0/teams.json > season0/new_teams.json

sed -e 's/Washington Footballteam/Ft. Worth Piano Tuners/g' \
    -e 's/Forth Worth/Ft. Worth/g' \
    -e 's/Phoenix Good-At-Maths/Seattle Sneakers/g' \
    -e 's/Seattle Sneakernets/Seattle Sneakers/g' \
    season0/schedule.json > season0/new_schedule.json

sed -e 's/Washington Footballteam/Ft. Worth Piano Tuners/g' \
    -e 's/Forth Worth/Ft. Worth/g' \
    -e 's/Phoenix Good-At-Maths/Seattle Sneakers/g' \
    -e 's/Seattle Sneakernets/Seattle Sneakers/g' \
    season0/season.json > season0/new_season.json

sed -e 's/Washington Footballteam/Ft. Worth Piano Tuners/g' \
    -e 's/Forth Worth/Ft. Worth/g' \
    -e 's/Phoenix Good-At-Maths/Seattle Sneakers/g' \
    -e 's/Seattle Sneakernets/Seattle Sneakers/g' \
    season0/bracket.json > season0/new_bracket.json

sed -e 's/Washington Footballteam/Ft. Worth Piano Tuners/g' \
    -e 's/Forth Worth/Ft. Worth/g' \
    -e 's/Phoenix Good-At-Maths/Seattle Sneakers/g' \
    -e 's/Seattle Sneakernets/Seattle Sneakers/g' \
    season0/postseason.json > season0/new_postseason.json

sed -e 's/Washington Footballteam/Ft. Worth Piano Tuners/g' \
    -e 's/Forth Worth/Ft. Worth/g' \
    -e 's/Phoenix Good-At-Maths/Seattle Sneakers/g' \
    -e 's/Seattle Sneakernets/Seattle Sneakers/g' \
    season0/seed.json > season0/new_seed.json
