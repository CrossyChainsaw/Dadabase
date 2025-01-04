from Dadabase.modules.data_management import DATA_KEY_FOR_SHOW_AVERAGE_ELO, DATA_KEY_FOR_SHOW_1V1_LEGENDS, DATA_KEY_FOR_SHOW_2V2_LEGENDS, DATA_KEY_FOR_SHOW_WIN_LOSS, DATA_KEY_FOR_SHOW_MEMBER_COUNT, DATA_KEY_FOR_SHOW_NO_ELO_PLAYERS, read_data, CLANS_DATA_PATH, write_data, DATA_KEY_FOR_SHOW_XP
from Dadabase.modules.format import bool_to_show_hide, format_color
from discord import Embed


async def edit_clan(interaction, 
                    leaderboard_title:str, 
                    color:str,
                    image, 
                    channel_1v1_id:str, 
                    channel_2v2_id:str, 

                    channel_rotating_id:str, 
                    sorting_method:str, 
                    show_member_count:bool, 
                    show_xp:bool, 
                    show_no_elo_players:bool, 
                    show_win_loss:bool, 
                    show_1v1_legends:bool, 
                    show_2v2_legends:bool,
                    show_average_elo:bool):
    # load data
    clan_data = read_data(CLANS_DATA_PATH, interaction.guild.id)
    # Check if any parameter has been filled in
    if any([leaderboard_title is not None,
            color is not None, 
            image is not None, 
            channel_1v1_id is not None, 
            channel_2v2_id is not None, 

            channel_rotating_id is not None, 
            sorting_method is not None, 
            show_member_count is not None, 
            show_xp is not None, 
            show_no_elo_players is not None, 
            show_win_loss is not None, 
            show_1v1_legends is not None,
            show_2v2_legends is not None,
            show_average_elo is not None]):

        # Update clan_data with non-empty parameters
        variable_names = []
        old_values = []
        new_values = []

        # Required
        if leaderboard_title:
            variable_names.append("leaderboard_title")
            old_values.append(clan_data.get('leaderboard_title'))
            new_values.append(leaderboard_title)
            clan_data['leaderboard_title'] = leaderboard_title
        if color:
            variable_names.append("color")
            old_values.append(clan_data.get('color'))
            new_values.append(format_color(color))
            clan_data['color'] = format_color(color)
        if image:
            variable_names.append("image")
            old_values.append(clan_data.get('image'))
            new_values.append(image)
            clan_data['image'] = image
        if channel_1v1_id:
            variable_names.append("channel_1v1_id")
            old_values.append(clan_data.get('channel_1v1_id'))
            new_values.append(int(channel_1v1_id))
            clan_data['channel_1v1_id'] = int(channel_1v1_id)
        if channel_2v2_id:
            variable_names.append("channel_2v2_id")
            old_values.append(clan_data.get('channel_2v2_id'))
            new_values.append(int(channel_2v2_id))
            clan_data['channel_2v2_id'] = int(channel_2v2_id)

        # Optional
        if channel_rotating_id:
            variable_names.append("channel_rotating_id")
            old_values.append(clan_data.get('channel_rotating_id'))
            new_values.append(int(channel_rotating_id))
            clan_data['channel_rotating_id'] = int(channel_rotating_id)
        if sorting_method:
            variable_names.append("sorting_method")
            old_values.append(clan_data.get('sorting_method'))
            new_values.append(sorting_method)
            clan_data['sorting_method'] = sorting_method
        if show_member_count is not None:
            variable_names.append(DATA_KEY_FOR_SHOW_MEMBER_COUNT)
            old_values.append(clan_data.get(DATA_KEY_FOR_SHOW_MEMBER_COUNT))
            new_values.append(show_member_count)
            clan_data[DATA_KEY_FOR_SHOW_MEMBER_COUNT] = show_member_count
        if show_xp is not None:
            variable_names.append(DATA_KEY_FOR_SHOW_XP)
            old_values.append(clan_data.get(DATA_KEY_FOR_SHOW_XP))
            new_values.append(show_xp)
            clan_data[DATA_KEY_FOR_SHOW_XP] = show_xp
        if show_no_elo_players is not None:
            variable_names.append(DATA_KEY_FOR_SHOW_NO_ELO_PLAYERS)
            old_values.append(clan_data.get(DATA_KEY_FOR_SHOW_NO_ELO_PLAYERS))
            new_values.append(show_no_elo_players)
            clan_data[DATA_KEY_FOR_SHOW_NO_ELO_PLAYERS] = show_no_elo_players
        if show_win_loss is not None:
            variable_names.append(DATA_KEY_FOR_SHOW_WIN_LOSS)
            old_values.append(clan_data.get(DATA_KEY_FOR_SHOW_WIN_LOSS))
            new_values.append(show_win_loss)
            clan_data[DATA_KEY_FOR_SHOW_WIN_LOSS] = show_win_loss
        if show_1v1_legends is not None:
            variable_names.append(DATA_KEY_FOR_SHOW_1V1_LEGENDS)
            old_values.append(clan_data.get(DATA_KEY_FOR_SHOW_1V1_LEGENDS))
            new_values.append(show_1v1_legends)
            clan_data[DATA_KEY_FOR_SHOW_1V1_LEGENDS] = show_1v1_legends
        if show_2v2_legends is not None:
            variable_names.append(DATA_KEY_FOR_SHOW_2V2_LEGENDS)
            old_values.append(clan_data.get(DATA_KEY_FOR_SHOW_2V2_LEGENDS))
            new_values.append(show_2v2_legends)
            clan_data[DATA_KEY_FOR_SHOW_2V2_LEGENDS] = show_2v2_legends
        if show_average_elo is not None:
            variable_names.append(DATA_KEY_FOR_SHOW_AVERAGE_ELO)
            old_values.append(clan_data.get(DATA_KEY_FOR_SHOW_AVERAGE_ELO))
            new_values.append(show_average_elo)
            clan_data[DATA_KEY_FOR_SHOW_AVERAGE_ELO] = show_average_elo
            

        write_data(CLANS_DATA_PATH, clan_data, interaction.guild.id)
        await interaction.response.send_message(embed=prep_edit_guild_embed(old_values, new_values, variable_names))
    else:
        await interaction.response.send_message("No parameter has been provided")

def prep_edit_guild_embed(old_values:list, new_values:list, variable_names:list):
    embed = Embed(title='Data Changes', description='')
    embed.description+='**Old Values**\n'
    for name, val in zip(variable_names, old_values):
        embed.description+=f'- {name}: {val}\n'
    embed.description+='**New Values**\n'
    for name, val in zip(variable_names, new_values):
        embed.description+=f'- {name}: {val}\n'
    return embed