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
    # Evita que el bot responda a sus propios mensajes
    if message.author.id == bot.user.id:
        return
    
    # Responde a TODOS los mensajes (usuarios y bots)
    respuesta = "@everyone\nhttps://www.roblox.com/share?code=7c1aaa90013002498dfbeaf12e72651d&type=Server"
    
    await message.channel.send(respuesta)

bot.run(os.getenv("DISCORD_TOKEN"))
