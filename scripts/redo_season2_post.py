from golly_backend_generator.backend_data import BackendData
from golly_backend_generator.postseason_generator import PostseasonGenerator
import os
import json


HERE = os.path.abspath(os.path.dirname(__file__))
REPO = os.path.abspath(os.path.join(HERE, '..'))

def make_filename(x):
    return os.path.join(REPO, 'season2', x)

team_data_file = make_filename('teams.json')
bracket_data_file = make_filename('bracket.json')
seed_data_file = make_filename('seed.json')
postseason_data_file = make_filename('shortened_postseason.json')

backend = BackendData(team_data_file = team_data_file)
pg = PostseasonGenerator(
    backend,
    bracket_data_file = bracket_data_file,
    seed_data_file = seed_data_file,
    postseason_data_file = postseason_data_file
)

pg.generate(write=True)
