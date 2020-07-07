
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
        if msg.content.startswith('cactus'): # Here we look if the message starts with a specific word, like a prefix
          if msg.content[7:].startswith('explodes'): # 8 is the amount of characters in the first word. If you want to add a space between the two words, remember to add the space in the number too
            if msg.content[16:].startswith('baloons'): # for 7, it's the same thing as second word
              await msg.author.add_roles(discord.utils.get(msg.guild.roles, id=680422513121034310)) # add_roles is the call function for adding roles, of course, however we don't have any role object specified, so we make it on the fly by using this cool function that will search for something from a parameter of the wanted object. I recommend to use the ID because it never changes, however you can use name='name' too if you want. I think that other parameters such as 'color' work too, but I never tried, and the docs are shitty on explaining extra stuff
    await bot.process_commands(msg) # This is a call that you have to use because if on_message is called, bot will ignore every command unless you use this call that makes the bot check if the message was actually a command or not

bot.run(token)


