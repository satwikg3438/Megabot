import discord
from discord.ext import commands
import random
from discord.ext.commands import has_permissions, MissingPermissions
import random
import datetime
import humanfriendly
import asyncio
import ffmpeg as ffmpeg

Token= 'OTgzMzM3NjkyNTM0Mjk2Njc2.GpvTXy.OeQY_n8PjXb9qnZoM2hidKmuYtie2_xTQib4Bk'

intents= discord.Intents.all()
Bot = commands.Bot(command_prefix="", intents=intents)
bot = Bot

@Bot.event
async def on_connect():
 print(f'connected to {Bot.user.name} successfully!!')


async def ch_pr():
  await Bot.wait_until_ready()
  statuses = ['Satwik G', f'on {len(Bot.guilds)} Server/s', 'Mad over there!!']
  while not Bot.is_closed():
    status= random.choice(statuses)
    await Bot.change_presence(activity=discord.Streaming(name=status, url='https://youtube.com/channel/UCnPnTLdfODNCa63r7jUQo3g'))
    await asyncio.sleep(20)

@Bot.command()
async def Help(ctx):
  Hmbedo= discord.Embed(title="Feature Command", description="1.Kick \n2.Ban \n3.Unban \n4.Mute \n5.Unmute \n6.Cnick \n7.Qtion \n8.Lockdown \n9.Unlock \n10.Clear \n11.Slowmode \n12.Ping", url="https://discord.com/oauth2/authorize?client_id=978890477023678495&permissions=8&scope=applications.commands%20bot", colour=discord.Colour.blue())
  Hmbedt= discord.Embed(title="Music Commands:", description="1.play \n2.pause \n3.resume \n4.connect/con \n5.disconnect \n6.queue \n7.volume \n8.seek \n9.loop", url="https://discord.com/oauth2/authorize?client_id=978890477023678495&permissions=8&scope=applications.commands%20bot", colour=discord.Colour.blue())
  Hmbedth=discord.Embed(title="Other commands", description="1.Hi \n2.Hello \n3.Rickroll \n4.Kiss \n5.Kill \n6.Hug \n7.Lick \n8.RPS \n9.Slap \n10.Hack \n11.Avatar", url="https://discord.com/oauth2/authorize?client_id=978890477023678495&permissions=8&scope=applications.commands%20bot", colour=discord.Colour.blue())
  Hmbedo.set_footer(text='Crystal')
  Hmbedo.set_thumbnail(url='https://images-ext-2.discordapp.net/external/Hm0ZvkHYChoVrnQahfW9KLRwFYqmyiUzxJla6jI7kek/%3Fsize%3D4096/https/cdn.discordapp.com/avatars/978890477023678495/e7faeb20b1d31fde9d4b2be10c7e09ae.png')
  Hmbedt.set_footer(text='Crystal')
  Hmbedt.set_thumbnail(url='https://images-ext-2.discordapp.net/external/Hm0ZvkHYChoVrnQahfW9KLRwFYqmyiUzxJla6jI7kek/%3Fsize%3D4096/https/cdn.discordapp.com/avatars/978890477023678495/e7faeb20b1d31fde9d4b2be10c7e09ae.png')
  Hmbedth.set_footer(text='Crystal')
  Hmbedth.set_thumbnail(url='https://images-ext-2.discordapp.net/external/Hm0ZvkHYChoVrnQahfW9KLRwFYqmyiUzxJla6jI7kek/%3Fsize%3D4096/https/cdn.discordapp.com/avatars/978890477023678495/e7faeb20b1d31fde9d4b2be10c7e09ae.png')
  await ctx.channel.send(embed=Hmbedo)
  await ctx.channel.send(embed=Hmbedt)
  await ctx.channel.send(embed=Hmbedth)


@Bot.command()
async def Owner(ctx):
 await ctx.send ("Smart Satwik")

@Bot.command()
async def Idot(ctx):
 await ctx.send ("Ha ha its you 🤣")



@Bot.command()
async def Rickroll(ctx):
  await ctx.channel.purge(limit=1)
  await asyncio.sleep(1)
  mdk=await ctx.send ("https://youtube.com/shorts/BUykFA7FCo4?feature=share @everyone this is a good video")
  await asyncio.sleep(30)
  await mdk.edit(content='It was a Rickroll video LOL')

@Bot.command()
async def Yomama(ctx):
 await ctx.send ("OBAMA")

@Bot.command()
async def GANAPATIBOPPA(ctx):
 await ctx.send ("MOORAYA")

@Bot.command()
async def Game(ctx):
 await ctx.send ("A good Game is Minecraft")

@Bot.command()
async def ABC123(ctx):
 await ctx.send ("HA!.. HA!")

@Bot.command()
async def People(ctx):
 await ctx.send ("I don't know anyone i'm a bot mannnn!")

@Bot.command()
async def Ping(ctx):
 await ctx.send (f'Pong,🏓 {round(Bot.latency*1000)}ms')



@Bot.command()
async def Fuck(ctx):
 await ctx.send ("Looks like its Smelly")

@Bot.command()
async def Fart(ctx):
 await ctx.send ("Poooooooooooooooooooooop I farted")

@Bot.command()
@has_permissions(kick_members=True)
async def Kick(ctx, member : discord.Member, *,reason=None):
 await member.kick(reason=reason)
 await ctx.send(f"{member.mention} was kicked")



@Bot.command()
@has_permissions(ban_members=True)
async def Ban(ctx, member : discord.Member, *,reason=None):
 await member.ban(reason=reason)
 await ctx.send(f"{member.mention} was Banned")



@Bot.command()
async def RPS(ctx):
 RPS=('Rock', 'Paper', 'Scissor')
 await ctx.channel.send(random.choice(RPS))


@Bot.command()
@has_permissions(manage_messages=True)
async def Mute(ctx, member : discord.Member):
  role = discord.utils.get(ctx.guild.roles, name="Muted")
  guild = ctx.guild
  if role not in guild.roles:
   perms = discord.permissions(send_messages=False, speak=False)
   await guild.create.role(name="Muted", permissions=perms)
   await member.add_roles(role)
   await ctx.send(f"{member.mention} was muted")
  else:
   await member.add_roles(role)
   await ctx.send(f"{member.mention} was muted")


@Bot.command()
@has_permissions(manage_messages=True)
async def Unmute(ctx, member : discord.Member):
  role = discord.utils.get(ctx.guild.roles, name="Muted")
  await member.remove_roles(role)
  await ctx.send(f"{member.mention} was unmuted")


@Bot.command()
@has_permissions(manage_channels=True)
async def Slowmode(ctx, seconds: int):
 await ctx.channel.edit(slowmode_delay=seconds)
 await ctx.send(f"Slowmode is mow set to {seconds}s in this channel")


@Bot.command(pass_content=True)
@has_permissions(kick_members=True)
async def Cnick(ctx, member : discord.Member, nick):
 await member.edit(nick=nick)
 await ctx.send(f"U changed his Nickname to {member.mention}")



@Bot.command()
async def Hi(ctx):
    messasge = await ctx.send(f"Hi {ctx.author.mention}")
    await messasge.add_reaction(emoji="😁")

@Bot.command()
async def Hello(ctx):
   massage = await ctx.send(f"Hi {ctx.author.mention}")
   await massage.add_reaction(emoji="😁")


@Bot.command()
async def Qtion(ctx, *, Question):
 emb=discord.Embed(title="QUESTION", description=f"{Question}")
 await ctx.channel.purge(limit=1)
 await asyncio.sleep(1)
 msg= await ctx.channel.send(embed=emb)
 await msg.add_reaction("👍")
 await msg.add_reaction("👎")
 await msg.add_reaction("🧐")

@Bot.command()
@has_permissions(manage_channels=True)
async def Lockdown(ctx):
 await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
 await ctx.send(ctx.channel.mention+"Is now in lockdown")


@Bot.command()
@has_permissions(manage_channels=True)
async def Unlock(ctx):
 await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
 await ctx.send(ctx.channel.mention+"Is now Unlocked")


@Bot.command()
@has_permissions(manage_messages=True)
async def Clear(ctx, amount=5):
   await ctx.channel.purge(limit=1)
   await ctx.channel.purge(limit=amount+1)
   await asyncio.sleep(1)
   await ctx.send(f"I've Deleted {amount} messages")
   await asyncio.sleep(3)
   await ctx.channel.purge(limit=1)
   print(f"Someone cleared {amount} messages")


@Bot.command()
async def Kill(ctx, *, Member:discord.Member):
  msg=await ctx.send(f"{ctx.author.mention} kills {Member.mention} \n https://images-ext-2.discordapp.net/external/4nztNvTnX0WDlvW0n71rLjgLbQt-yHY-kD4nrBoPB0I/https/cdn.weeb.sh/images/HyXTiyKw-.gif")
  await msg.add_reaction("👍")

@Bot.command()
async def Kiss(ctx, *, Member:discord.Member):
  msg=await ctx.send(f"{ctx.author.mention} Kissed {Member.mention} \n https://images-ext-2.discordapp.net/external/jqbMG7I5LT9a19e8ChkcmbGFLksP5Id8F0YP3yEcR8M/https/cdn.weeb.sh/images/SJSr3TOv-.gif")
  await msg.add_reaction("👍")
 
@Bot.command()
async def Hug(ctx, *, Member:discord.Member):
  msg=await ctx.send(f"{ctx.author.mention} Hugs{Member.mention} \n https://images-ext-2.discordapp.net/external/OGn7ixKlnChwTwxZ8LXEyqDAPBzEguYM5uDeMFSzY7Y/https/cdn.weeb.sh/images/ryCG-OatM.gif")
  await msg.add_reaction("👍")
  
@Bot.command()
async def Slap(ctx, *, Member:discord.Member):
  msg=await ctx.send(f"{ctx.author.mention} Slaps {Member.mention} \n https://images-ext-2.discordapp.net/external/xdNGuZzdnzDvLnp3xLYx1wAXpz67yHwklt7yV1KJAAk/https/cdn.weeb.sh/images/B1jk41KD-.gif")
  await msg.add_reaction("👍")
 
@Bot.command()
async def Lick(ctx, *, Member:discord.Member):
  msg=await ctx.send(f"{ctx.author.mention} Licks {Member.mention} eww!! \n https://images-ext-2.discordapp.net/external/NDTd_FWKJcHbDQ0LeuYWS871_m2pBTOaNWAD8ZX8VBQ/https/cdn.weeb.sh/images/S1QzRJp7z.gif")
  await msg.add_reaction("👍")

@Bot.command()
async def Hack(ctx, user:discord.Member):
 ediot=await ctx.send("Finding IP")
 await asyncio.sleep(2)
 await ediot.edit(content='IP = 192.236.234.2.3')
 await asyncio.sleep(2)
 await ediot.edit(content='Finding username..')
 await asyncio.sleep(2)
 await ediot.edit(content=f'{user.name}@gmailz.com')
 await asyncio.sleep(2)
 await ediot.edit(content=f'Using $heck {user.name}')
 await asyncio.sleep(2)
 await ediot.edit(content=f'Hecked {user.name} Successfully')
 await asyncio.sleep(2)
 await ediot.edit(content='Selling data on Darkweb')
 await asyncio.sleep(2)
 await ediot.edit(content=f'Hacking {user.name}s bank account')
 await asyncio.sleep(2)
 await ediot.edit(content=f'Giving all the money to {ctx.author.name}')
 await asyncio.sleep(2)
 await ediot.edit(content=f'The 100% real and dangerous hacking was completed on {user.name} secretly')
 await asyncio.sleep(5)
 await ctx.channel.purge(limit=2)

@Bot.command()
async def Unban(ctx, *, member):
	banned_users = await ctx.guild.bans()
	
	member_name, member_discriminator = member.split('#')
	for ban_entry in banned_users:
		user = ban_entry.user
		
		if (user.name, user.discriminator) == (member_name, member_discriminator):
 			await ctx.guild.unban(user)
 			await ctx.channel.send(f"Unbanned {user.name}")

@Bot.command()
async def Avatar(ctx, member: discord.Member=None):
    if member == None:
        member = ctx.author
    
    icon_url = member.avatar_url 
 
    avatarEmbed = discord.Embed(title = f"{member.name}\'s Avatar", color = 0xFF0000)
 
    avatarEmbed.set_image(url = f"{icon_url}")
 
    avatarEmbed.timestamp = ctx.message.created_at 
 
    await ctx.send(embed = avatarEmbed)


Bot.lavalink_nodes = [
    {"host": "lava.link", "port": 80, "password": "Satwikisagoodboyrightquestionmark"},
]
Bot.spotify_credentials = {
    'client_id': '155edd70cac34557bd097748c9d959a7',
    'client_secret': 'a34b37a4f9464a56ac7cd5bd4750966f'
}

Bot.load_extension('dismusic')
Bot. remove_command('help')
Bot.loop.create_task(ch_pr())

Bot.run(Token)
