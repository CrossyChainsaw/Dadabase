import json
from Dadabase.modules.api import fetch_player_ranked_stats
from Dadabase.classes.Link import Link
from Dadabase.modules.data_management import add_link, already_claimed, codeblock_with_link_data, embed_with_link_data, find_link_index, read_link_data, update_link, write_data, read_data, SERVERS_DATA_PATH


async def add_server_player(interaction, brawlhalla_id, discord_id, discord_name, region, country_of_residence, ethnicity):
    region = __structure_option_if_empty(region)
    country_of_residence = __structure_option_if_empty(country_of_residence)
    ethnicity = __structure_option_if_empty(ethnicity)
    ranked_stats = await fetch_player_ranked_stats(brawlhalla_id)
    if (ranked_stats):
        link = Link(ranked_stats['brawlhalla_id'], ranked_stats['name'], int(discord_id), discord_name, region, country_of_residence, ethnicity)
        condition = already_claimed(interaction)
        if condition == True:
            await update_link(interaction, link)
        else:
            await add_link(interaction, link)
    else:
        await interaction.response.send_message("Account with `brawlhalla_id: "+brawlhalla_id+"` does not exist or hasn't played ranked yet")

def __structure_option_if_empty(option):
    try:
        print(option.value)
        return option.value
    except:
        return ""