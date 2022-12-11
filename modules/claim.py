from modules.api import fetch_player_ranked_stats
from classes.User import User
import json
from modules.data import read_link_data, write_link_data

DATA_LINKS_LOCATION = 'data/links.json'

async def claim(ctx, brawlhalla_id):
  ranked_stats = __request(brawlhalla_id)
  if (ranked_stats):
    condition = already_claimed(ctx)
    if condition == True:
      await __update_link(ctx, ranked_stats)
    else:
      await __add_link(ctx, ranked_stats)
  else:  
    await ctx.channel.send("Account with `brawlhalla_id: "+brawlhalla_id+"` does not exist or hasn't played ranked yet")

def already_claimed(ctx):
  link_data = []
  link_data = read_link_data()
  for user in link_data:
    if str(ctx.author.id) == str(user['discord_id']):
      return True
  return False
  
  
  #check if dc is linked
  

async def __add_link(ctx, ranked_stats):
  brawlhalla_name = __save_link(ctx, ranked_stats)
  await ctx.channel.send("Claimed brawlhalla account: " + brawlhalla_name)

async def __update_link(ctx, ranked_stats):
  user = __create_user(ctx, ranked_stats)
  link_data = read_link_data()
  x = 0
  print('g')
  for link in link_data:
    if ctx.author.id == link['discord_id']:
      break
    x+=1
  print(link_data[x])
  link_data[x]['brawlhalla_id'] = user.brawlhalla_id
  link_data[x]['brawlhalla_name'] = user.brawlhalla_name
  with open('data/links.json', 'w') as data_file:
    json.dump(link_data, data_file)
    await ctx.channel.send("Updated claimed brawlhalla account to ```brawlhalla_name: "+user.brawlhalla_name+'\nbrawlhalla_id: '+str(user.brawlhalla_id)+'```')
    
  
      
def __request(brawlhalla_id):
  return fetch_player_ranked_stats(brawlhalla_id)

def __save_link(ctx, ranked_stats):
  user = __create_user(ctx, ranked_stats)
  __save_data(user)
  return user.brawlhalla_name

def __create_user(ctx, ranked_stats):
  brawlhalla_id = ranked_stats['brawlhalla_id']
  brawlhalla_name = ranked_stats['name']
  discord_id = ctx.author.id
  discord_name = ctx.author.name
  user = User(brawlhalla_id, brawlhalla_name, discord_id, discord_name)
  return user

def __save_data(user):
    link_data = read_link_data()
    link_data.append(user.__dict__)
    write_link_data(link_data)


