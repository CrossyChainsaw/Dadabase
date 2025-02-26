import json
from Dadabase.modules.api import fetch_player_ranked_stats
from Dadabase.classes.Link import Link
from Dadabase.modules.data_management import add_link, codeblock_with_link_data, embed_with_link_data, find_link_index, read_link_data, update_link, write_data, read_data, SERVERS_DATA_PATH
# from Dadabase.modules.data_management import already_claimed

# Quick Fixed this command but it can be done cleaner
# already claimed function might be able to be imported from data manag.

async def add_server_player(interaction, brawlhalla_id, discord_id, discord_name, region, country_of_residence, ethnicity):
    region = __structure_option_if_empty(region)
    country_of_residence = __structure_option_if_empty(country_of_residence)
    ethnicity = __structure_option_if_empty(ethnicity)
    ranked_stats = await fetch_player_ranked_stats(brawlhalla_id)
    if (ranked_stats):
        link = Link(ranked_stats['brawlhalla_id'], ranked_stats['name'], int(discord_id), discord_name, region, country_of_residence, ethnicity)
        condition = __already_claimed(interaction, discord_id)
        if condition == True:
            await update_link(interaction, link)
        else:
            await add_link(interaction, link)
    else:
        await interaction.response.send_message("Account with `brawlhalla_id: "+brawlhalla_id+"` does not exist or hasn't played ranked yet")

def __structure_option_if_empty(option):
    try:
        return option.value
    except:
        return ""
    
def __already_claimed(interaction, discord_id):
    print('Entered: already_claimed()')
    link_data = []
    link_data = read_link_data(SERVERS_DATA_PATH, interaction.guild.id)
    for user in link_data:
        print(user['discord_id'])
        print(discord_id)
        print('--')
        if str(discord_id) == str(user['discord_id']):
            return True
    return False