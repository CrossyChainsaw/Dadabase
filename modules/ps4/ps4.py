import json

DATA_LOCATION = 'data/servers/'

def load_data(server_id):
  with open(DATA_LOCATION + str(server_id) + '.json', 'r') as file:
    return json.load(file)