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
async def calculadora(ctx,operacion="",num1=0,num2=0):
    if operacion=="suma":
        resultado=num1+num2
    elif operacion=="resta":
        resultado=num1-num2
    elif operacion=="multiplicacion":
        resultado=num1 *num2
    elif operacion =="division":
        if num2!=0:
            resultado=num1/num2
    else:
        await ctx.send("Esta calculadora es de matemanicas basicas")
        return
    await ctx.send(f"El resultado de tu {operacion} es: {resultado}")
