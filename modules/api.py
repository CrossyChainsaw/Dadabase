import os
import requests
import time

# METHODS
def fetch_player_ranked_stats(brawlhalla_id):
    return requests.get("https://api.brawlhalla.com/player/" +
                        str(brawlhalla_id) + "/ranked?api_key="+os.environ['API_KEY'])
