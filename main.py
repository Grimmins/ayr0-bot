from discord.ext.commands import has_permissions, CheckFailure
from discord.ext import commands,tasks
from dotenv import load_dotenv
import discord
import sys
import os
load_dotenv(dotenv_path=".env")

intents = discord.Intents().all()
client = commands.Bot(command_prefix=os.getenv("prefix"), intents=intents)
client.remove_command('help')

for fichier in os.listdir("./commandes"):
    if fichier.endswith(".py"):
        client.load_extension(f"commandes.{fichier[:-3]}")

client.run(os.getenv("token"))