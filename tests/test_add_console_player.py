# Purpose
# This test checks if the following variables are being added to the console_players list in the json data
# - brawlhalla_id
# - brawlhalla_name
# - clan_index

import os
import json
import random
import pytest
from Dadabase.commands.add_console_player import add_console_player
from Dadabase.modules.data_management import CLANS_DATA_PATH, read_data
from Dadabase.classes.BrawlhallaAccount import BrawlhallaAccount

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
async def test_add_console_player_integration(tmp_path):
    # Arrange
    mock_interaction = MockInteraction(guild_id=1)
    mock_brawlhalla_id = 1
    mock_brawlhalla_name = "TEST_PLAYER"
    mock_clan_index = 0

    # Action
    await add_console_player(mock_interaction, mock_brawlhalla_id, mock_brawlhalla_name, mock_clan_index)

    # Assert
    clan_data = read_data(CLANS_DATA_PATH, mock_interaction.guild.id)
    found = False
    for player in clan_data.get("console_players", []):
        if (
            player.get("brawlhalla_id") == mock_brawlhalla_id and
            player.get("brawlhalla_name") == mock_brawlhalla_name and
            player.get("clan_index") == mock_clan_index
        ):
            found = True
            break

    assert found, f"Player with id {mock_brawlhalla_id} and name {mock_brawlhalla_name} was not added"
