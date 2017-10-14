
# coding: utf-8

# In[9]:


get_ipython().magic(u'reset')


# In[2]:


# Basic imports
import discord
from discord.ext import commands
import asyncio
import json


# In[4]:


# Load configuration
with open('./config.json', 'r') as config_file:
    config = json.load(config_file)


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

