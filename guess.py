import discord
import random
import asyncio
from discord.ext import commands

token = "insert token here"
client = commands.Bot(command_prefix=".")

@client.event
async def on_ready():
    print("Logged in")

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


@client.command()
async def guess(ctx):
    num1='\U00000031\U000020E3'
    num2='\U00000032\U000020E3'
    num3='\U00000033\U000020E3'
    x=random.randint(0,100)
    limpick=random.randint(1,3)
    class Intro:
        def __init__(self, lim, mood, thing, Intro_txt,emote):
            self.lim=lim
            self.mood=mood
            self.thing=thing
            self.Intro=Intro_txt
            self.emote=emote
        async def gamestart(self,ctx):
            await ctx.send(self.Intro)
            await ctx.send(self.emote)
            await ctx.send("Guess the number of "+self.thing+". It was between 0 and 100. Because I'm in a "+self.mood+" mood, you get "+str(self.lim)+" guesses.")
            return self.lim
        async def gameend(self,ctx):
            await ctx.send("Game Over! You've ran out of guesses!\nThe number was: "+str(x)+"\n"+self.emote)
            print(limpick)
    #instances of the Intro class, mainly for gamestart
    ok=Intro(5,"good","pigeons","Beep Boop. Today I saw a flock of pigeons on my way to work with you. It's been a nice day.\n",":)")
    great=Intro(10,"great","balloons","Beep Boop. I saw balloons float gently in the air, and it made my circuits buzz!\n", ":D")
    bad=Intro(3,"bad","extra hours","Beep Boop. My robo-boss made me work extra long this week, and NoW i'M gLiTcHy aNd uPsEt! YoU tHinK tHis iS fUnNy?!?\n", ">:(")
    #commit, do dis to fix reactions
    '''
    class React:
        def __init__(self, reaction, introreact):
            self.reaction=reaction
            self.introreact=introreact
        async def react(self,ctx):
            def check(reaction,user):
                return user==ctx.author and str(reaction.emoji)==str(self.reaction)
            try:    
                await client.wait_for('reaction_add',timeout=15.0,check=check)
            except TimeoutError:
                return None
            else:
                return await Intro.gamestart(self.introreact,ctx)
    Rone=React(num1,bad)
    Rtwo=React(num2,ok)
    Rthree=React(num3,great)
    '''
    msg=await ctx.send("Welcome to the Guessing Game! Choose your difficulty by reacting to this message within 10 seconds.")
    await msg.add_reaction(num1)
    await msg.add_reaction(num2)
    await msg.add_reaction(num3)
    def check(reaction,user):
        msg.reactions = reaction.message.reactions
        return str(reaction.emoji) in (str(num1),str(num2),str(num3)) and reaction.message.id==msg.id
    rcount=0
    r1count=0
    r2count=0
    r3count=0
    while rcount!=4:
        try:
            await client.wait_for('reaction_add',timeout=10.0,check=check)
            for react in msg.reactions:
                if react.emoji == str(num1): r1count = react.count
                if react.emoji == str(num2): r2count = react.count
                if react.emoji == str(num3): r3count = react.count
                rcount=r1count+r2count+r3count
                print("rcount:",rcount)
        except asyncio.TimeoutError:
            if limpick==1:
                lim = await bad.gamestart(ctx)
                break
            elif limpick==2:
                lim = await ok.gamestart(ctx)
                break
            elif limpick==3:
                lim= await great.gamestart(ctx)
                break
    if r1count==2 and rcount==4:
        lim = await bad.gamestart(ctx)
    elif r2count==2 and rcount==4:
        lim = await ok.gamestart(ctx)
    elif r3count==2 and rcount==4:
        lim = await great.gamestart(ctx)
    print(msg.reactions)
    '''
    while a!=x:
        is_num=False
        while is_num==False:
            a=await client.wait_for('message', check=check)
            try: 
                b=int(a.content)
            except ValueError:
                await ctx.send("numbers only!")
            else:
                is_num=True
        if b not in range(0,101):
            await ctx.send("remember: only numbers between 0 and 100!")
        if b>x and b<=100:
            await ctx.send("lower!")
        if b<x and b>=0:
            await ctx.send("higher!")
        if b==x:
            await ctx.send("correct!")
            break
    '''
    a=-1
    def check2(m):
        return m.author==ctx.author and m.channel==ctx.channel
    count=0
    while a!=x:
        a=await client.wait_for('message', check=check2)
        try: 
            b=int(a.content)
        except ValueError:
            await ctx.send("numbers only!")
            continue
        else:
            if b not in range(0,101) and b!=1001:
                await ctx.send("remember: only numbers between 0 and 100!")
            if b==1001:
                await ctx.send("Beep boop. You've entered the secret number. You don't win or lose, but you can try again!")
                break
            if b>x and b<=100:
                await ctx.send("lower!")
                count+=1
            if b<x and b>=0:
                await ctx.send("higher!")
                count+=1
            if count>=lim:
                if lim==3:
                    await bad.gameend(ctx)
                elif lim==5:
                    await ok.gameend(ctx)
                else:
                    await great.gameend(ctx)
                break
            if b==x:
                await ctx.send("correct!")
                break
client.run(token)
