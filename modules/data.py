import json

DATA_LINKS_LOCATION = 'data/servers/'

def read_link_data(id):
  with open(DATA_LINKS_LOCATION + str(id) + '.json') as data:
    link_data = json.load(data)["links"]
    return link_data

def read_data(id):
  with open(DATA_LINKS_LOCATION + str(id) + '.json') as data:
    link_data = json.load(data)
    return data

def write_data(data, id):
  print('Entered: write_data()')
  with open(DATA_LINKS_LOCATION + str(id) + '.json', 'w') as write_file:
    json.dump(data, write_file)
  

    
