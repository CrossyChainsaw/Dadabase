from Dadabase.modules.command import ALL_COMMANDS
from discord import Interaction, Embed

async def help(interaction: Interaction):
    embed = Embed(title='All the Commands', description='')

    for command in sorted(ALL_COMMANDS, key=lambda c: c.name.lower()):
        embed.description += f"**/{command.name}**\n"
        embed.description += f"{command.description}\n"

    await interaction.response.send_message(embed=embed)
