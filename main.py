import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
intents = discord.Intents.default()
intents.members = True
load_dotenv(dotenv_path="config")


class Ayrobot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=(os.getenv("prefix")), description=f"{os.getenv('prefix')}haylp pour de l'aide")

    async def on_ready(self):
        print(f"{self.user.display_name} is connected !")

#Création de l'instance aybot
aybot = Ayrobot()
aybot.run(os.getenv("token"))

