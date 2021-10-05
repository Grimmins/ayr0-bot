from discord.ext import commands
from dotenv import load_dotenv
import discord
import sys

class generales(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def stop(self, ctx):
        if ctx.author.id in [652889258343792661, 265254730773692416]:
            sys.exit()
        else:
            await ctx.send("Vous n'avez pas la perm")
        
def setup(client):
    client.add_cog(generales(client))