from discord import app_commands
from Dadabase.classes.Command import Command

from Dadabase.modules.data_management import FlagType

# Defining all commands
ACCOUNT_LINKER_LIST_COMMAND = Command(name='account_linker_list', description='List all Account Linkers (Account Linker: player that should be removed from leaderboard manually)')
ADD_ACCOUNT_LINKER_COMMAND = Command(name='add_account_linker', description='Specify a player to remove from the leaderboard')
ADD_CONSOLE_PLAYER_COMMAND = Command(name='add_console_player', description='Add a console player')
ADD_SERVER_PLAYER_COMMAND = Command(name='add_server_player', description="(You aren't supposed to run this) Manually add a player to the server leaderboard")
CHECK_COMMAND = Command(name='check', description='Check your linked Brawlhalla account')
CLAIM_COMMAND = Command(name='claim', description='Link your Brawlhalla account to Discord')
CLAIM_2V2_LEGEND = Command(name='claim_2v2_legend_for_clans', description='Tell Ranknir what legend you play in 2v2')
CONSOLE_PLAYER_LIST = Command(name='console_player_list', description='List all console players')
EDIT_SERVER_COMMAND = Command(name='edit_server', description='Edit server data')
EDIT_CLAN_COMMAND = Command(name='edit_clan', description='Edit clan data')
HELP_COMMAND = Command(name='help', description='Help Command (This one)')
INITIALISE_CLAN_COMMAND = Command(name='initialise_clan', description="(You aren't supposed to run this) Generate a file with clan data for the current clan server")
INITIALISE_SERVER_COMMAND = Command(name='initialise_server', description="(You aren't supposed to run this) Generate a file with clan data for the current server")
PING_COMMAND = Command(name='ping', description='Check server response time')
REMOVE_ACCOUNT_LINKER_COMMAND = Command(name='remove_account_linker', description='Remove an Account Linker')
REMOVE_CONSOLE_PLAYER_COMMAND = Command(name='remove_console_player', description='Remove a console player')
REMOVE_SERVER_PLAYER_COMMAND = Command(name='remove_server_player', description="(You aren't supposed to run this) Manually remove a player from the server leaderboard")
SERVER_PLAYER_LIST = Command(name='server_player_list', description='List all server players')
VIEW_CLAN_DATA = Command(name='view_clan_data', description='List all the fields that are being used in the leaderboard')

ALL_COMMANDS = [
    ACCOUNT_LINKER_LIST_COMMAND,
    ADD_ACCOUNT_LINKER_COMMAND,
    ADD_CONSOLE_PLAYER_COMMAND,
    ADD_SERVER_PLAYER_COMMAND,
    CHECK_COMMAND,
    CLAIM_COMMAND,
    CLAIM_2V2_LEGEND,
    CONSOLE_PLAYER_LIST,
    EDIT_SERVER_COMMAND,
    EDIT_CLAN_COMMAND,
    HELP_COMMAND,
    INITIALISE_CLAN_COMMAND,
    INITIALISE_SERVER_COMMAND,
    PING_COMMAND,
    REMOVE_ACCOUNT_LINKER_COMMAND,
    REMOVE_CONSOLE_PLAYER_COMMAND,
    REMOVE_SERVER_PLAYER_COMMAND,
    SERVER_PLAYER_LIST,
    VIEW_CLAN_DATA
]


# App Commands Choices
BENELUX_COUNTRIES = [    
    app_commands.Choice(name="Netherlands", value="NL"),
    app_commands.Choice(name="Belgium", value="BE"),
    app_commands.Choice(name="Luxembourg", value="LU")]
ALL_COUNTRIES = [
    app_commands.Choice(name="Don't Specify", value=""),
    app_commands.Choice(name="Algeria", value="DZ"),
    app_commands.Choice(name="Argentina", value="AR"),
    app_commands.Choice(name="Belgium", value="BE"),
    app_commands.Choice(name="Brazil", value="BR"),
    app_commands.Choice(name="Canada", value="CA"),
    app_commands.Choice(name="Chile", value="CL"),
    app_commands.Choice(name="Curacao", value="CW"),
    app_commands.Choice(name="Dominican Republic", value="DO"),
    app_commands.Choice(name="Germany", value="DE"),
    app_commands.Choice(name="Indonesia", value="ID"),
    app_commands.Choice(name="Iraq", value="IQ"),
    app_commands.Choice(name="Italy", value="IT"),
    app_commands.Choice(name="Japan", value="JP"),
    app_commands.Choice(name="Luxembourg", value="LU"),
    app_commands.Choice(name="Morocco", value="MA"),
    app_commands.Choice(name="Netherlands", value="NL"),
    app_commands.Choice(name="Nigeria", value="NG"),
    app_commands.Choice(name="Romania", value="RO"),
    app_commands.Choice(name="Spain", value="ES"),
    app_commands.Choice(name="Suriname", value="SR"),
    app_commands.Choice(name="Syria", value="SY"),
    app_commands.Choice(name="Turkey", value="TR"),
    app_commands.Choice(name="United States of America", value="US"),
    app_commands.Choice(name="Vietnam", value="VN")
]
BRAWL_SERVERS = [
    app_commands.Choice(name="US-E", value="USE"),
    app_commands.Choice(name="US-W", value="USW"),
    app_commands.Choice(name="Europe", value="EU"),
    app_commands.Choice(name="South East Asia", value="SEA"),
    app_commands.Choice(name="Australia", value="AUS"),
    app_commands.Choice(name="Brazil", value="BRS"),
    app_commands.Choice(name="Japan", value="JPN"),
    app_commands.Choice(name="Middle East", value="MDE"),
    app_commands.Choice(name="Southern Africa", value="SAF"),
]
BRAWLHALLA_LEGENDS_EMOJIS = [
    app_commands.Choice(name="random", value="<:random:1295156657747132476>"),
    app_commands.Choice(name="bodvar", value="<:bodvar:1295142317044400140>"),
    app_commands.Choice(name="cassidy", value="<:cassidy:1295142767470575669>"),
    app_commands.Choice(name="orion", value="<:orion:1295142821396877422>"),
    app_commands.Choice(name="lordvraxx", value="<:lordvraxx:1295142831748546661>"),
    app_commands.Choice(name="gnash", value="<:gnash:1295142839126196264>"),
    app_commands.Choice(name="queennai", value="<:queennai:1295142867022512198>"),
    app_commands.Choice(name="hattori", value="<:hattori:1295142873867616286>"),
    app_commands.Choice(name="sirroland", value="<:sirroland:1295142882713403442>"),
    app_commands.Choice(name="scarlet", value="<:scarlet:1295143813358161981>"),
    app_commands.Choice(name="thatch", value="<:thatch:1295143831578083360>"),
    app_commands.Choice(name="ada", value="<:ada:1295143845989974047>"),
    app_commands.Choice(name="sentinel", value="<:sentinel:1295144096129749083>"),
    app_commands.Choice(name="lucien", value="<:lucien:1295144110260359208>"),
    app_commands.Choice(name="teros", value="<:teros:1295144119051485254>"),
    app_commands.Choice(name="brynn", value="<:brynn:1295144132557148241>"),
    app_commands.Choice(name="asuri", value="<:asuri:1295144158863822900>"),
    app_commands.Choice(name="barraza", value="<:barraza:1295144208767910049>"),
    app_commands.Choice(name="ember", value="<:ember:1295144232146829392>"),
    app_commands.Choice(name="azoth", value="<:azoth:1295144242804555837>"),
    app_commands.Choice(name="koji", value="<:koji:1295144252929474583>"),
    app_commands.Choice(name="ulgrim", value="<:ulgrim:1295144263545389080>"),
    app_commands.Choice(name="diana", value="<:diana:1295144273246683147>"),
    app_commands.Choice(name="jhala", value="<:jhala:1295144284437090324>"),
    app_commands.Choice(name="kor", value="<:kor:1295144479451516999>"),
    app_commands.Choice(name="wushang", value="<:wushang:1295144488473198774>"),
    app_commands.Choice(name="val", value="<:val:1295144502197092515>"),
    app_commands.Choice(name="ragnir", value="<:ragnir:1295144509453111357>"),
    app_commands.Choice(name="cross", value="<:cross:1295144518232051832>"),
    app_commands.Choice(name="mirage", value="<:mirage:1295144589849657416>"),
    app_commands.Choice(name="nix", value="<:nix:1295144633399120003>"),
    app_commands.Choice(name="mordex", value="<:mordex:1295144640345014404>"),
    app_commands.Choice(name="yumiko", value="<:yumiko:1295144647672201237>"),
    app_commands.Choice(name="artemis", value="<:artemis:1295144655163232317>"),
    app_commands.Choice(name="caspian", value="<:caspian:1295144662259990623>"),
    app_commands.Choice(name="sidra", value="<:sidra:1295144671710019704>"),
    app_commands.Choice(name="xull", value="<:xull:1295144682132602942>"),
    app_commands.Choice(name="kaya", value="<:kaya:1295144689225433218>"),
    app_commands.Choice(name="isaiah", value="<:isaiah:1295144735354261604>"),
    app_commands.Choice(name="jiro", value="<:jiro:1295144742232916090>"),
    app_commands.Choice(name="linfei", value="<:linfei:1295144753138237532>"),
    app_commands.Choice(name="zariel", value="<:zariel:1295144758980644904>"),
    app_commands.Choice(name="rayman", value="<:rayman:1295144768598315061>"),
    app_commands.Choice(name="dusk", value="<:dusk:1295144776395522149>"),
    app_commands.Choice(name="fait", value="<:fait:1295144788626112523>"),
    app_commands.Choice(name="thor", value="<:thor:1295144795798241371>"),
    app_commands.Choice(name="petra", value="<:petra:1295145039864791171>"),
    app_commands.Choice(name="vector", value="<:vector:1295145046169092156>"),
    app_commands.Choice(name="volkov", value="<:volkov:1295145065110568971>"),
    app_commands.Choice(name="onyx", value="<:onyx:1295145073016569966>"),
    app_commands.Choice(name="jaeyun", value="<:jaeyun:1295145081275285545>"),
    app_commands.Choice(name="mako", value="<:mako:1295145090234454028>"),
    app_commands.Choice(name="magyar", value="<:magyar:1295145096571916381>"),
    app_commands.Choice(name="reno", value="<:reno:1295145105916690496>"),
    app_commands.Choice(name="munin", value="<:munin:1295145114464686310>"),
    app_commands.Choice(name="arcadia", value="<:arcadia:1295145122408697910>"),
    app_commands.Choice(name="ezio", value="<:ezio:1295145131481239623>"),
    app_commands.Choice(name="tezca", value="<:tezca:1295145138955485275>"),
    app_commands.Choice(name="thea", value="<:thea:1295145147343962162>"),
    app_commands.Choice(name="redraptor", value="<:redraptor:1295145154251849748>"),
    app_commands.Choice(name="loki", value="<:loki:1295145162057580575>"),
    app_commands.Choice(name="seven", value="<:seven:1295145169716379763>"),
    app_commands.Choice(name="vivi", value="<:vivi:1295145176221745265>"),
    app_commands.Choice(name="imugi", value="<:imugi:1295145187903012884>"),
    app_commands.Choice(name="kingzuva", value="(i didnt add king zuva yet x crossy)")
]   
BRAWLHALLA_LEGENDS = [
    app_commands.Choice(name="Ada", value="ada"),
    app_commands.Choice(name="Arcadia", value="arcadia"),
    app_commands.Choice(name="Artemis", value="artemis"),
    app_commands.Choice(name="Asuri", value="asuri"),
    app_commands.Choice(name="Azoth", value="azoth"),
    app_commands.Choice(name="Barraza", value="barraza"),
    app_commands.Choice(name="Bodvar", value="bodvar"),
    app_commands.Choice(name="Brynn", value="brynn"),
    app_commands.Choice(name="Caspian", value="caspian"),
    app_commands.Choice(name="Cassidy", value="cassidy"),
    app_commands.Choice(name="Cross", value="cross"),
    app_commands.Choice(name="Diana", value="diana"),
    app_commands.Choice(name="Dusk", value="dusk"),
    app_commands.Choice(name="Ember", value="ember"),
    app_commands.Choice(name="Ezio", value="ezio"),
    app_commands.Choice(name="Fait", value="fait"),
    app_commands.Choice(name="Gnash", value="gnash"),
    app_commands.Choice(name="Hattori", value="hattori"),
    app_commands.Choice(name="Imugi", value="imugi"),
    app_commands.Choice(name="Isaiah", value="isaiah"),
    app_commands.Choice(name="Jaeyun", value="jaeyun"),
    app_commands.Choice(name="Jhala", value="jhala"),
    app_commands.Choice(name="Jiro", value="jiro"),
    app_commands.Choice(name="Kaya", value="kaya"),
    app_commands.Choice(name="King zuva", value="kingzuva"),
    app_commands.Choice(name="Koji", value="koji"),
    app_commands.Choice(name="Kor", value="kor"),
    app_commands.Choice(name="Linfei", value="linfei"),
    app_commands.Choice(name="Loki", value="loki"),
    app_commands.Choice(name="Lord Vraxx", value="lordvraxx"),
    app_commands.Choice(name="Lucien", value="lucien"),
    app_commands.Choice(name="Magyar", value="magyar"),
    app_commands.Choice(name="Mako", value="mako"),
    app_commands.Choice(name="Mirage", value="mirage"),
    app_commands.Choice(name="Mordex", value="mordex"),
    app_commands.Choice(name="Munin", value="munin"),
    app_commands.Choice(name="Queen Nai", value="queennai"),    
    app_commands.Choice(name="Nix", value="nix"),
    app_commands.Choice(name="Onyx", value="onyx"),
    app_commands.Choice(name="Orion", value="orion"),
    app_commands.Choice(name="Petra", value="petra"),
    app_commands.Choice(name="Queen Nai", value="queennai"),
    app_commands.Choice(name="Ragnir", value="ragnir"),
    app_commands.Choice(name="Random", value="random"),
    app_commands.Choice(name="Rayman", value="rayman"),
    app_commands.Choice(name="Redraptor", value="redraptor"),
    app_commands.Choice(name="Reno", value="reno"),
    app_commands.Choice(name="Sir Roland", value="sirroland"),
    app_commands.Choice(name="Scarlet", value="scarlet"),
    app_commands.Choice(name="Sentinel", value="sentinel"),
    app_commands.Choice(name="Seven", value="seven"),
    app_commands.Choice(name="Sidra", value="sidra"),
    app_commands.Choice(name="Sir Roland", value="sirroland"),
    app_commands.Choice(name="Teros", value="teros"),
    app_commands.Choice(name="Tezca", value="tezca"),
    app_commands.Choice(name="Thatch", value="thatch"),
    app_commands.Choice(name="Thea", value="thea"),
    app_commands.Choice(name="Thor", value="thor"),
    app_commands.Choice(name="Ulgrim", value="ulgrim"),
    app_commands.Choice(name="Val", value="val"),
    app_commands.Choice(name="Vector", value="vector"),
    app_commands.Choice(name="Vivi", value="vivi"),
    app_commands.Choice(name="Volkov", value="volkov"),
    app_commands.Choice(name="Lord Vraxx", value="lordvraxx"),
    app_commands.Choice(name="Wushang", value="wushang"),
    app_commands.Choice(name="Xull", value="xull"),
    app_commands.Choice(name="Yumiko", value="yumiko"),
    app_commands.Choice(name="Zariel", value="zariel"),
]
SORTING_METHOD_OPTIONS = [
    app_commands.Choice(name="Current Elo", value="current"),
    app_commands.Choice(name="Peak Elo", value="peak")]
FLAG_TYPE_OPTIONS = [
    app_commands.Choice(name="No Flags", value=FlagType.NONE.value),
    app_commands.Choice(name="Region / Server (Discord doesn't provide emojis for this option)", value=FlagType.REGION.value),
    app_commands.Choice(name="Country of Residence", value=FlagType.COUNTRY.value),
    app_commands.Choice(name="Ethnicity", value=FlagType.ETHNICITY.value),
]