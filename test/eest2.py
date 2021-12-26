from asyncio.tasks import wait
from youtubesearchpython import VideosSearch
import discord
from discord.ext import commands
import validators
from pytube import YouTube
import os
from asyncio import sleep

from youtubesearchpython.search import PlaylistsSearch

bot = commands.Bot(command_prefix="mm.",help_command=None)
activity = discord.Game(name="Prefix: mm.")

TOKEN = open("TOKEN.txt","r").read()

def isurl(URL:str):
    return validators.url(URL)

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.do_not_disturb,activity=activity)

    print(f"{bot.user} Pronto para o uso")

@bot.command()
async def help(ctx:discord.TextChannel):
    page1 = discord.Embed (title="Página 1/6",colour = discord.Colour.red())
    page1.description = "Comandos principais"
    page1.set_author(name="Autor: ChickChuck2#4645",icon_url="https://cdn.discordapp.com/avatars/462768330005282816/a_a02c469e8e8948276e66a40b068f0ce0.gif?size=4096")
    
    page1.add_field(name="Salve", value="Em desenvolvimento ainda..", inline=False)

    pages = [page1]

    message = await ctx.send(embed = page1)
    await message.add_reaction('⏮')
    await message.add_reaction('◀')
    await message.add_reaction('▶')
    await message.add_reaction('⏭')

    def check(reaction, user):
        return user == ctx.author
    i = 0
    reaction = None

    while True:
        if str(reaction) == '⏮':
            i = 0
            await message.edit(embed = pages[i])
        elif str(reaction) == '◀':
            if i > 0:
                i -= 1
                await message.edit(embed = pages[i])
        elif str(reaction) == '▶':
            if i < len(pages):
                i += 1
                await message.edit(embed = pages[i])
        elif str(reaction) == '⏭':
            i = len(pages)
            await message.edit(embed = pages[i])
        try:
            reaction, user = await bot.wait_for('reaction_add', timeout = 50.0, check = check)
            await message.remove_reaction(reaction, user)
        except:
            break

    await message.clear_reactions()

playlist = []

@bot.command(aliasses=["p","Play"])
async def play(ctx:discord.TextChannel, * ,URL:str):
    playlist.append(URL)
    
    for music in playlist:
        print(playlist)
        try:
            channel = ctx.author.voice.channel
            await channel.connect()
        except:
            pass

        yt = YouTube(music)
        try:
            video = yt.streams.filter(only_audio=True).first()
            outfile = video.download()
        except FileExistsError:
            os.remove(outfile)
            pass

        base, ext = os.path.splitext(outfile)
        new_file = base + ".mp3"

        try:
            os.rename(outfile, new_file)
        except:
            pass
        try:
            source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(new_file))
            ctx.voice_client.play(source,after= lambda e: print("Erro ao tocar") if e else None)

            for time in range(yt.length + 1):
                print(f"{time} >> {yt.length}")
                await sleep(1)
                if time == yt.length:
                    print("Deletando o arquivo musical")
                    os.remove(new_file)
                    playlist.remove(URL)
                    print(playlist)
        except discord.ClientException:
            await ctx.send("Música na fila")
            
    print("END")

bot.run(TOKEN)