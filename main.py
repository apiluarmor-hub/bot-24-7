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
    if message.author.bot and message.author.id != bot.user.id:  # Responde a otros bots
        respuesta = "@everyone\nhttps://www.roblox.com/share?code=7c1aaa90013002498dfbeaf12e72651d&type=Server"
        await message.channel.send(respuesta)
    
    # Para que también responda si un usuario escribe (opcional)
    # elif not message.author.bot:
    #     await message.channel.send("@everyone\nhttps://www.roblox.com/share?code=7c1aaa90013002498dfbeaf12e72651d&type=Server")

bot.run(os.getenv("DISCORD_TOKEN"))
