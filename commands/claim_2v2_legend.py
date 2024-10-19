from Dadabase.modules.data_management import read_data, write_data, CLANS_DATA_PATH, DATA_KEY_FOR_2V2_LEGENDS
from Dadabase.classes.BrawlhallaAccount import BrawlhallaAccount
import discord

async def claim_2v2_legend(interaction:discord.Interaction, brawlhalla_id:int, legend):
    server_id = interaction.guild.id
    data = read_data(CLANS_DATA_PATH, server_id)
    for entry in data[DATA_KEY_FOR_2V2_LEGENDS]:
        if str(entry['brawlhalla_id']) == str(brawlhalla_id):
            entry['legend_key'] = legend
            write_data(CLANS_DATA_PATH, data, server_id)
            break
    else:
        a = BrawlhallaAccount(brawlhalla_id, interaction.user.name, legend_key=legend)
        data[DATA_KEY_FOR_2V2_LEGENDS].append(a.__dict__)
        write_data(CLANS_DATA_PATH, data, server_id)
    await interaction.response.send_message('done')

    