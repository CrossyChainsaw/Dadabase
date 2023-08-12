from classes.Xos import Xos
os = Xos()

#import os
import requests
import time
import json

# METHODS
def fetch_player_ranked_stats(brawlhalla_id):
  json_object = requests.get("https://api.brawlhalla.com/player/" +
str(brawlhalla_id) + "/ranked?api_key=" + os.environ[0])
  return json.loads(json_object.content)  
