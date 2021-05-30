import os, discord, twitterimg, pickle, random
from zck_quotes.zck import zck
from discord.ext import commands

token = os.getenv("DISCORD_TOKEN")

help_command = commands.DefaultHelpCommand(
    no_category = 'Commands',
    sort_commands = False
)

bot = commands.Bot(command_prefix='!', help_command=help_command)

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

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    msg = message.content.lower()
    if "zck" in msg or "zisk" in msg:
        await message.channel.send(zck.query([])[0])
    

@bot.command(brief = "Says hi!", description = "Says hi!")
async def hi(ctx):
    print(ctx.channel)
    await ctx.send("Hi!")

@bot.command(brief = "Shows a picture of soft", description = "Shows a picture of soft from twitter with tag ぬいぐるみ撮影60分一本勝負")
async def soft(ctx):
    ## Get some soft photos from the web and return it.
    url = twitterimg.query("%23ぬいぐるみ撮影60分一本勝負")
    embed = discord.Embed(title = 'Soft!')
    embed.set_image(url=url)
    await ctx.send(embed=embed)

@bot.command(brief = "Shows a picture of ina", description = "Shows a picture of ina from twitter with tag inART")
async def wah(ctx):
    ## Get some wah photos from the web and return it.
    url = twitterimg.query("%23" + "inART")
    embed = discord.Embed(title = 'Wah!')
    embed.set_image(url=url)
    await ctx.send(embed=embed)

@bot.command(brief = "Shows a picture of gura", description = "Shows a picture of gura from twitter with tag gawrt")
async def gooruh(ctx):
    ## Get some shark photos from the web and return it.
    url = twitterimg.query("%23" + "gawrt")
    embed = discord.Embed(title = 'Shaaaaaark!')
    embed.set_image(url=url)
    await ctx.send(embed=embed)

@bot.command(brief = "Shows a zck quotation", description = "Shows a zck quotation from the database")
async def zisk(ctx, *args): #variable size length
    arr = [int(num) for num in args]
    messages = zck.query(arr)
    for message in messages:
        await ctx.send(message)

bot.run(token)
