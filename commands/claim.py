import json
from Dadabase.modules.api import fetch_player_ranked_stats
from Dadabase.classes.Link import Link
from Dadabase.classes.BrawlhallaAccount import BrawlhallaAccount
from Dadabase.modules.data_management import add_link, already_claimed, embed_with_link_data, find_link_index, read_link_data, update_link, write_data, read_data, SERVERS_DATA_PATH
from discord import Interaction

async def claim(interaction:Interaction, brawlhalla_id, region, country_of_residence, ethnicity, your_legend, teammate_legend):
    ranked_stats = await fetch_player_ranked_stats(brawlhalla_id)
    link = Link(ranked_stats['brawlhalla_id'], ranked_stats['name'], interaction.user.id, interaction.user.name, region, country_of_residence, ethnicity, own_legend=your_legend.lower(), mate_legend=teammate_legend.lower())
    condition = already_claimed(interaction)
    if condition == True:
        print('updating link')
        await update_link(interaction, link)
    else:
        await add_link(interaction, link)