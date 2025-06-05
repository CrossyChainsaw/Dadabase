import discord
from discord import app_commands

CROSSY_ID = 413070742591373314
def is_admin_or_crossy():
    async def predicate(interaction: discord.Interaction) -> bool:
        if interaction.user.id == CROSSY_ID:
            return True
        return interaction.user.guild_permissions.administrator
    return app_commands.check(predicate)