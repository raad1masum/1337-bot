import discord
from discord.ext import commands

f = open("token", "r")
token = f.read()

bot = commands.Bot(command_prefix='.')

@bot.event
async def on_ready():
    print("Bot is ready.")

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run(token)
