import random
import asyncio
import discord
import os

import io
import safygiphy
import requests
import perms


from discord import Game
from discord.ext.commands import Bot
from utilities import getTime





g = safygiphy.Giphy()


BOT_PREFIX = ("?","!")
TOKEN= os.environ.get('TOKEN', None)
WELCOME_CHANNEL_ID=os.environ.get('WELCOME_CHANNEL_ID', None)
CHANNEL_RULES_ID=os.environ.get('CHANNEL_RULES_ID',None)
REPORT_CHANNEL_ID=os.environ.get('REPORT_CHANNEL_ID',None)

CHANNEL_RULES= "<#"+CHANNEL_RULES_ID+">"



client = Bot(command_prefix=BOT_PREFIX)



@client.command(name='frühstück',
                description="Tell that you have breakfast",
                brief="Tell about your breakfast",
                aliases=['breakfast'],
                pass_context=True)

async def frühstück(context):
    possible_responses1 = [
        'a 🍪 ',
        'a :croissant: ',
        'a :chocolate_bar: ',
        'some :bread: ',
        'an :apple: ',
        'a :french_bread: ',
        'a :tea: ',
        'a :green_apple: ',
        'a :coffee: ',
    ]
    possible_responses2 = [
        'with jelly ',
        'with chocolate',
        'with fruits',
        'with Salt',
        'with Sugar',
        'with something to drink',
        'with chilli',
        'with a :kiwi: ',
    ]
    await client.say(context.message.author.mention + " Let me bring you " + random.choice(possible_responses1) + " " + random.choice(possible_responses2))


@client.command(name='like',
                description="Does Monsieur Biscuit likes you?",
                brief="Does Monsieur Biscuit likes you?",
                aliases=['likes'],
                pass_context=True)
async def like(context):
    possible_responses = [
        'I like you very much :hugging: ',
        'I dont even know you enough to tell that',
        'I like you, I hope its the same for you?',
        'You are great I like you :blush: ',
        'I will say nothing...',
        'Why are you asking me that question?',
        'I dont like you more if you keep asking that question over and over again',
    ]
    await client.say(context.message.author.mention + " " + random.choice(possible_responses) )


@client.command(name='spaß',
                description="spaß",
                brief="spaß",
                aliases=['spass'],
                pass_context=True)
async def ask(context):

    await client.say(context.message.author.mention + " macht gerade spaß :joy: :joy: :joy: ")

@client.command(name='hello',
                description="hello",
                brief="hello",
                aliases=['hallo', 'huhu', 'moin', 'morgen', 'nabend', 'abend'],
                pass_context=True)
async def hello(context):

    await client.say("Hello " + context.message.author.mention)

@client.command(name='calm',
                description="tell people to calm down",
                brief="calm down",
                aliases=['ruhig', 'ganzruhig','calmdown'],
                pass_context=True)
async def calm(context):

    await client.say("I get :crying_cat_face: if people are :angry: . Please make me happy again :hugging: ")

@client.command(name='gif',
                description="Search and Post Gif-Tag",
                brief="Post random gif example: !gif hello",
                aliases=['gifs'],
                pass_context=True)
async def gif(context):
            gif_tag = context.message.content
            rgif = g.random(tag=str(gif_tag))
            response = requests.get(
                str(rgif.get("data", {}).get('image_original_url')), stream=True
            )
            await client.send_file(context.message.channel, io.BytesIO(response.raw.read()), filename='video.gif')

@client.command(name='fun',
                description="Search and Post Fun-Gif",
                brief="Post random fun gif",
                pass_context=True)
async def fun(context):
            gif_tag = "fun"
            rgif = g.random (tag=str (gif_tag))
            response = requests.get (
                str (rgif.get ("data", {}).get ('image_original_url')), stream=True
            )
            await client.send_file(context.message.channel, io.BytesIO (response.raw.read ()), filename='video.gif')


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

#    if 'keks' in message.content:
#        await client.send_message (message.channel, ":thinking: Hat hier etwa jemand 🍪 gesagt?")
#    if 'cookie' in message.content:
#        await client.send_message (message.channel, ":thinking: Did anyone say 🍪 ?")


    if 'vote' in message.content:

        await client.add_reaction(message, "👍")
        await client.add_reaction(message, "👎")

    if 'Vote' in message.content:

        await client.add_reaction(message, "👍")
        await client.add_reaction(message, "👎")

    await client.process_commands(message)


@client.command(name='ask',
                description="Answer yes/no question",
                brief="Monsieur answers yes or no questions",
                aliases=['question'],
                pass_context=True)

async def ask(context):
    possible_responses = [
        'This is unlikely',
        'That will not happen',
        'Of course',
        'Yes',
        'No',
        'Maybe',
    ]
    await client.say(random.choice(possible_responses) + " " + context.message.author.mention)

@client.command(name='remind',
                description="Reminds you on tasks, Example: !remind Homework 1h, can only have 1 word for task",
                brief="Example: !remind Homework 1h",
                aliases=['reminder'],
                pass_context=True)
async def remind(ctx):

    getTime()
    args=ctx.message.content
    args=args.split(' ')
    try:
        if 's' in args[2]:
            time=int(args[2].replace('s', ''))
            await client.say(f"Ok, I will remind you in {str(args[2].replace('s',''))} seconds to: {str(args[1])}")
            await asyncio.sleep(time)
            await client.send_message(ctx.message.author,f"You asked to remind you to: {str(args[1])} {str(time)} seconds from {str(getTime())}")
        if 'm' in args[2]:
            time = int(args[2].replace('m', ''))*60
            await client.say(f"Ok, I will remind you in {str(args[2].replace('m',''))} minutes to: {str(args[1])}")
            await asyncio.sleep(time)
            await client.send_message(ctx.message.author,f"You asked to remind you to: {str(args[1])} {str(time/60)} minutes from {str(getTime())}")
        if 'h' in args[2]:
            time = int(args[2].replace('h', ''))*3600
            await client.say(f"Ok, I will remind you in {str(args[2].replace('h',''))} hours to: {str(args[1])}")
            await asyncio.sleep(time)
            await client.send_message(ctx.message.author,f"You asked to remind you to: {str(args[1])} {str(time/3600)} hours from {str(getTime())}")

        if 's' in args[1]:
            time=int(args[1].replace('s', ''))
            await client.say(f"Ok, I will remind you in {str(args[1].replace('s',''))} seconds to: {str(args[2])}")
            await asyncio.sleep(time)
            await client.send_message(ctx.message.author,f"You asked to remind you to: {str(args[2])} {str(time)} seconds from {str(getTime())}")
        if 'm' in args[1]:
            time = int(args[1].replace('m', ''))*60
            await client.say(f"Ok, I will remind you in {str(args[1].replace('m',''))} minutes to: {str(args[2])}")
            await asyncio.sleep(time)
            await client.send_message(ctx.message.author,f"You asked to remind you to: {str(args[2])} {str(time/60)} minutes from {str(getTime())}")
        if 'h' in args[1]:
            time = int(args[1].replace('h', ''))*3600
            await client.say(f"Ok, I will remind you in {str(args[1].replace('h',''))} hours to: {str(args[2])}")
            await asyncio.sleep(time)
            await client.send_message(ctx.message.author,f"You asked to remind you to: {str(args[2])} {str(time/3600)} hours from {str(getTime())}")



    except:
        pass






@client.command(name='warn',
                description="warn someone and tell there are rules",
                brief="Report a user with !warn @user1",
                aliases=['report'],
                pass_context=True)
async def warn(ctx, userName: discord.User):
    """Warn User"""
    report_msg= userName.mention + " you have been warned! Make sure you read the rules at" + CHANNEL_RULES + ":spy:"
    await client.say(report_msg)
    await client.send_message(userName.server.get_channel(REPORT_CHANNEL_ID), userName.mention + " has been reported!")



@client.command(name='ban',
                description="ban user",
                brief="ban user",
                aliases=['kick'],
                pass_context=True)
async def ban(ctx, userName2: discord.User):

            if not perms.check(ctx.message.author, 2):

                await client.say ("Your are not allowed to access this command!")
                return

            if perms.check(userName2, 2):

                await client.say ("Your are not allowed to ban this user!")
                return

            ban_msg = userName2.mention + " has been banned, due to violation of the rules in " + CHANNEL_RULES
            await client.say(ban_msg)
            await client.ban(userName2, delete_message_days=7)
            await client.unban(userName2.server, userName2)
            print('Ban was executed!')




@client.event
async def on_ready():

    await client.change_presence(game=Game(name="!help"))

    print('Eingeloggt als')
    print(client.user.name)
    print(client.user.id)
    print('-----------')


@client.event
async def on_member_join(member):
    channel = member.server.get_channel(WELCOME_CHANNEL_ID)
    message = 'Herzlich Willkommen/Welcome {0} Please read the rules in '+ CHANNEL_RULES + ' Call me if you need **!help** :blush:'

    await client.send_message(channel, message.format(member.mention))

# @client.event
# async def on_member_remove(member):
#     channel = member.server.get_channel(WELCOME_CHANNEL_ID)
#     message = '{0} has left us, for now...'
#
#     await client.send_message(channel, message.format(member.mention))







client.run(TOKEN)