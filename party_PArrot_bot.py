# bot.py
import os

import discord

TOKEN = "ODI1ODA3NzE2MTI3NjA0NzM2.YGDTXg.EaXG9CY34LLIOf_ZoeFKb2gDdHs"

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    print(client.user)
    strings = {"!party", "!p"}
    print(message.content)
    msg = message.content.lower()
    for s in strings:
        if s in msg:
            await do_the_thing(message)
            return


async def do_the_thing(message):
    script_dir = os.path.dirname(__file__)
    rel_path = r"partyparrotemoji.gif"
    abs_file_path = os.path.join(script_dir, rel_path)
    await message.channel.send(file=discord.File(abs_file_path))
    return


try:
    token = "ODI1ODA3NzE2MTI3NjA0NzM2.YGDTXg.EaXG9CY34LLIOf_ZoeFKb2gDdHs"
    client.run(token)
except OSError:
    print("Error: Token could not be accessed")
    exit(1)