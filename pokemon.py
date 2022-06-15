import discord
import os

from discord.ext import commands, tasks
from server.keep_alive import keep_alive

client = commands.Bot(command_prefix="P!")
TOKEN = os.environ['TOKEN']

for filename in os.listdir('./Events'):
  if filename.endswith('.py'):
    client.load_extension(f'Events.{filename[:-3]}')
    
  else:
    print(f'Unable to load {filename[:-3]}')

keep_alive()
client.run(TOKEN)