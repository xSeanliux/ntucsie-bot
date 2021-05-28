import os, discord, twitter, twitterimg
from discord import embeds
from discord.ext import commands

token = os.getenv("DISCORD_TOKEN")

print(twitter)

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print("Start!")

@bot.event
async def on_member_join(member):
    print("{} joined.".format(member.name))
    await member.send(
        "歡迎 {} 加入台大資工新生群!\n".format(member.name) +
        "請看群組中的 announcement 頻道以進行身分認證"
    )

@bot.command()
async def hi(ctx):
    print(ctx.channel)
    await ctx.send("Hi!")

@bot.command()
async def soft(ctx):
    ## Get some soft photos from the web and return it.
    url = twitterimg.query("%23ぬいぐるみ撮影60分一本勝負")
    embed = discord.Embed(title = 'Soft!\n')
    embed.set_image(url=url)
    await ctx.send(embed=embed)

@bot.command()
async def wah(ctx):
    ## Get some soft photos from the web and return it.
    url = twitterimg.query("%23" + "inART")
    embed = discord.Embed(title = 'Wah!\n')
    embed.set_image(url=url)
    await ctx.send(embed=embed)

bot.run(token)