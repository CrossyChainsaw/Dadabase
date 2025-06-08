# Purpose
# This test checks if the following variables are being added to the account_linkers list in the json data
# - brawlhalla_id
# - brawlhalla_name
# - clan_index

import random
import pytest
from Dadabase.commands.add_account_linker import add_account_linker
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
async def test_add_account_linker_integration():
    # Arrange
    mock_interaction = MockInteraction(guild_id=1)
    mock_brawlhalla_id = 1
    mock_brawlhalla_name = "TEST_LINK"
    mock_clan_index = 0

    # Action
    await add_account_linker(mock_interaction, mock_brawlhalla_id, mock_brawlhalla_name, mock_clan_index)

    # Assert
    clan_data = read_data(CLANS_DATA_PATH, mock_interaction.guild.id)
    found = False
    for linker in clan_data.get("account_linkers", []):
        if (
            linker.get("brawlhalla_id") == mock_brawlhalla_id and
            linker.get("brawlhalla_name") == mock_brawlhalla_name and
            linker.get("clan_index") == mock_clan_index
        ):
            found = True
            break

    assert found, f"Linker with id {mock_brawlhalla_id} and name {mock_brawlhalla_name} was not added"
