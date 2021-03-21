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

    # print(
    #     f'{client.user} has connected to the following servers:\n'
    #     f'{guild.name}(id: {guild.id})'
    # )

    # members = '\n - '.join([member.name for member in guild.members])
    # print(f'Guild Members:\n - {members}')


    game = discord.Game("with the API")
    await client.change_presence(activity=game)

    channelName = 123
    for guild in client.guilds:
        if guild == GUILD:
         break




    for channel in guild.channels:
        print(f'{channel}')
        if channel.name == "general":
            print(f'{channel}\n')
            channelName = channel.id
            print(f'{channelName}\n')
            break





@client.event
async def on_message(message):

    if message.channel.id == 773595120369008650:
        print(f'{message.author}')
        print(f'{message.content}')

    channel = client.get_channel(773595120369008650)
    printMessage = input()
    await channel.send(printMessage)
    



client.run(SECRET)