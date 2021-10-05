from discord.ext import commands
import discord
import sys

class Generales(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        activity = discord.Game(name=r"%aide pour avoir l'aide", type=3)
        await self.client.change_presence(status=discord.Status.online, activity=activity)
        
def setup(client):
    client.add_cog(Generales(client))