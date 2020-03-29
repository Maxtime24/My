import discord
import os

client = discord.Client

@client.event
async def On_ready():
    print(client.user.id)
    print("Ready")

@client.event
async def on_message(message):
    if message.content.startswith("안녕"):
        await message.channel.send("안녕하세요!")

        
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
