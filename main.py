## hey i was refactoring dadabase to be structured like queen spy folderwise
## and cleaning functions cleaning modules making them more independant

import discord
from discord import app_commands
from typing import List
from Dadabase.commands.account_linker_list import account_linker_list
from Dadabase.commands.add_account_linker import add_account_linker
from Dadabase.commands.add_console_player import add_console_player
from Dadabase.commands.add_server_player import add_server_player
from Dadabase.commands.console_player_list import console_player_list
from Dadabase.commands.check import check
from Dadabase.commands.claim import claim
from Dadabase.commands.claim_2v2_legend import claim_2v2_legend
from Dadabase.commands.edit_clan import edit_clan
from Dadabase.commands.edit_server import edit_server
from Dadabase.commands.help import help
from Dadabase.commands.initialise_clan import initialise_clan
from Dadabase.commands.initialise_server import initialise_server
from Dadabase.commands.ping import ping
from Dadabase.commands.remove_account_linker import remove_account_linker
from Dadabase.commands.remove_console_player import remove_console_player
from Dadabase.commands.remove_server_player import remove_server_player
from Dadabase.commands.server_player_list import server_player_list
from Dadabase.commands.view_clan_data import view_clan_data
from Dadabase.modules.command import ALL_COUNTRIES, COUNTRIES_DICT, VIEW_CLAN_DATA, BRAWL_SERVERS, HELP_COMMAND, CHECK_COMMAND, CLAIM_COMMAND, CLAIM_2V2_LEGEND, INITIALISE_CLAN_COMMAND, INITIALISE_SERVER_COMMAND, CONSOLE_PLAYER_LIST, FLAG_TYPE_OPTIONS, REMOVE_ACCOUNT_LINKER_COMMAND, SERVER_PLAYER_LIST, SORTING_METHOD_OPTIONS, ACCOUNT_LINKER_LIST_COMMAND, ADD_ACCOUNT_LINKER_COMMAND, PING_COMMAND, EDIT_CLAN_COMMAND, ADD_SERVER_PLAYER_COMMAND, EDIT_SERVER_COMMAND, ADD_CONSOLE_PLAYER_COMMAND, REMOVE_SERVER_PLAYER_COMMAND, REMOVE_CONSOLE_PLAYER_COMMAND
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


@tree.command(name=ACCOUNT_LINKER_LIST_COMMAND.name, description=ACCOUNT_LINKER_LIST_COMMAND.description)
async def account_linker_list_command(interaction):
    await account_linker_list(interaction)


@tree.command(name=ADD_ACCOUNT_LINKER_COMMAND.name, description=ADD_ACCOUNT_LINKER_COMMAND.description)
@is_admin_or_crossy()
@app_commands.describe(clan_index="First clan is 0, second clan is 1 etc, third is 2 etc.")
async def add_account_linker_command(interaction, brawlhalla_id:int, brawlhalla_name:str, clan_index:str):
    await add_account_linker(interaction, brawlhalla_id, brawlhalla_name, clan_index)


@tree.command(name=ADD_CONSOLE_PLAYER_COMMAND.name, description=ADD_CONSOLE_PLAYER_COMMAND.description)
@is_admin_or_crossy()
@app_commands.describe(clan_index="First clan is 0, second clan is 1 etc, third is 2 etc.")
async def add_console_player_command(interaction, brawlhalla_id:int, brawlhalla_name:str, clan_index:int):
    await add_console_player(interaction, brawlhalla_id, brawlhalla_name, clan_index)





async def autocomplete_country(interaction: discord.Interaction, current: str) -> List[app_commands.Choice[str]]:
    matches = [
        app_commands.Choice(name=country, value=code)
        for country, code in COUNTRIES_DICT.items()
        if current.lower() in country.lower()
    ]
    return matches[:25]  # Discord max limit for shown results

@tree.command(
    name=ADD_SERVER_PLAYER_COMMAND.name,
    description=ADD_SERVER_PLAYER_COMMAND.description
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
async def add_server_player_command(
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
    await add_server_player(
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


@tree.command(name=CONSOLE_PLAYER_LIST.name, description=CONSOLE_PLAYER_LIST.description)
async def console_player_list_command(interaction):
    await console_player_list(interaction)


@tree.command(name=EDIT_CLAN_COMMAND.name, description=EDIT_CLAN_COMMAND.description)
@is_admin_or_crossy()
@app_commands.describe(sorting_method="What elo should be prioritised?")
@app_commands.describe(color="Example: #5e357a")
@app_commands.choices(sorting_method=SORTING_METHOD_OPTIONS)
async def edit_clan_command(interaction, 
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
    await edit_clan(interaction, 
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


@tree.command(name=EDIT_SERVER_COMMAND.name, description=EDIT_SERVER_COMMAND.description)
@is_admin_or_crossy()
@app_commands.describe(sorting_method="What elo should be prioritised?")
@app_commands.choices(sorting_method=SORTING_METHOD_OPTIONS)
@app_commands.describe(flag_type="What flag should be shown next to each player?")
@app_commands.choices(flag_type=FLAG_TYPE_OPTIONS)
async def edit_server_command(interaction, 
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
    await edit_server(interaction, 
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


@tree.command(name=INITIALISE_CLAN_COMMAND.name, description=INITIALISE_CLAN_COMMAND.description)
@is_admin_or_crossy()
@app_commands.describe(sorting_method="What elo should be prioritised?")
@app_commands.choices(sorting_method=SORTING_METHOD_OPTIONS)
@app_commands.describe(color = "Provide a Hex color code")
async def initialise_clan_command(interaction, 
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
    await initialise_clan(interaction, clan_names, channel_1v1_id, channel_2v2_id, clan_id, color, image, 
                         sorting_method.value, show_member_count, show_xp, show_no_elo_players, channel_rotating_id, server_id, server_name)


@tree.command(name=INITIALISE_SERVER_COMMAND.name, description=INITIALISE_SERVER_COMMAND.description)
@is_admin_or_crossy()
@app_commands.describe(sorting_method="What elo should be prioritised?")
@app_commands.choices(sorting_method=SORTING_METHOD_OPTIONS)
@app_commands.describe(flag_type="What flag should be shown next to each player?")
@app_commands.choices(flag_type=FLAG_TYPE_OPTIONS)
@app_commands.describe(color = "Provide a Hex color code")
async def initialise_server_command(interaction, 
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
    await initialise_server(interaction, leaderboard_title, sorting_method.value, show_member_count, show_no_elo_players, channel_1v1_id, channel_2v2_id, channel_rotating_id, color, image, flag_type.value)


@tree.command(name=PING_COMMAND.name)
async def ping_command(interaction):
    await ping(interaction)


@tree.command(name=REMOVE_ACCOUNT_LINKER_COMMAND.name, description=REMOVE_ACCOUNT_LINKER_COMMAND.description)
@is_admin_or_crossy()
async def remove_account_linker_command(interaction, brawlhalla_id:int):
    await remove_account_linker(interaction, brawlhalla_id)


@tree.command(name=REMOVE_CONSOLE_PLAYER_COMMAND.name, description=REMOVE_CONSOLE_PLAYER_COMMAND.description)
@is_admin_or_crossy()
async def remove_console_player_command(interaction, brawlhalla_id:int):
    await remove_console_player(interaction, brawlhalla_id)


@tree.command(name=REMOVE_SERVER_PLAYER_COMMAND.name, description=REMOVE_SERVER_PLAYER_COMMAND.description)
@is_admin_or_crossy()
async def remove_server_player_command(interaction, brawlhalla_id:int):
    await remove_server_player(interaction, brawlhalla_id)


@tree.command(name=SERVER_PLAYER_LIST.name, description=SERVER_PLAYER_LIST.description)
@is_admin_or_crossy()
async def server_player_list_command(interaction):
    await server_player_list(interaction)

@tree.command(name=VIEW_CLAN_DATA.name, description=VIEW_CLAN_DATA.description)
@is_admin_or_crossy()
async def view_clan_data_command(interaction):
    await view_clan_data(interaction)

    

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
