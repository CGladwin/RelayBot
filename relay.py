import discord
import random
import asyncio
from discord.ext import commands

token = "NzAwMDcxNTE2OTM0NjM1NTcw.Xtkmow.SBWfvwzY8coBfxxZ_8sD7r0RT4g"
client = commands.Bot(command_prefix=".")

class Player:
    def __init__(self, name: discord.user):
        self.name = name
    def __eq__(self, other):
        return self.name == other.name
    def __repr__(self):
        return self.name.mention

class Game:
    # Game is a listof Players, nicknames
    def __init__(self, players=[],nicknamedict={}):
        '''
        players: list(Player), roles: list(Character), missions: list(Mission), lotl: Lady 

        '''
        self.players = players
        self.nicknamedict = nicknamedict
    
    def __repr__(self):
        if len(self.players) == 0:
            return "Nobody has joined yet!"
        rv = "Players: "
        for p in self.players:
            rv += repr(p) + " "
        return rv

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    await client.process_commands(message)

@client.command()
async def testing(ctx):
    await ctx.send("poopoopeepee!")

@client.command()
async def testing2(ctx):
    await ctx.send("poo!")

setup_commands = ["join", "leave","start","mafia"]
@client.command()
async def cmds(ctx):
    embed = discord.Embed(title="Commands",description=None,color=discord.Colour.blue())
    embed.add_field(name=".mafia",value="start setup of a game session",inline=False)
    embed.add_field(name=".join",value="join the party. Be sure to include your 5-letter or shorter nickname(e.g. \".join Nicky\")",inline=False)
    embed.add_field(name=".leave",value="leave the party",inline=False)
    embed.add_field(name=".start",value="start the game. **This and all commands above aren't usable once the game is started.**",inline=False)
    embed.add_field(name=".w",value="dm the bot to whisper to another player (.w [their nickname][message] e.g.\".w Nicky Hey, How are you?\")",inline=False)
    embed.add_field(name=".nicknames",value="dm the bot to get a list of all players and their nicknames for this game",inline=False)
    embed.add_field(name=".reset",value="ends current game, allows players to join and leave again",inline=False)
    await ctx.send(embed=embed)
@client.command()
async def mafia(ctx):
    await setup(ctx)

async def setup(ctx, g=Game()):
    og = ctx
    await og.send("Let's play some mafia, join up.")

    def clear_commands():
        for cmd in setup_commands:
            client.remove_command(cmd)

    @client.command()
    async def join(ctx,nickname):
        ''' joins the party '''
        if ctx.author in g.players:
            await og.send("{0} is already in the party.".format(ctx.author.mention))
        else:
            if nickname in g.nicknamedict or len(nickname)>5 or nickname.isalpha()==False:
                await og.send("pick another nickname. 5 letters max, don't use numbers or special characters.")
            else:
                # if bool(g.nicknamedict)==False:
                #     g.nicknamedict.setdefault("nickname","user")
                g.players.append(Player(ctx.author))
                # g.nicknamedict.update({nickname,ctx.author})
                g.nicknamedict[nickname]=ctx.author
                await og.send("{0} joined the party.".format(ctx.author.mention))
                print(g.nicknamedict)

    @client.command()
    async def leave(ctx):
        try: 
            g.players.remove(Player(ctx.author))
            del g.nicknamedict[list(g.nicknamedict.keys())[list(g.nicknamedict.values()).index(ctx.author)]]
            await og.send("{0} successfully left the party.".format(ctx.author.mention))
            print(g.nicknamedict)
        except: 
            await og.send("{0} is not in the party.".format(ctx.author.mention))
    @client.command()
    async def start(ctx):
        if Player(ctx.author) in g.players:
            global playerlist 
            playerlist = g.players
            clear_commands()
            await gamestart(ctx)
        else:
            await ctx.send("join up first "+ctx.author.mention)
async def gamestart(ctx,g=Game()):
    await ctx.send("successfully started")
    og = ctx
    @client.command()
    @commands.check(discord.ext.commands.dm_only())
    async def w(ctx,nickname,*,msg):
        nick=g.nicknamedict[nickname]
        aut=str(ctx.author)
        if nickname in g.nicknamedict and Player(ctx.author) in playerlist:
            await nick.send(aut+" says: "+msg)
            await og.send("**"+list(g.nicknamedict.keys())[list(g.nicknamedict.values()).index(ctx.author)]+"**"+" ("+aut+")"+" is whispering to "+"**"+nickname+"**"+" ("+str(nick)+")")
        else:
            await ctx.author.send("both of you have to be in this game to whisper")
    @client.command()
    @commands.check(discord.ext.commands.dm_only())
    async def nicknames(ctx):
        for key, value in g.nicknamedict.items():
            await ctx.send(str(value)[:-5]+' : '+key)    
    @client.command()
    async def reset(ctx):
        await ctx.send("resetting...")
        await setup(ctx,g)
client.run(token)