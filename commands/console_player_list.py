from Dadabase.modules.data_management import read_data, DATA_KEY_FOR_CONSOLE_PLAYERS, CLANS_DATA_PATH
from Dadabase.modules.command import CONSOLE_PLAYER_LIST, REMOVE_CONSOLE_PLAYER_COMMAND
from Dadabase.modules.format import format_embed_list
import discord



async def console_player_list(interaction):
    clan_data = read_data(CLANS_DATA_PATH, interaction.guild.id)
    msg = format_embed_list(clan_data, DATA_KEY_FOR_CONSOLE_PLAYERS)
    embed = __create_embed(msg)
    await interaction.response.send_message(embed=embed)


def __create_embed(msg):
    return discord.Embed(title="Console Players", description=f"The following players will be added to the leaderboard manually. To add another run: `{CONSOLE_PLAYER_LIST.name}`. To remove one run: `{REMOVE_CONSOLE_PLAYER_COMMAND.name}`\n" + msg, color=0x00ff00)
