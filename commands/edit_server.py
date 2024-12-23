from Dadabase.modules.data_management import DATA_KEY_FOR_SHOW_1V1_LEGENDS, DATA_KEY_FOR_SHOW_2V2_LEGENDS, DATA_KEY_FOR_SHOW_WIN_LOSS, DATA_KEY_FOR_COLOR, DATA_KEY_FOR_IMAGE, DATA_KEY_FOR_SHOW_MEMBER_COUNT, DATA_KEY_FOR_CHANNEL_1V1_ID, DATA_KEY_FOR_CHANNEL_2V2_ID, DATA_KEY_FOR_CHANNEL_ROTATING_ID, DATA_KEY_FOR_LEADERBOARD_TITLE, DATA_KEY_FOR_FLAG_TYPE, DATA_KEY_FOR_SERVER_ID, DATA_KEY_FOR_SERVER_NAME, DATA_KEY_FOR_SHOW_NO_ELO_PLAYERS, DATA_KEY_FOR_SHOW_XP, DATA_KEY_FOR_SORTING_METHOD, DATA_KEY_FOR_SHOW_MEMBER_COUNT, DATA_KEY_FOR_SHOW_NO_ELO_PLAYERS, SERVERS_DATA_PATH, FlagType, read_data, write_data, DATA_KEY_FOR_SHOW_XP
from Dadabase.modules.format import bool_to_show_hide, format_color
from Dadabase.classes.Server import Server
from discord import Embed


async def edit_server(interaction, 
                      leaderboard_title:str, 
                      sorting_method:str, 
                      show_member_count:bool,
                      show_no_elo_players:bool,

                      channel_1v1_id:str, 
                      channel_2v2_id:str, 
                      channel_rotating_id:str, 
                      image:str, 
                      color:str, 
                      flag_type:str, 
                      show_win_loss:bool, 
                      show_1v1_legends:bool,
                      show_2v2_legends:bool):
    # load data
    server_data = read_data(SERVERS_DATA_PATH, interaction.guild.id)
    # Check if any parameter has been filled in
    if any([leaderboard_title is not None, 
            sorting_method is not None, 
            show_member_count is not None,
            show_no_elo_players is not None, 
            
            channel_1v1_id is not None, 
            channel_2v2_id is not None,
            channel_rotating_id is not None, 
            image is not None, 
            color is not None, 
            flag_type is not None, 
            show_win_loss is not None, 
            show_1v1_legends is not None,
            show_2v2_legends is not None,
            ]):

        variable_names = []
        old_values = []
        new_values = []
        
        # Required
        if leaderboard_title:
            variable_names.append(DATA_KEY_FOR_LEADERBOARD_TITLE)
            old_values.append(server_data[DATA_KEY_FOR_LEADERBOARD_TITLE])
            new_values.append(leaderboard_title)
            server_data[DATA_KEY_FOR_LEADERBOARD_TITLE] = leaderboard_title
        if sorting_method:
            variable_names.append(DATA_KEY_FOR_SORTING_METHOD)
            old_values.append(server_data[DATA_KEY_FOR_SORTING_METHOD])
            new_values.append(sorting_method.value)
            server_data[DATA_KEY_FOR_SORTING_METHOD] = sorting_method.value
        if show_member_count is not None:
            variable_names.append(DATA_KEY_FOR_SHOW_MEMBER_COUNT)
            old_values.append(server_data[DATA_KEY_FOR_SHOW_MEMBER_COUNT])
            new_values.append(show_member_count)
            server_data[DATA_KEY_FOR_SHOW_MEMBER_COUNT] = show_member_count
        if show_no_elo_players is not None:
            variable_names.append(DATA_KEY_FOR_SHOW_NO_ELO_PLAYERS)
            old_values.append(server_data[DATA_KEY_FOR_SHOW_NO_ELO_PLAYERS])
            new_values.append(show_no_elo_players)
            server_data[DATA_KEY_FOR_SHOW_NO_ELO_PLAYERS] = show_no_elo_players

        # Optional
        if channel_1v1_id:
            variable_names.append(DATA_KEY_FOR_CHANNEL_1V1_ID)
            old_values.append(server_data[DATA_KEY_FOR_CHANNEL_1V1_ID])
            new_values.append(int(channel_1v1_id))
            server_data[DATA_KEY_FOR_CHANNEL_1V1_ID] = int(channel_1v1_id)
        if channel_2v2_id:
            variable_names.append(DATA_KEY_FOR_CHANNEL_2V2_ID)
            old_values.append(server_data[DATA_KEY_FOR_CHANNEL_2V2_ID])
            new_values.append(int(channel_2v2_id))
            server_data[DATA_KEY_FOR_CHANNEL_2V2_ID] = int(channel_2v2_id)
        if channel_rotating_id:
            variable_names.append(DATA_KEY_FOR_CHANNEL_ROTATING_ID)
            old_values.append(server_data[DATA_KEY_FOR_CHANNEL_ROTATING_ID])
            new_values.append(int(channel_rotating_id))
            server_data[DATA_KEY_FOR_CHANNEL_ROTATING_ID] = int(channel_rotating_id)
        if image:
            variable_names.append(DATA_KEY_FOR_IMAGE)
            old_values.append(server_data[DATA_KEY_FOR_IMAGE])
            new_values.append(image)
            server_data[DATA_KEY_FOR_IMAGE] = image
        if color:
            variable_names.append(DATA_KEY_FOR_COLOR)
            old_values.append(server_data[DATA_KEY_FOR_COLOR])
            new_values.append(color)
            server_data[DATA_KEY_FOR_COLOR] = color
        if flag_type:
            variable_names.append(DATA_KEY_FOR_FLAG_TYPE)
            old_values.append(server_data[DATA_KEY_FOR_FLAG_TYPE])
            new_values.append(flag_type.value)
            server_data[DATA_KEY_FOR_FLAG_TYPE] = flag_type.value
        if show_win_loss is not None:
            variable_names.append(DATA_KEY_FOR_SHOW_WIN_LOSS)
            old_values.append(server_data[DATA_KEY_FOR_SHOW_WIN_LOSS])
            new_values.append(show_win_loss)
            server_data[DATA_KEY_FOR_SHOW_WIN_LOSS] = show_win_loss
        if show_1v1_legends is not None:
            variable_names.append(DATA_KEY_FOR_SHOW_1V1_LEGENDS)
            old_values.append(server_data[DATA_KEY_FOR_SHOW_1V1_LEGENDS])
            new_values.append(show_1v1_legends)
            server_data[DATA_KEY_FOR_SHOW_1V1_LEGENDS] = show_1v1_legends
        if show_2v2_legends is not None:
            variable_names.append(DATA_KEY_FOR_SHOW_2V2_LEGENDS)
            old_values.append(server_data[DATA_KEY_FOR_SHOW_2V2_LEGENDS])
            new_values.append(show_2v2_legends)
            server_data[DATA_KEY_FOR_SHOW_2V2_LEGENDS] = show_2v2_legends


        write_data(SERVERS_DATA_PATH, server_data, interaction.guild.id)
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