import os
import discord
from dotenv import load_dotenv

load_dotenv()
SECRET = os.getenv('TDM_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():

    for guild in client.guilds:
        if guild == GUILD:
            break

    print(
        f'{client.user} has connected to the following servers:\n'
        f'{guild.name}(id: {guild.id})'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')




client.run(SECRET)