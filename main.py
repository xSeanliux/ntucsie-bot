import os, discord, twitterimg
from discord.ext import commands

token = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix='!')
bot.remove_command("help")

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
async def help(ctx):
    embed = discord.Embed(Title='Help')
    embed.add_field(name = "hi", value = "say hi!")
    embed.add_field(name = "soft", value = "return a photo of soft")
    embed.add_field(name = "wah", value = "return a photo of ina")
    embed.add_field(name = "zisk", value = "return a ZCK quotation")
    await ctx.send(embed=embed)

@bot.command()
async def hi(ctx):
    print(ctx.channel)
    await ctx.send("Hi!")

@bot.command()
async def soft(ctx):
    ## Get some soft photos from the web and return it.
    url = twitterimg.query("%23ぬいぐるみ撮影60分一本勝負")
    embed = discord.Embed(title = 'Soft!')
    embed.set_image(url=url)
    await ctx.send(embed=embed)

@bot.command()
async def wah(ctx):
    ## Get some soft photos from the web and return it.
    url = twitterimg.query("%23" + "inART")
    embed = discord.Embed(title = 'Wah!')
    embed.set_image(url=url)
    await ctx.send(embed=embed)

bot.run(token)