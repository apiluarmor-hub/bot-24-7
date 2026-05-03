import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'✅ Bot {bot.user} está online!')

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content.lower() == "!roblox":
        await message.channel.send("https://www.roblox.com/share?code=7c1aaa90013002498dfbeaf12e72651d&type=Server")

# ✅ CORREGIDO
bot.run(os.getenv("DISCORD_TOKEN"))
