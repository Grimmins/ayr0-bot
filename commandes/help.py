from discord.ext import commands
import discord

class generales(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def aide(self, ctx):
        print("t")
        
def setup(client):
    client.add_cog(generales(client))