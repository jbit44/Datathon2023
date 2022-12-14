import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import toxicity

BOT_NAME = "Datathon23Bot"

load_dotenv()

DISCORD_TOKEN = ""
with open("discordtoken.txt", 'r') as file:
    DISCORD_TOKEN = file.read()

intents = discord.Intents(messages=True, message_content=True)
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has logged in.')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if toxicity.isToxic(message.content):
        await message.delete()

if __name__ == '__main__':
    bot.run(DISCORD_TOKEN)
