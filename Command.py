#importing the discord and commands packages
import discord
from discord.ext import commands
#initialising the bot with a prefix
client=commands.Bot(command_prefix='put a prefix here')

#making a command

@client.command(name="ping")
async def ping(ctx):
    await ctx.message.channel.send('pong')

"""Sends 'pong' when the ping command is invoked"""

#running the bot
client.run('insert token code here')

"""Token code can be recieved from https://discord.com/developers/applications
Go to your bot user and under the 'bot' tab you will find
A token code that is hidden and can he revealed
DO NOT REVEAL YOUR TOKEN CODE TO ANYONE ELSE
"""
