import discord
from discord.ext import commands

alphabet = "abcdefghijklmnopqrstuvwxyz "
leetspeak  = "@6cd3fgh1jk1mn09qr57uvwxyz_"

bot = commands.Bot(command_prefix='lee')

def leet(word):
    out = ""
    for letter in word:
        if letter in alphabet:
            out += leetspeak[alphabet.index(letter)]
        else:
            out += letter
    return out

@bot.event
async def on_ready():
    print("Bot is ready.")

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def t(ctx, str):
    await ctx.send(leet(str))

f = open("token", "r")
token = f.read()

bot.run(token)
