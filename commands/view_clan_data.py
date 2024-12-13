from modules.data_management import read_data, CLANS_DATA_PATH
from discord import Interaction, Embed

async def view_clan_data(interaction:Interaction):
    clan_data = read_data(CLANS_DATA_PATH, interaction.guild.id)
    embed = Embed(title="Clan Information", description="To edit any of the following fields run `/edit_clan`", color=int(clan_data['color'], 16))  # Convert hex color to int
    
    # Add fields to the embed
    for key, value in clan_data.items():
        if isinstance(value, list):
            continue
        elif isinstance(value, dict):
            value = ', '.join(f"{k}: {v}" for k, v in value.items())  # Flatten dicts
        else:
            value = str(value)  # Convert other types to string
        
        embed.add_field(name=key, value=value, inline=True)

    embed.set_footer(text='Run /console_player_list or /account_linker_list for additional information')
    await interaction.response.send_message(embed=embed)