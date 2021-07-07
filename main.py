import os, discord, twitterimg, requests, re, igimg
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
    try:
        if msg[0] == '!':
            await bot.process_commands(message)
        elif "zck" in msg or "zisk" in msg:
            await message.channel.send(zck.query([])[0])
    except: pass
    

@bot.command(brief = "Says hi!", description = "Says hi!")
async def hi(ctx):
    filename = os.path.realpath(__file__) 
    filename = os.path.dirname(filename) + "/scum/hi.jpg"
    with open (filename, 'rb') as fp:
        await ctx.send(file = discord.File(fp))

@bot.command(brief = "Shows a picture of soft", description = "Shows a picture of soft from twitter with tag ぬいぐるみ撮影60分一本勝負")
async def soft(ctx):
    ## Get some soft photos from the web and return it.
    url, source = twitterimg.query("%23ぬいぐるみ撮影60分一本勝負")
    embed = discord.Embed(title = 'Soft!', description=source)
    embed.set_image(url=url)
    await ctx.send(embed=embed)

@bot.command(brief = "Shows a picture of ina", description = "Shows a picture of ina from twitter with tag inART")
async def wah(ctx):
    ## Get some wah photos from the web and return it.
    url, source = twitterimg.query("%23" + "inART")
    embed = discord.Embed(title = 'Wah!', description=source)
    embed.set_image(url=url)
    await ctx.send(embed=embed)

@bot.command(brief = "Shows a picture of gura", description = "Shows a picture of gura from twitter with tag gawrt")
async def gooruh(ctx):
    ## Get some shark photos from the web and return it.
    url, source = twitterimg.query("%23" + "gawrt")
    embed = discord.Embed(title = 'Shaaaaaark!', description=source)
    embed.set_image(url=url)
    await ctx.send(embed=embed)

@bot.command(brief = "Shows a picture of designated tag", description = "Shows a picture of designated tag from twitter with tag ぬいぐるみ撮影60分一本勝負")
async def twit(ctx, *args):
    ## Get some photos from the web and return it.
    que_str = str(args[0])
    url, source = twitterimg.query("%23" + que_str)
    embed = discord.Embed(title = 'Here is your {}!'.format(que_str), description=source)
    embed.set_image(url=url)
    await ctx.send(embed=embed)

@bot.command(brief = "Shows a picture of ramen", description = "Shows a picture of ramen from instagram with tag 拉麵")
async def ramen(ctx):
    ## Get some ramen photos from the web and return it.
    url, source = igimg.query("台北拉麵")
    embed = discord.Embed(title = 'Ramen!', description="https://www.instagram.com/p/" + source)
    embed.set_image(url=url)
    await ctx.send(embed=embed)

@bot.command(brief = "Shows a zck quotation", description = "Shows a zck quotation from the database")
async def zisk(ctx, *args): #variable size length
    try:
        arr = [int(num) for num in args]
    except:
        arr = []
    messages = zck.query(arr)
    for message in messages:
        await ctx.send(message)

@bot.command(brief = "Corrects wrong Chinese words", description = "Makes a post request to https://coct.naer.edu.tw/spcheck/do/")
async def denial(ctx, *args):
    message = str(args[0])
    r = requests.post('https://coct.naer.edu.tw/spcheck/do', json = {"text" : message})
    msg = r.json()["output"]
    msg = re.sub("<[^<>]*>", "", msg)
    await ctx.send(msg)

@bot.command(brief = "Remind the user after {input} minutes", description = "Enter an integer. The bot will tag you after that time(in minutes). Type cancel(no prefix) to cancel the countdown at any time.")
async def countdown(ctx, time : int):
    await ctx.send("Countdown started!")
    def check(message):
        return message.channel == ctx.channel and message.author == ctx.author and message.content.lower() == "cancel"
    try:
        await bot.wait_for("message", check=check, timeout=time * 60)
        await ctx.send("Countdown cancelled.")
    except:
        await ctx.send("{} Your countdown has ended!".format(ctx.author.mention))

bot.run(token)
