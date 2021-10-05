from discord.ext import commands
from dotenv import load_dotenv
import discord
import os

load_dotenv(dotenv_path=".env")


class Generales(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def clear(self, ctx, nbr_msgs: int):
        msg = await ctx.channel.history(limit=nbr_msgs+1).flatten()
        for each_msg in msg:
            await each_msg.delete()



def setup(client):
    client.add_cog(Generales(client))