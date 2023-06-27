import discord
from discord.ext import commands, tasks
import os
from dotenv import load_dotenv
import youtube_dl

load_dotenv()
token = os.getenv("token")

intents = discord.Intents().all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command(name="join", help="musik95 joined the channel!")
async def join(ctx):
    if not ctx.message.author.voice:
        await ctx.send(f"{ctx.message.author.name} is not connected to channel!")
        return
    else:
        channel=ctx.message.author.voice.channel
        await channel.connect()

@bot.command(name="leave", help=" left the channel!")
async def leave(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_connected():
        await voice_client.disconnect()
    else:
        await ctx.send(f"{ctx.message.author.name} is not connected to a channel!")

if __name__ == "__main__":
    bot.run(token)