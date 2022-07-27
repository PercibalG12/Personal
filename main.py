import discord 
import os
from dotenv import load_dotenv

client = discord.Client()
load_dotenv()
TOKEN = os.getenv('TOKEN')

@client.event
async def on_connect():
 print("Bot is active{0.user}".format(client))
 channel = client.get_channel(1000213971745390608)
 await channel.send("I'M ALIVEEE!")
 

@client.event
async def on_member_join(member):
 await member.create_dm()
 await member.dm_channel.send(f"Welcome to the server {member}!" )

 

client.run(TOKEN)  
