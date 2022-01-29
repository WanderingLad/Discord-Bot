'''
---------------------------------------------------------------------------
Fun bot I made to DM your friends in a server
Uses KVP and discord.py
Only one instance can be run at once
Contact: Prei#6785 jreilly2112@gmail.com
---------------------------------------------------------------------------
'''
from discord.ext import commands
from discord import Message
import random 
import discord

TOKEN = 'nottherealtoken'

GUILD = "Test Server"

intents = discord.Intents(messages=True, guilds=True, members=True)

bot = discord.Client(intents=intents)

bot = commands.Bot(command_prefix="#")

#This sets a  list of comamnds that allows you to make a bot join a voice channel
#This also gives it a chance to play an .mp3 from your computer
@bot.command()
async def join(ctx):
    if(ctx.message.author.id == 232629621038776331 and not ctx.voice_client):
        channel = ctx.author.voice.channel
        await channel.connect()
    
@bot.command()
async def leave(ctx):
    if(ctx.message.author.id == 232629621038776331 and ctx.voice_client):
        server = ctx.message.guild.voice_client
        await server.disconnect()

@bot.command()
async def play(ctx):
    if(ctx.message.author.id == 232629621038776331 and ctx.voice_client):
        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(bot.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio('Music\\oh_hey_alex.mp3')
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)

@bot.command()
async def pause(ctx):
    if(ctx.message.author.id == 232629621038776331 and ctx.voice_client):
        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(bot.voice_clients, guild=guild)
        if voice_client.is_playing():
            voice_client.pause()

@bot.command()
async def resume(ctx):
    if(ctx.message.author.id == 232629621038776331 and ctx.voice_client):
        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(bot.voice_clients, guild=guild)
        if voice_client.is_paused():
            voice_client.resume()

#This sends a message to a user specified by their numeric ID
Message Sending
@bot.event
async def on_ready():
    for guild in bot.guilds:
        print(guild)
        for member in guild.members:
            print(member)
            print(member.id)
    user = bot.get_user(232629621038776331)
    await user.send("Bromeo")

##This sends a series of Link pictures from the popular game legend of Zelda
pics = ['Links/1.png', 'Links/2.png', 'Links/3.png', 'Links/4.png', 'Links/5.png']

words = ['HYAAAA', 'CHAAAAA', 'NRYAAAA', 'WAAAAA', 'HAUUUU', '*rusty chain noises*', '-no sound-']

bot = commands.Bot(command_prefix="!")

@bot.command()
async def LINK(ctx):
    await ctx.channel.send(random.choice(words))
    await ctx.channel.send(file=discord.File(random.choice(pics)))
    
async def bitch(ctx):
    await ctx.channel.send("<@" + str(user_id) + ">")

bot.run(TOKEN)
exit()
