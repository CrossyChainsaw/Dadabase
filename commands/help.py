from Dadabase.modules.command import ALL_COMMANDS
from discord import Interaction, Embed
import discord

async def help(interaction:Interaction):
    print('hello???')
    embed = Embed(title='All the Commands', description='')
    for command in ALL_COMMANDS:
        embed.description+=f"**/{command.name}**\n"
        embed.description+=f"{command.description}\n"
    await interaction.response.send_message(embed=embed)