import os, discord, twitterimg, pickle, random
from discord.ext import commands

token = os.getenv("DISCORD_TOKEN")

help_command = commands.DefaultHelpCommand(
    no_category = 'Commands',
    sort_commands = False
)

bot = commands.Bot(command_prefix='!', help_command=help_command)
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
    
'''
@bot.command()
async def help(ctx):
    embed = discord.Embed(Title='Help')
    embed.add_field(name = "hi", value = "say hi!")
    embed.add_field(name = "soft", value = "return a photo of soft")
    embed.add_field(name = "wah", value = "return a photo of ina")
    embed.add_field(name = "zisk", value = "return a ZCK quotation")
    await ctx.send(embed=embed)
'''

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
    ## Randomly chooses a quote from ./zck_quotes/zckquotes and displays it
    def getMsg(idx): #Gets the #idx -th quote, formats it, and returns it as a string
        if(idx >= len(allquotes) || idx < 0):
            return "ZCK#%03d not found." % (idx)
        txt = allquotes[idx].splitlines()
        mxlen = 0
        fulltxt = ''
        for x in txt:
            if(x == ''):
                continue
            fulltxt = fulltxt + '> 　' + x.strip() + '\n'
            mxlen = max(mxlen, len(x))
        msg = '> 「\n%s> %s 」——ZCK#%03d' % (fulltxt, '　'*(mxlen + 1), idx)
        return msg

    if(len(args) == 0):
        idx = random.randint(0, len(allquotes))
        await ctx.send(getMsg(idx))
    else:
        for _idx in args:
            await ctx.send(getMsg(int(_idx)))



bot.run(token)
