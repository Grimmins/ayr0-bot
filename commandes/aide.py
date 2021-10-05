from discord.ext import commands
from dotenv import load_dotenv
import discord
import os

load_dotenv(dotenv_path=".env")


class Generales(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def aide(self, ctx):
        prefix = os.getenv("prefix")
        help = f"""
**COMMANDES GENERAL : **
{prefix}aide ==> affiche l'aide
**COMMANDES ADMIN : **
{prefix}clear ==> clear le nombre de messages demandé
**COMMANDES OWNER : **
{prefix}reboot ==> reboot le bot
        """
        embedVar = discord.Embed(title="AIDE : ", description=help, color=0x00ff00)
        await ctx.send(embed=embedVar)


def setup(client):
    client.add_cog(Generales(client))
