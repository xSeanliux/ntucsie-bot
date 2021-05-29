import os, discord, twitterimg, pickle, random
from discord.ext import commands

token = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix='!')
allquotes = []

@bot.event
async def on_ready():
    print("Start!")
    with open ('./zck_quotes/zckquotes', 'rb') as fp:
        global allquotes
        allquotes = pickle.load(fp)
        print("Loaded", len(allquotes), "quotes")

    

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
    ## Get some wah photos from the web and return it.
    url = twitterimg.query("%23" + "inART")
    embed = discord.Embed(title = 'Wah!')
    embed.set_image(url=url)
    await ctx.send(embed=embed)

@bot.command()
async def gooruh(ctx):
    ## Get some shark photos from the web and return it.
    url = twitterimg.query("%23" + "gawrt")
    embed = discord.Embed(title = 'Shaaaaaark!')
    embed.set_image(url=url)
    await ctx.send(embed=embed)

@bot.command()
async def zisk(ctx, *args):
    ## Randomly chooses a quote from ./zck_quotes/zckquotes and displays it
    def getMsg(idx):
        if(idx >= len(allquotes)):
            return "ZCK#%03d not found." % (idx)
        txt = allquotes[idx].splitlines()
        mxlen = 0
        fulltxt = ''
        for x in txt:
            if(x == ''):
                continue
            fulltxt = fulltxt + '> 　' + x.strip() + '\n'
            mxlen = max(mxlen, len(x))
        msg = '> 「\n %s > %s 」——ZCK#%03d' % (fulltxt, '　'*(mxlen + 1), idx)
        return msg

    if(len(args) == 0):
        idx = random.randint(0, len(allquotes))
        await getMsg(idx)
    else:
        for _idx in args:
            await getMsg(_idx)


bot.run(token)
