import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def users(ctx):
    await ctx.send(f"usuarios:  {bot.user}")
    
@bot.command()
async def help(ctx):
    await ctx.send(f"comandos: $hello, $usuarios, $heh  {bot.user}")


bot.run("import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def users(ctx):
    await ctx.send(f"usuarios:  {bot.user}")
    
@bot.command()
async def help(ctx):
    await ctx.send(f"comandos: $hello, $usuarios, $heh  {bot.user}")

@bot.command()
async def decime_un_chiste(ctx):
    await ctx.send(f" cual es el cafe mas peligroso? el ex-preso :){bot.user}")

bot.run("token")
