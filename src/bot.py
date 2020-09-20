import discord
from discord.ext import commands

alphabet = "abcdefghijklmnopqrstuvwxyz "
leetspeak  = "@bcd3fgh1jk1mn0pqr57uvwxyz "

bot = commands.Bot(command_prefix='l')

def leet(word):
    out = ""
    for letter in word:
        if letter in alphabet:
            out += leetspeak[alphabet.index(letter)]
    return out

@bot.event
async def on_ready():
    print("Bot is ready.")

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def eet(ctx, str):
    await ctx.send(leet(str))

f = open("token", "r")
token = f.read()

bot.run(token)
