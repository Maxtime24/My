import discord

client = discord.Client

@client.event
async def On_ready():
    print(client.user.id)
    print("Ready")

@client.event
async def on_message(message):
    if message.content.startswith("안녕"):
        await message.channel.send("안녕하세요!")

client.run("NjkzMDkyNzI3ODc3MDA5NDc4.XoBLMA.vDqmB1I0YhIfwyyPa24jITfPGM8")