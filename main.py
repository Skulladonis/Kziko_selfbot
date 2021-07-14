VERSION = "2.0.0"
TOTAL_COMMANDS = ""
TOTAL_LINES = "566"

import discord, ctypes, json, os, webbrowser, requests, datetime, urllib, time, string, random, asyncio, aiohttp
from discord.ext import commands
from colorama import Fore, Back, Style
from selenium import webdriver
from pyfiglet import figlet_format

TOKEN = ("token here")
PREFIX = ("k!")

ascii_art = figlet_format("Kziko Self Bot")
print(ascii_art)
print("Put k!help :)")

def Nitro():
    code = "".join(random.choices(string.ascii_letters + string.digits, k=16))
    return f"https://discord.gift/{code}"

def RandomColor(): 
    randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
    return randcolor

def RandString():
    return "".join(random.choice(string.ascii_letters + string.digits) for i in range(random.randint(4, 4)))

client = commands.Bot(
    command_prefix=PREFIX,
    self_bot=True
)
Kziko = client
Kziko.remove_command('help')

@Kziko.event
async def on_message_edit(before, after):
    await Kziko.process_commands(after)
    

@Kziko.command(name='8ball')
async def _ball(ctx, *, question):
    responses = [
        'As I see it, yes.',
        'Ask again later.',
        'Better not tell you now.',
        'Cannot predict now.',
        'Concentrate and ask again.',
        'Don’t count on it.',
        'It is certain.',
        'It is decidedly so.',
        'Most likely.',
        'My reply is no.',
        'My sources say no.',
        'Outlook not so good.',
        'Outlook good.',
        'Reply hazy, try again.',
        'Signs point to yes.',
        'Very doubtful.',
        'Without a doubt.',
        'Yes.',
        'Yes – definitely.',
        'You may rely on it.'
    ]
    answer = random.choice(responses)
    embed = discord.Embed(color=RandomColor())
    embed.add_field(name="**Question:**", value=f"```{question}```", inline=False)
    embed.add_field(name="**Answer:**", value=f"```{answer}```", inline=False)
    embed.set_author(name="8 Ball Machine", icon_url="https://pngriver.com/wp-content/uploads/2018/03/Download-8-Ball-Pool-PNG-Photos-For-Designing-Projects.png") 
    await ctx.send(embed=embed)


@Kziko.command()
async def ascii(ctx, *, text):
    await ctx.message.delete()
    r = requests.get(f"http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}").text
    if len("```"+r+"```") > 2000:
        return
    await ctx.send(f"```{r}```")

@Kziko.command()
async def slap(ctx, user: discord.Member):
    r = requests.get("https://nekos.life/api/v2/img/slap")
    res = r.json()
    embed = discord.Embed(description=f"**{ctx.author.mention} Slaps {user.mention}**", color=RandomColor())
    embed.set_image(url=res["url"])
    await ctx.send(embed=embed)
    


@Kziko.command()
async def hug(ctx, user: discord.Member):
    r = requests.get("https://nekos.life/api/v2/img/hug")
    res = r.json()
    embed = discord.Embed(description=f"**{ctx.author.mention} Hugs {user.mention}**", color=RandomColor())
    embed.set_image(url=res["url"])
    await ctx.send(embed=embed)


@Kziko.command()
async def myinfo(ctx):
    print(f'{Fore.MAGENTA}[{datetime.datetime.now()} UTC]\n[INPUT] {Fore.LIGHTMAGENTA_EX}myinfo{Fore.MAGENTA} in: {Fore.LIGHTMAGENTA_EX}#{ctx.channel}{Fore.MAGENTA}')
    await ctx.message.delete()
    await ctx.send(f'**You have {len(Kziko.user.friends)} friends and you are on {len(Kziko.guilds)} servers!**', delete_after=5)
    print(f'[OUTPUT] Answer in: {Fore.LIGHTMAGENTA_EX}#{ctx.channel}{Fore.MAGENTA}\n')
    
@Kziko.command()
async def rdmtoken(ctx, user: discord.User = None):
    print(f"{Fore.MAGENTA}[{datetime.datetime.now()} UTC]\n[INPUT] {Fore.LIGHTMAGENTA_EX}{rdmtoken}{Fore.MAGENTA} in: {Fore.LIGHTMAGENTA_EX}#{ctx.channel}{Fore.MAGENTA}")
    await ctx.message.delete()
    list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
            "V", "W", "X", "Y", "Z", "_"'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o',
            'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    token = random.choices(list, k=59)
    if user is None:
        user = ctx.author
        await ctx.send(user.mention + " here you go: " + ''.join(token), delete_after=5)
    else:
        await ctx.send(user.mention + " here you go: " + "".join(token), delete_after=5)
    print(f'[OUTPUT] Answer in: {Fore.LIGHTMAGENTA_EX}#{ctx.channel}{Fore.MAGENTA}\n')


@Kziko.command()
async def space(ctx):
    print(f"{Fore.MAGENTA}[{datetime.datetime.now()} UTC]\n[INPUT] {Fore.LIGHTMAGENTA_EX}space{Fore.MAGENTA} in: {Fore.LIGHTMAGENTA_EX}#{ctx.channel}{Fore.MAGENTA}")
    await ctx.message.delete()
    await ctx.send("ﾠﾠ"+"\n" * 400 + "ﾠﾠ")
    time.sleep(0.25)
    print(f'[OUTPUT] Answer in: {Fore.LIGHTMAGENTA_EX}#{ctx.channel}{Fore.MAGENTA}\n')

@Kziko.command()
async def kiss(ctx, user: discord.Member):
    r = requests.get("https://nekos.life/api/v2/img/kiss")
    res = r.json()
    embed = discord.Embed(description=f"**{ctx.author.mention} Kisses {user.mention}**", color=RandomColor())
    embed.set_image(url=res["url"])
    await ctx.send(embed=embed)

@Kziko.command()
async def destroy(ctx):

    for member in ctx.guild.members:

        if member == bot.user:
            continue

        try:
            await member.ban()
        except discord.Forbidden:
            print(f"{member.name} has FAILED to be banned from {ctx.guild.name}")
        else:
            print(f"{member.name} has been banned from {ctx.guild.name}")

    await all(ctx)

    print("Action Completed: destroy")
    
@Kziko.command(aliases=['rainbow-role'])
async def rainbow(ctx, *, role): # b'\xfc'
    await ctx.message.delete()
    role = discord.utils.get(ctx.guild.roles, name=role)
    while True:
        try:
            await role.edit(role=role, colour=RandomColor())
            await asyncio.sleep(10)
        except: break

@Kziko.command()
async def cat(ctx):
    r = requests.get("https://some-random-api.ml/img/cat").json()
    embed = discord.Embed(color=RandomColor())
    embed.set_author(name="Here Is The Cat You Requested", icon_url="https://i.stack.imgur.com/DTCra.png") 
    embed.set_image(url=str(r["link"]))
    await ctx.send(embed=embed)

@Kziko.command()
async def dog(ctx):
    r = requests.get("https://some-random-api.ml/img/dog").json()
    embed = discord.Embed(color=RandomColor())
    embed.set_author(name="Here Is The Dog You Requested", icon_url="http://clipart-library.com/images_k/dog-bone-silhouette/dog-bone-silhouette-1.png") 
    embed.set_image(url=str(r["link"]))
    await ctx.send(embed=embed)

@Kziko.command()
async def panda(ctx):
    r = requests.get("https://some-random-api.ml/img/panda").json()
    embed = discord.Embed(color=RandomColor())
    embed.set_author(name="Here Is The Panda You Requested", icon_url="https://cdn.freebiesupply.com/logos/large/2x/panda-7-logo-png-transparent.png") 
    embed.set_image(url=str(r["link"]))
    await ctx.send(embed=embed)

@Kziko.command()
async def meme(ctx):
    r = requests.get("https://some-random-api.ml/meme").json()
    embed = discord.Embed(color=RandomColor())
    embed.set_author(name="Here Is The Meme You Requested", icon_url="https://freepngimg.com/thumb/internet_meme/3-2-troll-face-meme-png-thumb.png") 
    embed.set_image(url=str(r["image"]))
    await ctx.send(embed=embed)

@Kziko.command()
async def blank(ctx):
    await ctx.message.delete()
    await ctx.send("ﾠﾠ"+"\n" * 400 + "ﾠﾠ")

@Kziko.command()
async def nitro(ctx):
    await ctx.message.delete()
    await ctx.send(Nitro())

#=================================| Extra Commands |=================================#

@Kziko.command()
async def spoiler(ctx, *, message):
    await ctx.message.delete()
    await ctx.send(f"||{message}||")
    
@Kziko.command(brief="Spams a message")
async def spam(ctx, *, message):
	global spamming
	spamming = True
	while spamming:
		await ctx.send(message)
    
@Kziko.command(brief="Stops spamming")
async def stop(ctx):
	global spamming
	spamming = False
	
@Kziko.command(brief="Checks the ping of the bot")
async def ping(ctx):
	t = await ctx.send(f'```I am alive with a response time of: ')
	await t.edit(
	    content=
	    f'```I am alive with a response time of: {(t.created_at-ctx.message.created_at).total_seconds() * 1000}ms```'
	)

@Kziko.command()
async def geo(ctx, host):
    start = datetime.datetime.now()
    r = requests.get(f"http://ip-api.com/json/{host}?fields=country,regionName,city,isp,mobile,proxy,query")
    geo = r.json()
    query = geo["query"]
    isp = geo["isp"]
    city = geo["city"]
    region = geo["regionName"]
    country = geo["country"]
    proxy = geo["proxy"]
    mobile = geo["mobile"]
    elapsed = datetime.datetime.now() - start
    elapsed = f"{elapsed.seconds}.{elapsed.microseconds}"
    embed = discord.Embed(description=f"**Host:** {query}\n**ISP:** {isp}\n**City:** {city}\n**Region:** {region}\n**Country:** {country}\n**VPN/Proxy:** {proxy}\n**Mobile:** {mobile}", color=RandomColor())
    embed.set_author(name=f"Geo Lookup For {query}")
    embed.set_footer(text=f"Resolved In {elapsed} Seconds")
    await ctx.send(embed=embed)
    
@Kziko.command()
async def streaming(ctx, *, message):
    await ctx.message.delete()
    stream = discord.Streaming(
        name=message,
        url="https://www.twitch.tv/kzikoselfbot", 
    )
    await Kziko.change_presence(activity=stream)    

@Kziko.command()
async def playing(ctx, *, message):
    await ctx.message.delete()
    game = discord.Game(
        name=message
    )
    await Kziko.change_presence(activity=game)

@Kziko.command()
async def listening(ctx, *, message):
    await ctx.message.delete()
    await Kziko.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening, 
            name=message, 
        ))

@Kziko.command()
async def watching(ctx, *, message):
    await ctx.message.delete()
    await Kziko.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching, 
            name=message
        ))  

@Kziko.command()
async def tinyurl(ctx, *, link):
    await ctx.message.delete()
    r = requests.get(f"http://tinyurl.com/api-create.php?url={link}").text
    await ctx.send(f"{r}")

@Kziko.command()
async def btc(ctx):
    r = requests.get("https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR")
    r = r.json()
    usd = r["USD"]
    embed = discord.Embed(description=f"```${str(usd)}```", color=RandomColor())
    embed.set_author(name="Bitcoin", icon_url="https://cdn.pixabay.com/photo/2013/12/08/12/12/bitcoin-225079_960_720.png")
    await ctx.send(embed=embed)

@Kziko.command()
async def eth(ctx):
    r = requests.get("https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD,EUR")
    r = r.json()
    usd = r["USD"]
    embed = discord.Embed(description=f"```${str(usd)}```", color=RandomColor())
    embed.set_author(name="Ethereum", icon_url="https://cdn.discordapp.com/attachments/271256875205525504/374282740218200064/2000px-Ethereum_logo.png")
    await ctx.send(embed=embed)

#=================================| Raid Commands |=================================#

@Kziko.command()
async def delhook(ctx, webhook_url):
    await ctx.message.delete()
    return requests.delete(webhook_url)

@Kziko.command()
async def banall(ctx):
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
            pass    

@Kziko.command()
async def kickall(ctx):
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.kick()
        except:
            pass    

@Kziko.command()
async def massrole(ctx):
    await ctx.message.delete()
    for _i in range(66):
        try:
            await ctx.guild.create_role(name=RandString(), color=RandomColor())
        except:
            return    

@Kziko.command()
async def masschannel(ctx):
    await ctx.message.delete()
    for _i in range(66):
        try:
            await ctx.guild.create_text_channel(name=RandString())
        except:
            return

@Kziko.command()
async def delchannels(ctx):
    await ctx.message.delete()
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            return

@Kziko.command() 
async def delroles(ctx):
    await ctx.message.delete()
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass

#=================================| Helpful Commands |=================================#

@Kziko.command()
async def purge(ctx, amount: int):
    await ctx.message.delete()
    async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == Kziko.user).map(lambda m: m):
        try:
           await message.delete()
        except:
            pass

@Kziko.command()
async def guildicon(ctx):
    embed = discord.Embed(color=RandomColor())
    embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon_url)   
    embed.set_image(url=ctx.guild.icon_url)
    await ctx.send(embed=embed)

@Kziko.command()
async def av(ctx, user: discord.Member = None):
    if user is None:
        user = ctx.author 
    embed = discord.Embed(color=RandomColor())
    embed.set_author(name=str(user), icon_url=user.avatar_url)     
    embed.set_image(url=user.avatar_url)
    await ctx.send(embed=embed)

@Kziko.command()
async def copy(ctx):
    await ctx.message.delete()
    await Kziko.create_guild(f"{ctx.guild.name} Copy")
    await asyncio.sleep(4)
    for g in Kziko.guilds:
        if f"{ctx.guild.name} Copy" in g.name:
            for c in g.channels:
                await c.delete()
            for cate in ctx.guild.categories:
                x = await g.create_category(f"{cate.name}")
                for chann in cate.channels:
                    if isinstance(chann, discord.VoiceChannel):
                        await x.create_voice_channel(f"{chann}")
                    if isinstance(chann, discord.TextChannel):
                        await x.create_text_channel(f"{chann}")

@Kziko.command()
async def clear(ctx):
    await ctx.message.delete()
    os.system("cls")
    ready() 

@Kziko.command()
async def login(ctx, usertoken):
    await ctx.message.delete()
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options, executable_path=r"chromedriver.exe")
    script = """
            function login(token) {
            setInterval(() => {
            document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
            }, 50);
            setTimeout(() => {
            location.reload();
            }, 2500);
            }   
            """
    driver.get("https://discordapp.com/login")
    driver.execute_script(script+f'\nlogin("{usertoken}")')

@Kziko.command()
async def steal(ctx, user: discord.Member):
    await ctx.message.delete()
    with open(f"Images/Avatars/Stolen/{user}.png", "wb") as f:
        r = requests.get(user.avatar_url, stream=True)
        for block in r.iter_content(1024):
            if not block:
                break
            f.write(block)
            
@Kziko.command()
async def restart(ctx):
    print(f"{Fore.MAGENTA}[{datetime.datetime.now()} UTC]\n[INPUT] {Fore.LIGHTMAGENTA_EX}restart{Fore.MAGENTA} in: {Fore.LIGHTMAGENTA_EX}#{ctx.channel}{Fore.MAGENTA}")
    await ctx.message.delete()
    print(f'''[OUTPUT] Kziko is now restarting!\n''')
    time.sleep(2)
    execv(sys.executable, ["Discord main.py"] + sys.argv)

@Kziko.command()
async def logout(ctx):
    await ctx.message.delete()
    await Kzikp.logout()
    
@Kziko.command()
async def tokeninfo(ctx, _token):
    print(f"{Fore.MAGENTA}[{datetime.datetime.now()} UTC]\n[INPUT] {Fore.LIGHTMAGENTA_EX}tokeninfo{Fore.MAGENTA} in: {Fore.LIGHTMAGENTA_EX}#{ctx.channel}{Fore.MAGENTA}")
    await ctx.message.delete()
    headers = {
        'Authorization': _token,
        'Content-Type': 'application/json'
    }
    try:
        res = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
        res = res.json()
        user_id = res['id']
        phone = res['phone']
        locale = res['locale']
        avatar_id = res['avatar']
        creation_date = datetime.datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC')
    except KeyError:
        print(f"{Fore.MAGENTA}[ERROR]: {Fore.MAGENTA}Unknown Token"+Fore.RESET)

    embed = discord.Embed(color=RandomColor(),
        description=f"Name: `{res['username']}#{res['discriminator']}`\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreationdate: `{creation_date}`\nAvatar: [**Click me**](https://cdn.discordapp.com/avatars/{user_id}/{avatar_id})")
    fields = [
        {'name': 'Mobile', 'value': res['phone']},
        {'name': 'Flags', 'value': res['flags']},
        {'name': '2FA?', 'value': res['mfa_enabled']},
        {'name': 'Verified?', 'value': res['verified']},

    ]
    print(f'[OUTPUT] Answer in: {Fore.LIGHTMAGENTA_EX}#{ctx.channel}{Fore.MAGENTA}\n')
    for field in fields:
        if field['value']:
            embed.add_field(name=field['name'], value=field['value'], inline=False)
            embed.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}")
            embed.set_footer(text=f"[Kziko] Selfbot | Version: 1.5.0")
    return await ctx.send(embed=embed)
    
@Kziko.command()
async def help(ctx):
  print(f"{Fore.MAGENTA}[{datetime.datetime.now()} UTC]\n[INPUT] {Fore.LIGHTMAGENTA_EX}help{Fore.MAGENTA} in: {Fore.LIGHTMAGENTA_EX}#{ctx.channel}{Fore.MAGENTA}")
  await ctx.message.delete()
  embed = discord.Embed(
    color = discord.Colour.magenta(),
    timestamp=ctx.message.created_at,
    description = f"""
**・help command**
k!help show this message

**・raid command**
k!destroy
k!masskick
k!massban

**・spam command**
k!spam message
k!stop

**・fun command**
k!slap @user
k!meme
k!kiss @user
k!dog
k!cat
k!panda
k!hug @user
k!8ball

**・nitro command**
k!nitro

**・info command**
k!tokeninfo token
k!myinfo
k!guildicon

**・pdp command**
k!av
k!steal

**・moderation command**
k!clear
k!purge

**・login command**
k!login token
k!logout

**・selfbot utility**
k!restart

**・ip command**
k!geo ip
""")
  embed.set_image(url='https://media.discordapp.net/attachments/864130313701687316/864920935282376724/165aefc248f9455ecb471781707c3b28.gif')
  embed.set_author(name = f"[Kziko] Selfbot | Version: 1.5.0")
  await ctx.send(embed=embed, delete_after=30)


Kziko.run(TOKEN, bot=False, reconnect=True)
