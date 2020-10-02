# First of all we import the discord.py library and the library for the bot framework
import discord
from discord.ext import commands
bot = commands.Bot(command_prefix='') # Here we replace the standard usage of "client" with "bot", which is an enhanced client, to say it very short
bot.remove_command('help') # Here we disable the default help command
# We use on_message event that checks for every message sent
@bot.event
async def on_message(msg): # msg is the message
    if msg.author == bot.user: # Here we make sure that the bot doesn't check his own messages
        return
    else:
        if msg.content.startswith('knowledge'):
          if msg.content[10:].startswith('enhances'):
            if msg.content[19:].startswith('power'):
                if msg.content[25:].startswith('lol'):
                    await msg.author.add_roles(discord.utils.get(msg.guild.roles, id=680422513121034310))
                    await msg.delete()
        if msg.channel.id == 730161129992618043:
          w=['!verify','hi','gay', 'owo', 'hewwo'] #actually this is like the blacklist words, put them if ppl says the same thing
          p=[365154614594502657, 649986611668451338, 550001691492089856, 306512687817555978, 421706224388800512, 471785433232179210, 209701282028453888, 213634643327582208, 600874061316489226, 257196097494188032, 333942090079797250, 436111437698433024, 602470901610446858, 708633835243569204, 262613435131363332,] # don't put the ' ' between the ID, put it as a normal number
          if msg.content.lower() in w or len(msg.content.split()) < 70 or len(msg.content) > 1000: #if the messages is lower than 4 words and higher than 1000, delete
              if msg.author.id not in p:
                  await msg.delete()
                  print('beep boop it worked')
    await bot.process_commands(msg)
bot.run('NzU3OTY2NjkzODUwMDIxOTc5.X2oFfg.5OXUguZLAodkxVymnNfYIjjyhyM')
#a
