from Dadabase.modules.data_management import read_data, SERVERS_DATA_PATH, DATA_KEY_FOR_SERVER_LINKS
from Dadabase.modules.command import LEADERBOARD_COMMUNITY_ADD_PLAYER, LEADERBOARD_COMMUNITY_REMOVE_PLAYER
from Dadabase.modules.format import format_embed_list_big
import discord



async def leaderboard_community_list_players(interaction):
    server_data = read_data(SERVERS_DATA_PATH, interaction.guild.id)
    msg, msg2 = format_embed_list_big(server_data, DATA_KEY_FOR_SERVER_LINKS)
    embed = __create_embed(msg)
    if len(msg2) > 0:
        embed2 = __create_embed(msg2)
        await interaction.response.send_message(embeds=[embed, embed2])
    else:
        await interaction.response.send_message(embed=embed)


def __create_embed(msg):
    return discord.Embed(title="Server Players", description=f"The following players will be added to the leaderboard. To add another run: `{LEADERBOARD_COMMUNITY_ADD_PLAYER.name}`. To remove one run: `{LEADERBOARD_COMMUNITY_REMOVE_PLAYER.name}`\n" + msg, color=0x00ff00)