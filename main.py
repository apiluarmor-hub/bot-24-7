import discord
import os
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'✅ {bot.user} está conectado 24/7 en Railway!')

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    if bot.user.mentioned_in(message):
        await message.channel.send("@everyone\nhttps://www.roblox.com/share?code=7c1aaa90013002498dfbeaf12e72651d&type=Server")

bot.run(os.getenv("TOKEN"))
