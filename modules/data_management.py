from enum import Enum
import json
from discord import app_commands
from Dadabase.classes.Link import Link
import discord 

# Paths
DADABASE_DATA_PATH = 'Dadabase/data/'
SERVERS_DATA_PATH = DADABASE_DATA_PATH + 'servers/'
CLANS_DATA_PATH = DADABASE_DATA_PATH + 'clans/'


# Data Keys
# Clans
DATA_KEY_FOR_ACCOUNT_LINKERS = 'account_linkers' # account linkers / remove players / crossplayers
DATA_KEY_FOR_CONSOLE_PLAYERS = 'console_players' # console players
DATA_KEY_FOR_SHOW_XP = 'show_xp'
DATA_KEY_FOR_2V2_LEGENDS = 'legends_for_2v2'
DATA_KEY_FOR_OWN_2V2_LEGEND = 'own_legend'
DATA_KEY_FOR_MATE_2V2_LEGEND = 'mate_legend'
DATA_KEY_FOR_SHOW_WIN_LOSS = 'show_win_loss'
DATA_KEY_FOR_SHOW_LEGENDS = 'show_legends'
# Server
DATA_KEY_FOR_SERVER_ID = 'id'
DATA_KEY_FOR_SERVER_NAME = "name"
DATA_KEY_FOR_LEADERBOARD_TITLE = "leaderboard_title"
DATA_KEY_FOR_FLAG_TYPE = 'flag_type'
DATA_KEY_FOR_SERVER_LINKS = 'links'
class FlagType(Enum):
    NONE = 'no_flags'
    REGION = 'region'
    COUNTRY = 'country'
    ETHNICITY = 'ethnicity'
# Both
DATA_KEY_FOR_SHOW_MEMBER_COUNT = 'show_member_count'
DATA_KEY_FOR_SHOW_NO_ELO_PLAYERS = 'show_no_elo_players'
DATA_KEY_FOR_SORTING_METHOD = "sorting_method"
DATA_KEY_FOR_CHANNEL_1V1_ID = "channel_1v1_id"
DATA_KEY_FOR_CHANNEL_2V2_ID = "channel_2v2_id"
DATA_KEY_FOR_CHANNEL_ROTATING_ID = "channel_rotating_id"
DATA_KEY_FOR_IMAGE = 'image'
DATA_KEY_FOR_COLOR = 'color'

# Legends
BRAWLHALLA_LEGENDS = [
    "ada", "arcadia", "artemis", "asuri", "azoth", "barraza", "bodvar", "brynn", 
    "caspian", "cassidy", "cross", "diana", "dusk", "ember", "ezio", "fait", 
    "gnash", "hattori", "imugi", "isaiah", "jaeyun", "jhala", "jiro", "kaya", 
    "kingzuva", "koji", "kor", "linfei", "loki", "lordvraxx", "lucien", "magyar", 
    "mako", "mirage", "mordex", "munin", "queennai", "nix", "onyx", "orion", 
    "petra", "queennai", "ragnir", "random", "rayman", "redraptor", "reno", 
    "scarlet", "sentinel", "seven", "sidra", "sirroland", "teros", 
    "tezca", "thatch", "thea", "thor", "ulgrim", "val", "vector", "vivi", 
    "volkov", "lordvraxx", "wushang", "xull", "yumiko", "zariel"
]



# Functions
async def add_link(interaction, link: Link):
    print('Entered: __add_link()')
    __save_data(interaction, link)
    await interaction.response.send_message(embed=embed_with_link_data(link, interaction))

def __save_data(interaction, user):
    print('Entered: __save_data()')
    server_data = read_data(SERVERS_DATA_PATH, interaction.guild.id)
    link_data = server_data['links']
    link_data.append(user.__dict__)
    server_data['links'] = link_data
    write_data(SERVERS_DATA_PATH, server_data, interaction.guild.id)

async def update_link(interaction, new_link:Link):
    print('Entered: __update_link()')
    server_data = read_data(SERVERS_DATA_PATH, interaction.guild.id)
    link_data = server_data['links']
    link_index = find_link_index(interaction.user.id, link_data)
    link = link_data[link_index]
    link['brawlhalla_id'] = new_link.brawlhalla_id
    link['brawlhalla_name'] = new_link.brawlhalla_name
    link['region'] = new_link.region
    link['country'] = new_link.country
    link['ethnicity'] = new_link.ethnicity
    link['legends_for_2v2'] = new_link.legends_for_2v2
    write_data(SERVERS_DATA_PATH, server_data, interaction.guild.id)
    await interaction.response.send_message(embed=embed_with_link_data(new_link, interaction))

def already_claimed(interaction):
    print('Entered: already_claimed()')
    link_data = []
    link_data = read_link_data(SERVERS_DATA_PATH, interaction.guild.id)
    for user in link_data:
        if str(interaction.user.id) == str(user['discord_id']):
            return True
    return False

def read_data(path, id):
  """Read clan or server data"""
  with open(path + str(id) + '.json') as file:
    data = json.load(file)
    return data
  
def read_link_data(path, id):
  with open(path + str(id) + '.json') as data:
    link_data = json.load(data)["links"]
    return link_data

def write_data(path, data, id):
  print('Entered: write_data()')
  with open(path + str(id) + '.json', 'w') as write_file:
    json.dump(data, write_file, indent=4)

def add_player_to_clan_data(interaction, data, brawlhalla_account, data_location, key):
    """Adds a player to clan data. Used for Console Players and Account Linkers"""
    data[key].append(brawlhalla_account.__dict__)
    with open(data_location + str(interaction.guild.id) + '.json', 'w') as file:
        json.dump(data, file, indent=4)


def remove_player_from_clan_data(interaction, brawlhalla_id, data, key):
    """Removes a player from clan data. Used for Console Players and Account Linkers"""
    bh_name = ""
    removed_player = False
    for index, player in enumerate(data[key]):
        if str(player['brawlhalla_id']) == str(brawlhalla_id):
            bh_name = data[key].pop(index)['brawlhalla_name']
            with open(CLANS_DATA_PATH + str(interaction.guild.id) + '.json', 'w') as file:
                json.dump(data, file)
                removed_player = True
            break
    return bh_name, removed_player

def find_link(discord_id, link_data):
    for link in link_data:
        if str(discord_id) == str(link['discord_id']):
            user:Link = Link(brawlhalla_id=link['brawlhalla_id'], 
                        brawlhalla_name=link['brawlhalla_name'],
                        discord_id=link['discord_id'], 
                        discord_name=link['discord_name'], 
                        region=__check_empty(link.get('region')), 
                        country=__check_empty(link.get('country')), 
                        ethnicity=__check_empty(link.get('ethnicity')),
                        own_legend=__check_empty(link.get(DATA_KEY_FOR_2V2_LEGENDS, {}).get(DATA_KEY_FOR_OWN_2V2_LEGEND)),
                        mate_legend=__check_empty(link.get(DATA_KEY_FOR_2V2_LEGENDS, {}).get(DATA_KEY_FOR_MATE_2V2_LEGEND)))
            return user
    else:
        return None
    
def find_link_index(discord_id, link_data):
    for index, link in enumerate(link_data):
        if discord_id == link['discord_id']:
            return index
    
def __check_empty(value):
   if value:
      return value
   else: 
      return "Not Specified"
   


def codeblock_with_link_data(link:Link):
    return f"```ts\nbrawlhalla_name: {__empty_name(link.brawlhalla_name)}\nbrawlhalla_id: {link.brawlhalla_id}\nregion: {__check_empty(link.region)}\ncountry: {__check_empty(link.country)}\nethnicity: {__check_empty(link.ethnicity)}```"

def embed_with_link_data(link:Link, interaction:discord.Interaction):
    embed = discord.Embed(
        title=f"{link.brawlhalla_name}'s Claimed Profile",
        color=0x09fbd7
    )
    embed.set_thumbnail(url=interaction.user.avatar)
    embed.add_field(name="Brawlhalla Name", value=link.brawlhalla_name, inline=False)
    embed.add_field(name="Brawlhalla ID", value=link.brawlhalla_id, inline=False)
    embed.add_field(name="Region", value=__check_empty(link.region), inline=False)
    embed.add_field(name="Country", value=__check_empty(link.country), inline=False)
    embed.add_field(name="Ethnicity", value=__check_empty(link.ethnicity), inline=False)
    embed.add_field(name="My 2v2 Comp", value=f"{__check_empty(link.legends_for_2v2[DATA_KEY_FOR_OWN_2V2_LEGEND]).capitalize()} & {__check_empty(link.legends_for_2v2[DATA_KEY_FOR_MATE_2V2_LEGEND]).capitalize()}", inline=False)
    return embed

def __empty_name(name):
    if name == "":
        return "N/A (finish 1s placement matches)"
    else:
        return name
    
def embed_no_claimed_account():
    embed = discord.Embed(
        title="Oops!",
        description="You haven't claimed an account yet",
        color=0x09fbd7
    )
    return embed