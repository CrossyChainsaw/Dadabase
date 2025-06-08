import pytest
from Dadabase.commands.remove_console_player import remove_console_player
from Dadabase.modules.data_management import CLANS_DATA_PATH, read_data

class MockGuild:
    def __init__(self, id):
        self.id = id

class MockResponse:
    def __init__(self):
        self.message_sent = None

    async def send_message(self, message):
        self.message_sent = message

class MockInteraction:
    def __init__(self, guild_id):
        self.guild = MockGuild(guild_id)
        self.response = MockResponse()

@pytest.mark.asyncio
async def test_remove_console_player_integration():
    # Arrange - this should match the user added in your add_console_player test
    mock_interaction = MockInteraction(guild_id=1)
    mock_brawlhalla_id = 1
    mock_brawlhalla_name = "TEST_PLAYER"
    mock_clan_index = 0

    # Action - call remove_console_player (assuming signature is similar)
    await remove_console_player(mock_interaction, mock_brawlhalla_id)

    # Assert - check that the user with that brawlhalla_id no longer exists
    clan_data = read_data(CLANS_DATA_PATH, mock_interaction.guild.id)
    found = False
    for player in clan_data.get("console_players", []):
        if (
            player.get("brawlhalla_id") == mock_brawlhalla_id or
            player.get("brawlhalla_name") == mock_brawlhalla_name or
            player.get("clan_index") == mock_clan_index
        ):
            found = True
            break


    assert not found, f"Player with id {mock_brawlhalla_id} was not removed"
