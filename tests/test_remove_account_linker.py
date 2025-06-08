# Purpose
# This test verifies that remove_account_linker properly removes the player
# from the account_linkers list in the json data.

import random
import pytest
from Dadabase.commands.remove_account_linker import remove_account_linker
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
async def test_remove_account_linker_integration(tmp_path):
    # Arrange - add first
    mock_interaction = MockInteraction(guild_id=1)
    mock_brawlhalla_id = 1
    mock_brawlhalla_name = "TEST_LINK"
    mock_clan_index = 0
    
    # Act - remove the linker
    await remove_account_linker(mock_interaction, mock_brawlhalla_id)

    # Assert - ensure it's gone
    updated_data = read_data(CLANS_DATA_PATH, mock_interaction.guild.id)
    assert not any(
        linker.get("brawlhalla_id") == mock_brawlhalla_id or
        linker.get("brawlhalla_name") == mock_brawlhalla_name or
        linker.get("clan_index") == mock_clan_index
        for linker in updated_data.get("account_linkers", [])
    ), f"Linker with id {mock_brawlhalla_id} was not removed"
