from modules.api import fetch_player_ranked_stats
from classes.User import User
import json

async def claim(ctx, brawlhalla_id):
  ranked_stats = request(brawlhalla_id)
  brawlhalla_name = save_link(ctx, ranked_stats)
  await ctx.channel.send("Claimed brawlhalla account: " + brawlhalla_name)

def request(brawlhalla_id):
   return json.loads(fetch_player_ranked_stats(brawlhalla_id).content)

def save_link(ctx, ranked_stats):
  # filter to variables
  brawlhalla_id = ranked_stats['brawlhalla_id']
  brawlhalla_name = ranked_stats['name']
  discord_id = ctx.author.id
  discord_name = ctx.author.name
  user = User(brawlhalla_id, brawlhalla_name, discord_id, discord_name)

  # save data
  with open('data/links.json', 'r') as read_file:
    links = json.load(read_file)
    links.append(user.__dict__)
    with open('data/links.json', 'w') as write_file:
      json.dump(links, write_file)
  return brawlhalla_name
  