from Dadabase.modules.data_management import read_data, write_data, CLANS_DATA_PATH, DATA_KEY_FOR_2V2_LEGENDS, BRAWLHALLA_LEGENDS, DATA_KEY_FOR_OWN_2V2_LEGEND, DATA_KEY_FOR_MATE_2V2_LEGEND

from Dadabase.classes.BrawlhallaAccount import BrawlhallaAccount
import discord

async def claim_2v2_legend(interaction:discord.Interaction, brawlhalla_id:int, your_legend_input:str, teammate_legend_input:str):
    acc = BrawlhallaAccount(brawlhalla_id, interaction.user.name, interaction.user.id)
    your_legend = (your_legend_input.replace(" ", "")).lower()
    teammate_legend = (teammate_legend_input.replace(" ", "")).lower()
    if your_legend in BRAWLHALLA_LEGENDS and teammate_legend in BRAWLHALLA_LEGENDS:
        acc.own_legend = your_legend
        acc.mate_legend = teammate_legend
    else:
        # Invalid input, handle the error
        await interaction.response.send_message(f"One or both legends are invalid. Please check the spelling: {your_legend_input}, {teammate_legend_input}")
        return
    
    server_id = interaction.guild.id
    data = read_data(CLANS_DATA_PATH, server_id)
    # update
    for entry in data[DATA_KEY_FOR_2V2_LEGENDS]:
        if str(entry['discord_id']) == str(interaction.user.id):
            entry['brawlhalla_id'] = acc.brawlhalla_id
            entry[DATA_KEY_FOR_OWN_2V2_LEGEND] = acc.own_legend
            entry[DATA_KEY_FOR_MATE_2V2_LEGEND] = acc.mate_legend
            write_data(CLANS_DATA_PATH, data, server_id)
            break
    # write
    else:
        data[DATA_KEY_FOR_2V2_LEGENDS].append(acc.__dict__)
        write_data(CLANS_DATA_PATH, data, server_id)
    await interaction.response.send_message(f'You claimed {acc.own_legend} & {acc.mate_legend}. These legends will appear next to your best team next update.')


    