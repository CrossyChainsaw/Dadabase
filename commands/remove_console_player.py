import json
from Dadabase.modules.data_management import read_data, remove_player_from_clan_data, CLANS_DATA_PATH, DATA_KEY_FOR_CONSOLE_PLAYERS


async def remove_console_player(interaction, brawlhalla_id):
    clan_data = read_data(CLANS_DATA_PATH, interaction.guild.id)
    brawlhalla_name, removed_player = remove_player_from_clan_data(interaction, brawlhalla_id, clan_data, DATA_KEY_FOR_CONSOLE_PLAYERS)
    if removed_player:
        await interaction.response.send_message(brawlhalla_name + " was removed")
    else:
        await interaction.response.send_message(f"Couldn't find player with `brawlhalla_id:{brawlhalla_id}`")