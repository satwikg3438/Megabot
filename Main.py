import discord
import webserver
import random
from webserver import keep_alive

TOKEN = "OTYzNzA2ODMwMDQxNzg0MzYx.YlZ_7Q.6e5M4LHTYYN5A8bWB_so00pHWQw"

client = discord.Client()

client.change_presence(activity=discord.Game(name="SATWIK"))

@client.event
async def on_ready():
    print("{0.user} is now online mann!".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('Hi'):
        await message.channel.send('Hi')

        if message.content.startswith('bye'):
     await message.channel.send ('byebye')

        if message.conts in(.startswith('Who is intelligent'):
        await message.channel.send('SATWIK')

        if message.content.startswith('__help'):
        await message.channel.send('no help from me understand!!!!!?')

        if message.content.startswith('spam'):
        await message.channel.send('nooo! @everyone this fellow wants to spam messages')

        if message.content.startswith('Idot'):
        await message.channel.send('dont use such words')

   if message.content.startswith('Mega bot'):
        await message.channel.send('Yes plzzz')

 if message.content.startswith('Owner'):
        await message.channel.send('Satwik')

if message.content.startswith('How are you working mega bot?'):
        await message.channel.send('by replit and uptimerobot')
        
if message.content.startswith('GANAPATHI BOPPA'):
        await message.channel.send('MOORAYA')
        
if message.content.startswith('Nuke bot link'):
        await message.channel.send('https://discord.com/oauth2/authorize?client_id=963354634892746752&scope=applications.commands%20bot&permissions=8')

if message.content.startswith('Ping'):
     await message.channel.send('Pong 1ms')
     
if message.content.startswith('Am I good'):
    await message.channel.send('probably')
    
if message.content.startswith('Are you coded'):
    await message.channel.send('yesssss')
    
    if message.content.startswith('Give me admin'):
    await message.channel.send('No!')
    
if message.content.startswith('SHAKALAKA BOOB BOOM'):
    await message.channel.send('BOOM-BOOM-BOOM')
    
if message.content.startswith('Satwik is bad'):
    await message.channel.send('You are bad not satwik')

keep_alive()

client.run(TOKEN)
