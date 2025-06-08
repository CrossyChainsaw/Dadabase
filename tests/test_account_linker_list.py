import pytest
from Dadabase.commands.add_account_linker import add_account_linker
from Dadabase.commands.account_linker_list import account_linker_list
from Dadabase.modules.data_management import read_data, CLANS_DATA_PATH

class MockGuild:
    def __init__(self, id):
        self.id = id

class MockResponse:
    def __init__(self):
        self.sent_embed = None

    async def send_message(self, *, embed=None, content=None):
        self.sent_embed = embed

class MockInteraction:
    def __init__(self, guild_id):
        self.guild = MockGuild(guild_id)
        self.response = MockResponse()

@pytest.mark.asyncio
async def test_account_linker_list_includes_expected_fields():
    # Arrange: create and add a test account linker
    mock_interaction = MockInteraction(guild_id=2)
    mock_brawlhalla_id = 2
    mock_brawlhalla_name = "TEST_PLAYER"
    mock_clan_index = 0

    # Act: run the list command
    await account_linker_list(mock_interaction)

    # Assert: check the message sent in the embed
    embed = mock_interaction.response.sent_embed
    assert embed is not None, "No embed was sent."

    desc = embed.description
    assert "clan_index" in desc, '"clan_index" label not found in embed description'
    assert str(mock_clan_index) in desc, "clan_index value not found in embed"
    assert "id" in desc, '"brawlhalla_id" label not found in embed description'
    assert str(mock_brawlhalla_id) in desc, "brawlhalla_id value not found in embed"
    assert "name" in desc, '"brawlhalla_id" label not found in embed description'
    assert mock_brawlhalla_name in desc, "brawlhalla_name not found in embed"


