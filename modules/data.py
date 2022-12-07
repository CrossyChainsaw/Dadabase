import json

DATA_LINKS_LOCATION = 'data/links.json'

def read_link_data():
  with open(DATA_LINKS_LOCATION) as data:
    link_data = json.load(data)
    return link_data

def write_link_data(link_data):
  with open(DATA_LINKS_LOCATION, 'w') as write_file:
    json.dump(link_data, write_file)