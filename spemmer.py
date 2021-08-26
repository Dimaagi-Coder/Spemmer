#use python discordbot.py to run (in terminal)
import discord
from discord.ext import commands
import asyncio

client = commands.Bot(command_prefix=".")

@client.event
async def on_ready():
    print("me be ready")
    

@client.command()
async def ping(ctx, time:int ,member:discord.Member):
    for i in range(time):
        await ctx.send(member.mention)

client.run("ODgwMDU4OTkyNDY0OTE2NTQx.YSYwzg.ouAoT5kjT8ebb3zqUgHEhPjK9Uo")