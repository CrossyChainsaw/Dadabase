import os
import discord
from discord.ext import commands
from modules.claim import claim

intents = discord.Intents().all()
bot = commands.Bot(command_prefix=['d!'], intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command(name='say')
async def say(ctx):
  await ctx.channel.send("hello")

@bot.command(name='claim')
async def claim_command(ctx, brawlhalla_id):
  await claim(ctx, brawlhalla_id)

  

bot.run(os.environ['BOT_KEY'])



