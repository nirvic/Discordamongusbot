from itertools import cycle
import random
import os
import time
import aiohttp
import asyncio
from aiohttp import web
import discord #python3 -m pip install -U discord.py[voice]
from discord.ext.commands import check
from discord.ext import commands, tasks
from discord import voice_client
from discord import Role
from discord import Guild
from config import *

client = commands.Bot(command_prefix = '.')
status = cycle(['Status 1', 'Status 2'])

#Among us values
dead_members = []
dead_color = ['red','blue']


#Color alias

#When bot connects to server.
@client.event
async def on_ready():
    
    print('Umbra is present.')

#When member joins the server.
@client.event
async def on_member_join(member):
    print(f'{member} has joined the server.')

#When member leaves the server.
@client.event
async def on_member_remove(member):
    print(f'{member} has left the server.')

#After error is triggered
#@client.event
#async def on_command_error(ctx, error):
#    if isinstance(error, commands.CommandNotFound):
#        await ctx.send('Command not found.')


#Ping command
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong. {client.latency * 1000}ms')

#8ball command
@client.command(aliases=['8ball'])
async def _8ball(ctx, *,question):
    responses = ['Yes',
                 'No']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

#Clear x number of messages from channel
@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=5):    
        await ctx.channel.purge(limit= amount+1)
@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('Sorry you are not allowed to use this command.')

#Mute all members in channel
@client.command()
async def mute(ctx):
    global dead_members

    for member in list(client.get_channel(755960738987901018).members):
        if member.id in dead_members:
            await member.edit(mute=False, deafen=False)
        else:
            await member.edit(mute=False, deafen=True)

#Unmute all members in channel
@client.command()
async def unmute(ctx):
    global dead_members

    for member in list(client.get_channel(755960738987901018).members):
        if member.id in dead_members:
            await member.edit(mute=True, deafen=False)
        else:
            await member.edit(mute=False, deafen=False)                

#Revive dead members
@client.command()
async def revive(ctx):
    global dead_members
    dead_members = []
    for member in list(client.get_channel(755960738987901018).members):
        await member.edit(mute=False, deafen=False)
    await ctx.send('Dead players have been revived.')

#Add member to dead members
@client.command()
async def kill(ctx, *members: discord.Member):
    global dead_members
    
    for member in members:
        if  member.id not in dead_members:
            dead_members.append(member.id)
            print(dead_members)

#Spaghetty for now
#@client.command()
#async def color(ctx):

    #def color_switch(player_color):
    #    switcher={'red':'#a70000','blue':'#000c96','brown':'#552c09','green':'#117400','gray':'#242424','lime':'#66d36b','orange':'#f59200','pink':'#cc00a3','white':'#ffffff','purple':'#4f008a','teal':'#00ffb3','yellow':'#f1d900'}
    #    switcher.get(player_color, 'Uhhhh,neradi')

    #if member in list(client.get_channel(755960738987901018).members):
    #    print(member.color)
        #if member.color == color_switch(player_color):
        #    member.id.append(dead_members)



#Check dead members list
@client.command()
async def shded(ctx):
    await ctx.send(f'{dead_members}')

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

#Handle requests
@client.command
async def handle_request(request):
    action = request.match_info.get('action', "nothing")
    if action == "mute":
        await mute(None)
    elif action == "unmute":
        await unmute(None)
    elif action == "revive":
        await revive(None)

    return web.Response(text=None)
    
@client.command()
async def run_bot():
    app = web.Application()
    app.router.add_get('/', handle_request)
    app.router.add_get('/{action}', handle_request)

    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '', port)
    await site.start()

    try:
        await client.start(bot_token)

    except KeyboardInterrupt:
        client.close(),

    finally:
        await runner.cleanup()

try:
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run_bot())

except OSError:
    print("[*] ERROR: address already in use")

except Exception as e:
    print(f"{e}\n\n[*] ERROR: invalid discord bot token\n")

except KeyboardInterrupt:
    print("\n[*] Exiting..")

#@tasks.loop(minutes=5)
#async def change_status():
#    await client.change_presence(activity=discord.Game(next(status)))


#for filename in os.listdir('./cogs'):
#    if filename.endswith('.py'):
#        client.load_extension(f'cogs.{filename[:-3]}')    


#client.run(bot_token)