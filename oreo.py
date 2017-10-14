
# coding: utf-8

# In[1]:


get_ipython().magic(u'reset')


# In[11]:


# Basic imports
import discord
from discord.ext import commands
import asyncio
import json


# In[12]:


# Load configuration
with open('./config.json', 'r') as config_file:
    config = json.load(config_file)


# In[ ]:


import discord
from discord.ext import commands
import random

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''
bot = commands.Bot(command_prefix = config['prefix'], description = description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def add(left : int, right : int):
    """Adds two numbers together."""
    await bot.say(left + right)

@bot.command()
async def roll(dice : str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await bot.say('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await bot.say(result)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(*choices : str):
    """Chooses between multiple choices."""
    await bot.say(random.choice(choices))

@bot.command()
async def repeat(times : int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await bot.say(content)

@bot.command()
async def joined(member : discord.Member):
    """Says when a member joined."""
    await bot.say('{0.name} joined in {0.joined_at}'.format(member))

@bot.group(pass_context=True)
async def cool(ctx):
    """Says if a user is cool.

    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await bot.say('No, {0.subcommand_passed} is not cool'.format(ctx))

@cool.command(name='bot')
async def _bot():
    """Is the bot cool?"""
    await bot.say('Yes, the bot is cool.')

bot.run(config['token'])


# In[15]:


import discord
import asyncio
client = discord.Client()
@client.event
async def on_read():
    print("Logged in as {}, {}".format(client.user.name, client.user.id))

@client.event
async def on_message(message):
    tmp = await client.send_message(message.channel, "abc")
    word = "right?"
    await client.edit_message(tmp, 'something here {}'.format(word))
    


# In[16]:


# client.run(config['token'])


# In[10]:


import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')

#client.run(config['token'])


# In[11]:


client.close()


# In[2]:


# import logging# logger = logging.getLo('aeb')
# hdlr = logging.FileHandler('aeb.log')
# formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
# hdlr.setFormatter(formatter)
# if len(logger.handlers) == 0:
#     logger.addHandler(hdlr)
# print len(logger.handlers):
#     logger.setLevel(logging.DEBUG)

