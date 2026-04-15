## hey i was refactoring dadabase to be structured like queen spy folderwise
## and cleaning functions cleaning modules making them more independant

import discord
from discord import app_commands
from typing import List
from Dadabase.commands.account_linker_list import leaderboard_clan_list_hidden_players
from Dadabase.commands.add_account_linker import leaderboard_clan_hide_players
from Dadabase.commands.add_console_player import leaderboard_clan_add_console_player
from Dadabase.commands.add_server_player import leaderboard_community_add_player
from Dadabase.commands.console_player_list import leaderboard_clan_list_console_players
from Dadabase.commands.check import check
from Dadabase.commands.claim import claim
from Dadabase.commands.claim_2v2_legend import claim_2v2_legend
from Dadabase.commands.edit_clan import leaderboard_clan_edit_data
from Dadabase.commands.edit_server import leaderboard_community_edit_data
from Dadabase.commands.help import help
from Dadabase.commands.initialise_clan import leaderboard_clan_init
from Dadabase.commands.initialise_server import leaderboard_community_init
from Dadabase.commands.ping import ping
from Dadabase.commands.remove_account_linker import leaderboard_clan_unhide_player
from Dadabase.commands.remove_console_player import leaderboard_clan_remove_console_player
from Dadabase.commands.remove_server_player import leaderboard_community_remove_player
from Dadabase.commands.server_player_list import leaderboard_community_list_players
from Dadabase.commands.view_clan_data import leaderboard_clan_data
from Dadabase.modules.command import ALL_COUNTRIES, COUNTRIES_DICT, LEADERBOARD_CLAN_DATA, BRAWL_SERVERS, HELP_COMMAND, CHECK_COMMAND, CLAIM_COMMAND, CLAIM_2V2_LEGEND, LEADERBOARD_CLAN_INIT, LEADERBOARD_COMMUNITY_INIT, LEADERBOARD_CLAN_LIST_CONSOLE_PLAYERS, FLAG_TYPE_OPTIONS, LEADERBOARD_CLAN_UNHIDE_PLAYER, LEADERBOARD_COMMUNITY_LIST_PLAYERS, SORTING_METHOD_OPTIONS, LEADERBOARD_CLAN_LIST_HIDDEN_PLAYERS, LEADERBOARD_CLAN_HIDE_PLAYER, PING_COMMAND, LEADERBOARD_CLAN_EDIT_DATA, LEADERBOARD_COMMUNITY_ADD_PLAYER, LEADERBOARD_COMMUNITY_EDIT_DATA, LEADERBOARD_CLAN_ADD_CONSOLE_PLAYER, LEADERBOARD_COMMUNITY_REMOVE_PLAYER, LEADERBOARD_CLAN_REMOVE_CONSOLE_PLAYER
from Dadabase.modules.env import env_variable
from Dadabase.modules.check_permission import has_permission
from Dadabase.modules.data_management import FlagType
from Dadabase.modules.keep_alive import keep_alive
from Dadabase.modules.env import env_variable
from Dadabase.modules.decorators import is_admin_or_crossy

DADABASE_ACTIVE = env_variable("DADABASE_ACTIVE")
DADABASE_TESTING = env_variable("DADABASE_TESTING")


intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@tree.command(name=LEADERBOARD_CLAN_LIST_HIDDEN_PLAYERS.name, description=LEADERBOARD_CLAN_LIST_HIDDEN_PLAYERS.description)
async def leaderboard_clan_list_hidden_players_command(interaction):
    await leaderboard_clan_list_hidden_players(interaction)


@tree.command(name=LEADERBOARD_CLAN_HIDE_PLAYER.name, description=LEADERBOARD_CLAN_HIDE_PLAYER.description)
@is_admin_or_crossy()
@app_commands.describe(clan_index="First clan is 0, second clan is 1 etc, third is 2 etc.")
async def leaderboard_clan_hide_players_command(interaction, brawlhalla_id:int, brawlhalla_name:str, clan_index:str):
    await leaderboard_clan_hide_players(interaction, brawlhalla_id, brawlhalla_name, clan_index)


@tree.command(name=LEADERBOARD_CLAN_ADD_CONSOLE_PLAYER.name, description=LEADERBOARD_CLAN_ADD_CONSOLE_PLAYER.description)
@is_admin_or_crossy()
@app_commands.describe(clan_index="First clan is 0, second clan is 1 etc, third is 2 etc.")
async def leaderboard_clan_add_console_player_command(interaction, brawlhalla_id:int, brawlhalla_name:str, clan_index:int):
    await leaderboard_clan_add_console_player(interaction, brawlhalla_id, brawlhalla_name, clan_index)





async def autocomplete_country(interaction: discord.Interaction, current: str) -> List[app_commands.Choice[str]]:
    matches = [
        app_commands.Choice(name=country, value=code)
        for country, code in COUNTRIES_DICT.items()
        if current.lower() in country.lower()
    ]
    return matches[:25]  # Discord max limit for shown results

@tree.command(
    name=LEADERBOARD_COMMUNITY_ADD_PLAYER.name,
    description=LEADERBOARD_COMMUNITY_ADD_PLAYER.description
)
@is_admin_or_crossy()
@app_commands.describe(region="What server do you play on?")
@app_commands.choices(region=BRAWL_SERVERS)
@app_commands.describe(country_of_residence="Which country does the player live in?")
@app_commands.describe(ethnicity="What is the player's ethnicity?")
@app_commands.autocomplete(
    country_of_residence=autocomplete_country,
    ethnicity=autocomplete_country
)
async def leaderboard_community_add_player_command(
    interaction,
    brawlhalla_id: int,
    discord_id: str,
    discord_name: str,
    region: app_commands.Choice[str] = None,
    country_of_residence: str = "",
    ethnicity: str = ""
):
    # Validate country_of_residence
    valid_country_codes = set(COUNTRIES_DICT.values())
    valid_country_names = set(COUNTRIES_DICT.keys())
    
    def validate_country(input_str):
        if input_str.upper() in valid_country_codes:
            return input_str.upper()
        elif input_str.title() in valid_country_names:
            return COUNTRIES_DICT[input_str.title()]
        return None
    
    country_code = validate_country(country_of_residence)
    ethnicity_code = validate_country(ethnicity)
    
    if country_code is None:
        await interaction.response.send_message(
            f"Invalid country_of_residence '{country_of_residence}'. Please select a valid country.",
            ephemeral=True
        )
        return

    if ethnicity_code is None:
        await interaction.response.send_message(
            f"Invalid ethnicity '{ethnicity}'. Please select a valid country.",
            ephemeral=True
        )
        return
    
    discord_id = int(discord_id)
    await leaderboard_community_add_player(
        interaction,
        brawlhalla_id,
        discord_id,
        discord_name,
        region,
        country_code,
        ethnicity_code
    )








@tree.command(name=CHECK_COMMAND.name, description=CHECK_COMMAND.description)
async def check_command(interaction):
    await check(interaction)








@tree.command(name=CLAIM_COMMAND.name, description=CLAIM_COMMAND.description)
@app_commands.describe(region="What server do you play on?")
@app_commands.choices(region=BRAWL_SERVERS)
@app_commands.describe(country_of_residence="Which country do you live in?")
@app_commands.describe(ethnicity="What is your ethnicity?")
@app_commands.describe(your_legend="Type the legend you play in 2v2")
@app_commands.describe(teammate_legend="Type the legend your teammate plays in 2v2")
@app_commands.autocomplete(
    country_of_residence=autocomplete_country,
    ethnicity=autocomplete_country
)
async def claim_command(interaction, 
                        brawlhalla_id:int, 
                        region: app_commands.Choice[str],
                        country_of_residence: str, 
                        ethnicity: str,
                        your_legend: str = 'random',
                        teammate_legend: str = 'random'):
    # Validate country_of_residence and ethnicity inputs against your dict
    valid_country_codes = set(COUNTRIES_DICT.values())
    valid_country_names = set(COUNTRIES_DICT.keys())
    
    # Normalize inputs (for example, uppercase code, or title case name)
    input_country_code = None
    
    # Check if user entered country code or country name
    if country_of_residence.upper() in valid_country_codes:
        input_country_code = country_of_residence.upper()
    elif country_of_residence.title() in valid_country_names:
        input_country_code = COUNTRIES_DICT[country_of_residence.title()]
    else:
        await interaction.response.send_message(
            f"Invalid country_of_residence '{country_of_residence}'. Please select a valid country.",
            ephemeral=True
        )
        return
    
    input_ethnicity_code = None
    if ethnicity.upper() in valid_country_codes:
        input_ethnicity_code = ethnicity.upper()
    elif ethnicity.title() in valid_country_names:
        input_ethnicity_code = COUNTRIES_DICT[ethnicity.title()]
    else:
        await interaction.response.send_message(
            f"Invalid ethnicity '{ethnicity}'. Please select a valid country.",
            ephemeral=True
        )
        return

    print(f'{interaction.user.name} called claim!')
    if has_permission(interaction):
        await claim(interaction, brawlhalla_id, region.value, input_country_code, input_ethnicity_code, your_legend, teammate_legend)
    else:
        await interaction.response.send_message(f'{interaction.user.name} does not have permission to use this command', ephemeral=True)



# @tree.command(name=CLAIM_2V2_LEGEND.name, description=CLAIM_2V2_LEGEND.description)
# @app_commands.describe(your_legend="Type the legend you play in 2v2")
# @app_commands.describe(teammate_legend="Type the legend your teammate plays in 2v2")
# async def claim_2v2_legend_command(interaction, brawlhalla_id:int, your_legend:str, teammate_legend:str):
#     await claim_2v2_legend(interaction, brawlhalla_id, your_legend, teammate_legend)


@tree.command(name=LEADERBOARD_CLAN_LIST_CONSOLE_PLAYERS.name, description=LEADERBOARD_CLAN_LIST_CONSOLE_PLAYERS.description)
async def leaderboard_clan_list_console_players_command(interaction):
    await leaderboard_clan_list_console_players(interaction)


@tree.command(name=LEADERBOARD_CLAN_EDIT_DATA.name, description=LEADERBOARD_CLAN_EDIT_DATA.description)
@is_admin_or_crossy()
@app_commands.describe(sorting_method="What elo should be prioritised?")
@app_commands.describe(color="Example: #5e357a")
@app_commands.choices(sorting_method=SORTING_METHOD_OPTIONS)
async def leaderboard_clan_edit_data_command(interaction, 
                            leaderboard_title:str=None,
                            color:str=None, 
                            image:str=None, 
                            channel_1v1_id:str=None, 
                            channel_2v2_id:str=None, 
                            
                            channel_rotating_id:str = None,
                            sorting_method:app_commands.Choice[str]=None, 
                            show_member_count:bool=None, 
                            show_xp:bool=None, 
                            show_no_elo_players:bool=None,
                            show_win_loss:bool=None,
                            show_1v1_legends:bool=None, 
                            show_2v2_legends:bool=None,
                            show_average_elo:bool=None
                            ):
    await leaderboard_clan_edit_data(interaction, 
                    leaderboard_title,
                    color, 
                    image, 
                    channel_1v1_id, 
                    channel_2v2_id, 
                    
                    channel_rotating_id, 
                    sorting_method, 
                    show_member_count, 
                    show_xp, 
                    show_no_elo_players, 
                    show_win_loss, 
                    show_1v1_legends,
                    show_2v2_legends,
                    show_average_elo)


@tree.command(name=LEADERBOARD_COMMUNITY_EDIT_DATA.name, description=LEADERBOARD_COMMUNITY_EDIT_DATA.description)
@is_admin_or_crossy()
@app_commands.describe(sorting_method="What elo should be prioritised?")
@app_commands.choices(sorting_method=SORTING_METHOD_OPTIONS)
@app_commands.describe(flag_type="What flag should be shown next to each player?")
@app_commands.choices(flag_type=FLAG_TYPE_OPTIONS)
async def leaderboard_community_edit_data_command(interaction, 
                              leaderboard_title:str=None, 
                              sorting_method:app_commands.Choice[str]=None, 
                              show_member_count:bool=None, 
                              show_no_elo_players:bool=None, 

                              channel_1v1_id:str=None, 
                              channel_2v2_id:str=None, 
                              channel_rotating_id:str = None, 
                              image:str=None, 
                              color:str=None, 
                              flag_type:app_commands.Choice[str]=None,
                              show_win_loss:bool=None,
                              show_1v1_legends:bool=None,
                              show_2v2_legends:bool=None,
                              ):
    await leaderboard_community_edit_data(interaction, 
                      leaderboard_title, 
                      sorting_method, 
                      show_member_count, 
                      show_no_elo_players, 
                      
                      channel_1v1_id, 
                      channel_2v2_id, 
                      channel_rotating_id, 
                      image, 
                      color, 
                      flag_type, 
                      show_win_loss, 
                      show_1v1_legends,
                      show_2v2_legends)


@tree.command(name=HELP_COMMAND.name, description=HELP_COMMAND.description)
async def help_command(interaction):
    await help(interaction)


@tree.command(name=LEADERBOARD_CLAN_INIT.name, description=LEADERBOARD_CLAN_INIT.description)
@is_admin_or_crossy()
@app_commands.describe(sorting_method="What elo should be prioritised?")
@app_commands.choices(sorting_method=SORTING_METHOD_OPTIONS)
@app_commands.describe(color = "Provide a Hex color code")
async def leaderboard_clan_init_command(interaction, 
                                  clan_names:str, 
                                  channel_1v1_id:str, 
                                  channel_2v2_id:str, 
                                  clan_id:str, 
                                  color:str,
                                  sorting_method: app_commands.Choice[str], 
                                  show_member_count: bool, 
                                  show_no_elo_players: bool, 
                                  show_xp: bool, 
                                  channel_rotating_id:str=None, 
                                  image:str="", 
                                  server_id:str=None, 
                                  server_name:str=None):
    await leaderboard_clan_init(interaction, clan_names, channel_1v1_id, channel_2v2_id, clan_id, color, image, 
                         sorting_method.value, show_member_count, show_xp, show_no_elo_players, channel_rotating_id, server_id, server_name)


@tree.command(name=LEADERBOARD_COMMUNITY_INIT.name, description=LEADERBOARD_COMMUNITY_INIT.description)
@is_admin_or_crossy()
@app_commands.describe(sorting_method="What elo should be prioritised?")
@app_commands.choices(sorting_method=SORTING_METHOD_OPTIONS)
@app_commands.describe(flag_type="What flag should be shown next to each player?")
@app_commands.choices(flag_type=FLAG_TYPE_OPTIONS)
@app_commands.describe(color = "Provide a Hex color code")
async def leaderboard_community_init_command(interaction, 
                                   leaderboard_title:str,
                                   sorting_method: app_commands.Choice[str], 
                                   show_member_count: bool,
                                   show_no_elo_players: bool,
                                   channel_1v1_id:str,
                                   channel_2v2_id:str,
                                   channel_rotating_id:str,
                                   flag_type:app_commands.Choice[str],
                                   color:str="0xFFFFFF",
                                   image:str=""):
    await leaderboard_community_init(interaction, leaderboard_title, sorting_method.value, show_member_count, show_no_elo_players, channel_1v1_id, channel_2v2_id, channel_rotating_id, color, image, flag_type.value)


@tree.command(name=PING_COMMAND.name)
async def ping_command(interaction):
    await ping(interaction)


@tree.command(name=LEADERBOARD_CLAN_UNHIDE_PLAYER.name, description=LEADERBOARD_CLAN_UNHIDE_PLAYER.description)
@is_admin_or_crossy()
async def leaderboard_clan_unhide_player_command(interaction, brawlhalla_id:int):
    await leaderboard_clan_unhide_player(interaction, brawlhalla_id)


@tree.command(name=LEADERBOARD_CLAN_REMOVE_CONSOLE_PLAYER.name, description=LEADERBOARD_CLAN_REMOVE_CONSOLE_PLAYER.description)
@is_admin_or_crossy()
async def leaderboard_clan_remove_console_player_command(interaction, brawlhalla_id:int):
    await leaderboard_clan_remove_console_player(interaction, brawlhalla_id)


@tree.command(name=LEADERBOARD_COMMUNITY_REMOVE_PLAYER.name, description=LEADERBOARD_COMMUNITY_REMOVE_PLAYER.description)
@is_admin_or_crossy()
async def leaderboard_community_remove_player_command(interaction, brawlhalla_id:int):
    await leaderboard_community_remove_player(interaction, brawlhalla_id)


@tree.command(name=LEADERBOARD_COMMUNITY_LIST_PLAYERS.name, description=LEADERBOARD_COMMUNITY_LIST_PLAYERS.description)
@is_admin_or_crossy()
async def leaderboard_community_list_players_command(interaction):
    await leaderboard_community_list_players(interaction)

@tree.command(name=LEADERBOARD_CLAN_DATA.name, description=LEADERBOARD_CLAN_DATA.description)
@is_admin_or_crossy()
async def leaderboard_clan_data_command(interaction):
    await leaderboard_clan_data(interaction)

    

# sync everything up
@client.event
async def on_ready():
    await tree.sync()
    print(f'We have logged in as {client.user}')

def run_dadabase():
    if DADABASE_ACTIVE:
        keep_alive()
        client.run(env_variable("DADABASE_BOT_TOKEN"))
    if DADABASE_TESTING:
        keep_alive()
        client.run(env_variable("RANKNIR_TESTING_BOT_TOKEN"))
