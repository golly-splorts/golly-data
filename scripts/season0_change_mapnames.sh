#!/bin/bash

sed -e 's/HCC Superfund Site/West Hellmouth/g' \
    -e 's/Food Court/Parking Garage/g' \
    -e 's/Sandwich Zone/Level 2A/g' \
    -e 's/Beans Zone/Level 2B/g' \
    -e 's/Freezer Zone/Level 1B/g' \
    -e 's/Kitchen Zone/Level 1A/g' \
    -e 's/Site 500/Sunbeam Moondog/g' \
    -e 's/Gammatron Accelerator/sunbeam/g' \
    -e 's/Radiobaric Chamber/moonbeam/g' \
    -e 's/Cryogenics Facility/moondog/g' \
    -e 's/Mysterious Landing Pad/sundog/g' \
    -e 's/Abandoned Lab Space/The Zoo/g' \
    -e 's/Biohazard Lab/land birds/g' \
    -e 's/Cryptobiology Lab/air birds/g' \
    -e 's/Electronics Lab/air reptiles/g' \
    -e 's/Chemistry Lab/land reptiles/g' \
    season0/postseason.json > season0/new_postseason.json
    #season0/season.json > season0/new_season.json
