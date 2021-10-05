from discord.ext import commands
from dotenv import load_dotenv
import discord
import sys
import os
import asyncio
import random

class generales(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    def restart_bot(self):
        os.execv(sys.executable, ['python'] + sys.argv)

    @commands.command()
    async def reboot(self, ctx):
        if ctx.author.id in [652889258343792661, 265254730773692416]:
            await ctx.send("Redémarrage en cours...")
            await asyncio.sleep((random.randint(2, 12)/10))
            await ctx.send("Redémarrage terminé !")
            self.restart_bot()
        else:
            await ctx.send("Vous n'avez pas la permission !")
        
def setup(client):
    client.add_cog(generales(client))