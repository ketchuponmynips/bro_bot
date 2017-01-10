#resources https://tutorials.botsfloor.com/creating-chatbots-for-discord-90407e1bf382#.60umxs7et
#https://www.youtube.com/watch?v=ohgOjYv-3-k#

import discord
from discord.ext.commands import Bot

import secrets

bro_bot = Bot(command_prefix="!")

@bro_bot.event

#can run multiple of these in a loop
#on_read lets read channel
async def on_read():
    print("Client logged in")


@bro_bot.command()
async def hello(*args):
    return await bro_bot.say("hello_world")

@bro_bot.command()
async def python_help(*args):
    print(args)
    return await bro_bot.say("Looking that up!")

bro_bot.run(secrets.BOT_TOKEN)
