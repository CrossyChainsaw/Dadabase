from Dadabase.modules.data_management import embed_with_link_data, find_link, read_link_data, SERVERS_DATA_PATH, embed_no_claimed_account
from Dadabase.classes.Link import Link


async def check(interaction):
    link_data = read_link_data(SERVERS_DATA_PATH, interaction.guild.id)
    link = find_link(interaction.user.id, link_data)
    if link:
        await interaction.response.send_message(embed=embed_with_link_data(link, interaction))
    else:
        await interaction.response.send_message(embed=embed_no_claimed_account())