import json
from Dadabase.modules.api import fetch_player_ranked_stats
from Dadabase.classes.Link import Link
from Dadabase.modules.data_management import embed_with_link_data, find_link_index, read_link_data, write_data, read_data, SERVERS_DATA_PATH


async def claim(interaction, brawlhalla_id, region, country_of_residence, ethnicity):
    ranked_stats = await fetch_player_ranked_stats(brawlhalla_id)
    link = Link(ranked_stats['brawlhalla_id'], ranked_stats['name'], interaction.user.id, interaction.user.name, region, country_of_residence, ethnicity)
    condition = __already_claimed(interaction)
    if condition == True:
        print('updating link')
        await __update_link(interaction, link)
    else:
        await __add_link(interaction, link)
    

def __already_claimed(interaction):
    print('Entered: already_claimed()')
    link_data = []
    link_data = read_link_data(SERVERS_DATA_PATH, interaction.guild.id)
    for user in link_data:
        if str(interaction.user.id) == str(user['discord_id']):
            return True
    return False


async def __add_link(interaction, link:Link):
    print('Entered: __add_link()')
    __save_data(interaction, link)
    await interaction.response.send_message(embed=embed_with_link_data(link, interaction))


async def __update_link(interaction, new_link:Link):
    print('Entered: __update_link()')
    server_data = read_data(SERVERS_DATA_PATH, interaction.guild.id)
    print(server_data)
    link_data = server_data['links']
    link_index = find_link_index(interaction.user.id, link_data)
    link = link_data[link_index]
    link['brawlhalla_id'] = new_link.brawlhalla_id
    link['brawlhalla_name'] = new_link.brawlhalla_name
    link['region'] = new_link.region
    link['country'] = new_link.country
    link['ethnicity'] = new_link.ethnicity
    server_data['links'][link_index] = link
    write_data(SERVERS_DATA_PATH, server_data, interaction.guild.id)
    await interaction.response.send_message(embed=embed_with_link_data(new_link, interaction))

def __save_data(interaction, user):
    print('Entered: __save_data()')
    server_data = read_data(SERVERS_DATA_PATH, interaction.guild.id)
    link_data = server_data['links']
    link_data.append(user.__dict__)
    server_data['links'] = link_data
    write_data(SERVERS_DATA_PATH, server_data, interaction.guild.id)