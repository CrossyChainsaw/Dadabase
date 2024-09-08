import json
from Dadabase.modules.api import fetch_player_ranked_stats
from Dadabase.classes.Link import Link
from Dadabase.modules.data_management import add_link, already_claimed, embed_with_link_data, find_link_index, read_link_data, update_link, write_data, read_data, SERVERS_DATA_PATH


async def claim(interaction, brawlhalla_id, region, country_of_residence, ethnicity):
    ranked_stats = await fetch_player_ranked_stats(brawlhalla_id)
    link = Link(ranked_stats['brawlhalla_id'], ranked_stats['name'], interaction.user.id, interaction.user.name, region, country_of_residence, ethnicity)
    condition = already_claimed(interaction)
    if condition == True:
        print('updating link')
        await update_link(interaction, link)
    else:
        await add_link(interaction, link)