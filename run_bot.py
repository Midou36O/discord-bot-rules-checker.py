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
        if msg.content.startswith('experience'): # "experience" = 10 characters
          if msg.content[11:].startswith('creates'): # " creates" = 1 space (considered a character too) + 7 characters
            if msg.content[19:].startswith('insane'): # " insane" = 1 space + 6 characters
                if msg.content[26:].startswith('differences'): # " differences" 1 space + 11 characters
                    await msg.author.add_roles(discord.utils.get(msg.guild.roles, id=ROLE_ID))
                    await msg.delete()
        if msg.channel.id == CHANNEL_ID: #put your channel id here so the bot scans for messages here.
          w=['!verify','hi','gay', 'owo', 'hewwo'] #actually this is like the blacklist words, put them if ppl says the same thing
          p=[USER_ID_1, USER_ID_2] # Whitelist if you don't want to get your messages deleted (for example if you want to pin a welcome message)
          if msg.content.lower() in w or len(msg.content.split()) < 70 or len(msg.content) > 1000: #if the messages is lower than 4 words and higher than 1000, delete
              if msg.author.id not in p:
                  await msg.delete()
                  print('beep boop it worked')
    await bot.process_commands(msg)
bot.run('token here')
