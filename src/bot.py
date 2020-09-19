import discord
from discord.ext import commands
from utilitybelt import change_charset

alphabet = "abcdefghijklmnopqrstuvwxyz "
leetspeak  = "@bcd3fgh1jk1mn0pqr57uvwxyz "

f = open("token", "r")
token = f.read()

bot = commands.Bot(command_prefix='l')

@bot.event
async def on_ready():
    print("Bot is ready.")

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def eet(ctx, str):
    await ctx.send(change_charset(str, alphabet, leetspeak))

bot.run(token)
