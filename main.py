import os
import discord
from discord.ext import commands
from modules.claim import claim
from modules.check import check
from modules.ping import ping
from modules.keep_alive import keep_alive

intents = discord.Intents().all()
bot = commands.Bot(command_prefix=['d!'], intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command(name='ping')
async def say(ctx):
  await ping(ctx)
  
@bot.command(name='claim')
async def claim_command(ctx, brawlhalla_id):
  await claim(ctx, brawlhalla_id)

@bot.command(name='check')
async def check_command(ctx):
  await check(ctx)

@claim_command.error
async def claim_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('format your message like the following\n`'+bot.command_prefix[0]+'claim brawlhalla_id`')

  
keep_alive()
bot.run(os.environ['BOT_KEY'])



