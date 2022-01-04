import discord
import random
import asyncio
from discord.ext import commands

token = "NzAwMDcxNTE2OTM0NjM1NTcw.Xtkmow.SBWfvwzY8coBfxxZ_8sD7r0RT4g"
client = commands.Bot(command_prefix="/")

@client.event
async def on_ready():
    print("Logged in")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    await client.process_commands(message)
class Player:
    def __init__(self, name: discord.user, role=None):
        self.name = name
        self.role = role
    def __eq__(self, other):
        return self.name == other.name
    def __repr__(self):
        return self.name.mention