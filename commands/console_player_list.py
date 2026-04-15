from Dadabase.modules.data_management import read_data, DATA_KEY_FOR_CONSOLE_PLAYERS, CLANS_DATA_PATH
from Dadabase.modules.command import LEADERBOARD_CLAN_LIST_CONSOLE_PLAYERS, LEADERBOARD_CLAN_REMOVE_CONSOLE_PLAYER
from Dadabase.modules.format import format_embed_list
import discord



async def leaderboard_clan_list_console_players(interaction):
    clan_data = read_data(CLANS_DATA_PATH, interaction.guild.id)
    msg = format_embed_list(clan_data, DATA_KEY_FOR_CONSOLE_PLAYERS)
    embed = __create_embed(msg)
    await interaction.response.send_message(embed=embed)


def __create_embed(msg):
    return discord.Embed(title="Console Players", description=f"The following players will be added to the leaderboard manually. To add another run: `{LEADERBOARD_CLAN_LIST_CONSOLE_PLAYERS.name}`. To remove one run: `{LEADERBOARD_CLAN_REMOVE_CONSOLE_PLAYER.name}`\n" + msg, color=0x00ff00)
