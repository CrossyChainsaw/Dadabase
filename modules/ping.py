import random

async def ping(ctx):
  num = random.randrange(0, 8192)
  if num == 1:
    msg = ("ping en pong spelen ping pong, ping zei de ping pong bal. Ping die zei dat pong het deed maar pong die zei hou je kk bek")
  else:
    msg = ('pong')
  await ctx.channel.send(msg)

  
  