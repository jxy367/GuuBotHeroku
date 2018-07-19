import discord
import asyncio
import random
from datetime import datetime
from pytz import timezone
import os
import urllib
from urllib import request
from urllib import parse
from bs4 import BeautifulSoup
#import youtube_dl
import time
import re

#API_KEY = os.environ.get('API_KEY')
TOKEN = os.environ.get('TOKEN')
#TOKEN = 'NDM4ODkyMDQ3MDM5MDcwMjE4.DcLNng.AbGD6jAOyNo5JIgadsgR3rI_3Wc'

client = discord.Client()

# Guu Messages #
woo = 'Woo'
my_woo = 'Woo.. Woo.. Woo.. Nom.'
multi_woo = 'Woo.. Woo.. Woo..'
wu = "Wu"
awoo = "Awoo.. Awoo.. Awoo.."
woop = "Woop Woop, pull over that ass is too fat"
nico = "Nico Nico No"
morning = "It's morning!"
conan = "At least the ice will melt..."
malt_shop = "To the malt shop."
fire = 'We should have guubot fire on "freaked it" - Danny Miles'
despacito = 'https://www.youtube.com/watch?v=kJQP7kiw5Fk'

# Guu Embeds #
woo_embed = discord.Embed()
woo_embed.set_image(
    url='https://78.media.tumblr.com/924178ff9e2b7d99446ecd124e3bf1ed/tumblr_nri6gbXrfC1tsmbjio2_250.gif')

wu_embed1 = discord.Embed()
wu_embed1.set_image(
    url='https://cdn.discordapp.com/attachments/191988856839602176/438907914552475660/oRV3vC6E_400x400.png')

wu_embed2 = discord.Embed()
wu_embed2.set_image(url='https://scontent.fbkl1-1.fna.fbcdn.net/v/t31.0-8/23004588_1807971082834301_9153680533274895689_o.jpg?_nc_cat=0&_nc_eui2=v1%3AAeGbnqhaXMf0xOFb0HZWvNxBvC9lIuEiS6m55S2E46FofIaAOfmLtipA3BDKkom43pF3sG8tDppkxbPQ5ICnJu_ABx2iC2JuDxzjYFpDUMKj3A&oh=5b4fc35b2c43bea5283ad315def59e64&oe=5B68987A')

wu_embed3 = discord.Embed()
wu_embed3.set_image(url='https://scontent.fbkl1-1.fna.fbcdn.net/v/t1.0-9/16711577_1691924731105604_448770579254912570_n.jpg?_nc_cat=0&_nc_eui2=v1%3AAeGNWyFqGgPHbBoPqljpVJZlyTSNI298EMfHoR3p_m7g94Apj4VqpCoN_Ya7vh7sz8V1o4K4Vr6nudMcUWW9DRnv1NxHWYTAXpEoFTYworEGKQ&oh=383f61bc9566164c2aad0d0a64cb5d83&oe=5B6712C6')

awoo_embed1 = discord.Embed()
awoo_embed1.set_image(url='http://i0.kym-cdn.com/photos/images/newsfeed/001/175/124/112.gif')

awoo_embed2 = discord.Embed()
awoo_embed2.set_image(url='https://i.imgur.com/FXSNNQa.gif')

woop_embed = discord.Embed()
woop_embed.set_image(url='https://media.giphy.com/media/zPSkALwMfE72U/giphy.gif')

nico_embed = discord.Embed()
nico_embed.set_image(url='http://i0.kym-cdn.com/photos/images/newsfeed/001/205/802/99e.gif')

nora_morning = discord.Embed()
nora_morning.set_image(url='https://media1.tenor.com/images/bbb22e19dd5fbdf57982bf6efe026f32/tenor.gif')

conan_embed = discord.Embed()
conan_embed.set_image(url='https://i.imgur.com/bFE5wR9.jpg')

malt_shop_embed = discord.Embed()
malt_shop_embed.set_image(url='https://media.discordapp.net/attachments/216304922025525248/450292196562960395/latest.png')

fire_embed = discord.Embed()
fire_embed.set_image(url='https://i.gifer.com/MRnP.gif')

sheik_embed = discord.Embed()
sheik_embed.set_image(url='https://i.imgur.com/kL7DF.gif')

fair_embeds = []
fair_urls = ['http://www.pensacolafair.com/wp-content/themes/wp-responsive110/scripts/timthumb.php?src=http://www.pensacolafair.com/wp-content/uploads/2012/11/midway-night-600x400.jpg&w=600&h=400&zc=1',
        'https://myareanetwork-photos.s3.amazonaws.com/editorphotos/f/26657_1520825140.png',
        'https://media1.fdncms.com/clevescene/imager/u/original/9012469/ohio_state_fair_-_readingandlearning_instagram.png',
        'https://media.nbcwashington.com/images/652*367/fairgrounds071017.jpg',
        'https://d3m7xw68ay40x8.cloudfront.net/assets/2016/10/14163048/1016-state-fair.jpg',
        'http://www.stratfordagriculturalsociety.com/wp-content/uploads/2015/09/FB-Fair-pic.jpg',
        'https://scontent.fbkl1-1.fna.fbcdn.net/v/t31.0-8/11148833_10153519083058322_8334046223350439297_o.jpg?_nc_cat=0&oh=7c835a3f739107548538ca894c06a507&oe=5B9A73E2',
        'https://upload.wikimedia.org/wikipedia/commons/b/b7/L.A._County_Fair_1262.jpg',
        'https://www.gannett-cdn.com/-mm-/c0059ff26d6046b65292170ffc20f75e93874fea/c=0-261-3396-2180&r=x1683&c=3200x1680/local/-/media/2016/10/17/Phoenix/Phoenix/636122964086278930-Arizona-State-Fair-20.jpg',
        'http://www.effinghamcountyfair.com/wp-content/uploads/2014/12/county-fair.jpg',
        'https://i.ytimg.com/vi/2yVeQRcOTi4/maxresdefault.jpg',
        'http://www.lancasterfair.com/wp-content/uploads/2017/01/44.jpg']

noah_morning_embed = discord.Embed()
noah_morning_embed.set_image(url='https://cdn.discordapp.com/attachments/239214414132281344/468755357200809984/image.jpg')

for url in fair_urls:
    new_embed = discord.Embed()
    new_embed.set_image(url=url)
    fair_embeds.append(new_embed)

mr_dictionary = {}
playlist_dictionary = {}

on_cooldown = {}
cooldown_time = 10

noah_cooldown = False
# Server specific ids
# Channels
venting_channel = 400096015740567552
main_channel = 239214414132281344
TS_channel = 405046053809946647
voice_text_channel = 455118686315872257

# emojis
expand1 = 459124362075832320
expand2 = 459124362063118336
expand3 = 459124362004529173
expand4 = 459124361698213890

# Bots
nicer_completion_bot = 439346446697889792

# People
me = 191797757357457408
julian = 185940933160730624
kaius = 115589615603286024
kolson = 316041338862829569
riley = 306997179367555074
danny = 191426236935831552
esther = 145075344095969281
noah = 165481032043331584

# Voice stuff
#discord.opus.load_opus('libopus-0.dll')
#with youtube_dl.YoutubeDL() as ydl:
#    ydl.download()

def exactly_in(str1: str, str2: str):  # str1 exactly in str2
    index = str2.find(str1)
    len_str1 = len(str1)

    if index < 0:
        return False

    if index + len_str1 < len(str2):
        next_char = str2[index + len_str1]
        if next_char.isalnum():
            return False

    if index > 0:
        past_char = str2[index - 1]
        if past_char.isalnum():
            return False

    return True


def at_end_of(str1: str, str2: str):
    index = str2.find(str1)
    len_str1 = len(str1)

    if index < 0:  # str1 not in str 2
        return False

    if index + len_str1 < len(str2):  # str1 is in str2 but not necessarily at end
        next_char_index = index + len_str1
        while next_char_index < len(str2):
            if str2[next_char_index].isalnum():
                return False
            next_char_index += 1

    if index > 0:
        if str2[index - 1].isalnum():
            return False

    return True


def str1_star_str2(str1: str, str2: str, str3: str):
    if not exactly_in(str1, str3) or not at_end_of(str2, str3):
        return False
    else:
        index = str2.find(str1)
        len_str1 = len(str1)
        return exactly_in(str2, str3[index+len_str1:])


def request_youtube_video(keyword: str):
    start = time.time()
    query = urllib.parse.quote(keyword)
    quote_finished = time.time()
    url = "https://www.youtube.com/results?search_query=" + query
    url_made = time.time()
    response = urllib.request.urlopen(url)
    response_received = time.time()
    html = response.read()
    response_read = time.time()
    soup = BeautifulSoup(html, 'html.parser')
    soup_made = time.time()

    for vid in soup.findAll(attrs={'class': 'yt-uix-tile-link'}):
        video_url = 'https://www.youtube.com' + vid['href']
        find_index = video_url.find('https://www.youtube.com/watch')
        if find_index == 0:
            return video_url

    print("Returning despacito")
    return despacito


async def reset_display_name():
    for changed_guild in client.guilds:
        if changed_guild.me.display_name != "GuuBot":
            print(changed_guild.name)
            print(changed_guild.me.display_name)
            print("---")
            await changed_guild.me.edit(nick=None)


async def reset_noah_cooldown():
    global noah_cooldown
    est = timezone('EST')
    today = datetime.now().astimezone(est)
    if today.hour == 5 and today.minute == 0:
        noah_cooldown = True


async def background_update():
    await client.wait_until_ready()
    while not client.is_closed():
        await reset_display_name()
        await reset_noah_cooldown()
        await asyncio.sleep(60)


async def cooldown():
    global on_cooldown
    await client.wait_until_ready()
    while not client.is_closed():
        for guild in on_cooldown:
            on_cooldown[guild] = on_cooldown[guild] - 1
            if on_cooldown[guild] < 0:
                on_cooldown[guild] = 0
        await asyncio.sleep(1)


async def await_message(message, content=None, embed=None):
    global on_cooldown
    global cooldown_time

    if content is None:
        await message.channel.send(embed=embed)
    elif embed is None:
        await message.channel.send(content=content)
    else:
        await message.channel.send(content=content, embed=embed)

    if message.guild is not None:
        guild_id = message.guild
    else:
        guild_id = message.channel.id
    on_cooldown[guild_id] = cooldown_time


async def await_channel(channel, content=None, embed=None):
    global on_cooldown
    if channel is not None:
        if content is None:
            await channel.send(embed=embed)
        elif embed is None:
            await channel.send(content=content)
        else:
            await channel.send(content=content, embed=embed)
        if channel.guild is not None:
            on_cooldown[channel.guild] = True
        else:
            on_cooldown[channel.id] = True

@client.event
async def on_message(message):
    global mr_dictionary
    global on_cooldown

    guild_id = message.guild
    if guild_id is None:
        guild_id = message.channel.id
    if guild_id not in on_cooldown:
        on_cooldown[guild_id] = 0

    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.author.bot:
        if message.author.id == nicer_completion_bot:  # Nicer Completion Bot | Nicer Completion Bot Winning
            if "And then everyone important died." in message.content:
                members = message.guild.members
                print(members)
                for member in members:
                    if not member.bot:
                        mr_dictionary[member.id] = (member.roles, member.nick)
                        await message.guild.kick(message.author)
                await await_message(message, content="Have Fun Noah")
                print(mr_dictionary)
            else:
                return
        else:
            return

    try:
        mr_dictionary[message.author.id] = (message.author.roles, message.author.nick)
    except AttributeError:
        pass

    guild_cooldown = on_cooldown[guild_id] <= 0
    if not guild_cooldown:
        return

    if message.channel.id == venting_channel:
        return

    guu_bot_select = 0
    if guu_bot_select == 0:
        # Figure out if version of "let's go" is in the message
        lets_go_found = False
        for lets in ["let's", "lets", "let" + u"\u2019" + "s"]:
            if not lets_go_found:
                if str1_star_str2(lets, "go", message.content.lower()):
                    #await await_message(message=message, content=malt_shop, embed=malt_shop_embed)
                    lets_go_found = True

        # Check if "fair" appears in message
        exact_fair = exactly_in("fair", message.content.lower())

        if "awoo" in message.content.lower():

            awoo_select = random.randrange(0, 4)

            if awoo_select < 3:
                await await_message(message=message, content=awoo, embed=awoo_embed1)
            elif awoo_select == 4:
                await await_message(message=message, content=awoo, embed=awoo_embed2)
            else:
                await await_message(message=message, content=awoo, embed=awoo_embed1)

        elif "woo" in message.content.lower():

            exact_woo = exactly_in("woo", message.content.lower())

            if exact_woo:
                if message.author.id == me:
                    await await_message(message=message, content=my_woo, embed=woo_embed)

                elif message.author.id == julian:
                    wu_option_select = random.randrange(0, 6)
                    if wu_option_select == 0:
                        await  await_message(message=message, content=wu, embed=wu_embed1)
                    elif wu_option_select == 1:
                        await  await_message(message=message, content=wu, embed=wu_embed2)
                    elif wu_option_select == 2:
                        await  await_message(message=message, content=wu, embed=wu_embed3)
                    else:
                        await  await_message(message=message, content=multi_woo, embed=woo_embed)

                elif message.author.id == kaius:
                    kaius_select = random.randrange(0, 2)
                    if kaius_select == 0:
                        await await_message(message=message, content=woop, embed=woop_embed)
                    else:
                        await await_message(message=message, content=multi_woo, embed=woo_embed)

                elif message.author.id == riley:
                    riley_select = random.randrange(0, 2)
                    if riley_select == 0:
                        await await_message(message=message, content=woop, embed=woop_embed)
                    else:
                        await await_message(message=message, content=multi_woo, embed=woo_embed)

                else:
                    await await_message(message=message, content=multi_woo, embed=woo_embed)

            else:
                await await_message(message=message, content=woo, embed=woo_embed)

        elif exact_fair:
            index = random.randrange(0, len(fair_embeds))
            if message.author.id == danny:  # Danny
                danny_select = random.randrange(0, 2)
                if danny_select == 0:
                    await await_message(message=message, embed=sheik_embed)
                else:
                    await await_message(message=message, embed=fair_embeds[index])
            else:
                await await_message(message=message, embed=fair_embeds[index])

        elif "pasta" in message.content.lower():
            if message.author.id == kolson:
                new_invite = await message.channel.create_invite(max_uses=1)
                user = client.get_user(message.author.id)
                await user.send(content=new_invite)
                await await_message(message=message, content='He said "pasta"! SWING THE BAN HAMMER!')
                await message.guild.kick(message.author)
                await await_message(message=message, content='Fine. Just the kick hammer...')

        elif "nico" in message.content.lower():
            await await_message(message=message, content=nico, embed=nico_embed)

        elif "secret" in message.content.lower() and "woman" in message.content.lower():
            await await_message(message=message, content=conan, embed=conan_embed)

        elif lets_go_found:
            await await_message(message=message, content=malt_shop, embed=malt_shop_embed)

        elif "freaked it" in message.content.lower():
            await await_message(message=message, content=fire, embed=fire_embed)

        elif "nora" in message.content.lower():
            est = timezone('EST')
            today = datetime.now().astimezone(est)
            if today.hour < 12:
                await await_message(message=message, content=morning, embed=nora_morning)

        elif "@someone" in message.content.lower():
            await await_message(message=message, content="^ "+message.author.mention)

        elif "guubot play " in message.content.lower():
            play_url = ""
            if message.author.id == noah:
                noah_select = random.randrange(0, 10)
                if noah_select == 0:
                    play_url = request_youtube_video("barbie girl")
                    await await_message(message=message, content=play_url)
                else:
                    play_url = request_youtube_video(
                        message.content.lower()[message.content.lower().find("guubot play ") + len("guubot play "):])
                    await await_message(message=message, content=play_url)

            else:
                play_url = request_youtube_video(
                        message.content.lower()[message.content.lower().find("guubot play ") + len("guubot play "):])
                await await_message(message=message, content=play_url)

            #if message.channel.id == TS_channel:


        elif "sad" == message.content.lower() or "sad!" == message.content.lower():
            if message.author.id == noah:
                await await_message(message=message, content="Smile\nSweet\nSister\nSadistic\nSurprise\nService")

        elif message.content.lower().find("roll ") == 0:
            roll_string = "Input was not acceptable"
            message_string = message.content
            modifier_matching = re.compile('roll \d+d\d+ *[-+] *\d* *', re.IGNORECASE)
            modifier_match = modifier_matching.match(message_string)
            find_digits = re.compile('\d+')
            if modifier_match is None:
                # Try basic matching
                basic_matching = re.compile('roll \d+d\d+ *', re.IGNORECASE)
                basic_match = basic_matching.match(message_string)
                if basic_match is None:
                    x = 0

                elif basic_match.end() != len(message_string):
                    print(str(basic_match.end())+","+str(len(message_string)))

                else:
                    # continue with basic matching
                    numeric_values = find_digits.findall(message_string)
                    assert len(numeric_values) == 2
                    number_of_rolls = int(numeric_values[0])
                    number_of_sides = int(numeric_values[1])
                    if number_of_rolls < 1 or number_of_sides < 1:
                        roll_string = "At least one of the values is less than 1"

                    elif number_of_rolls > 100 or number_of_sides > 100:
                        roll_string = "At least one of the values is greater than 100"

                    else:
                        dice_list = []
                        for num in range(0, number_of_rolls):
                            dice_list.append(random.randrange(1, number_of_sides+1))

                        roll_string = "Dice values: " + str(dice_list)[1:-1] + "\nSum: " + str(sum(dice_list))

            elif modifier_match.end() != len(message_string):
                print(str(modifier_match.end()) + "," + str(len(message_string)))

            else:
                # continue with modifier matching
                assert "+" in message_string or "-" in message_string

                modifier_symbol = "+" in message_string
                modifier_as_multiplier = 2 * int(modifier_symbol) - 1

                numeric_values = find_digits.findall(message_string)
                assert len(numeric_values) == 3
                number_of_rolls = int(numeric_values[0])
                number_of_sides = int(numeric_values[1])
                modifier = int(numeric_values[2])
                if number_of_rolls < 1 or number_of_sides < 1:
                    roll_string = "At least one of the values is less than 1"

                elif number_of_rolls > 100 or number_of_sides > 100:
                    roll_string = "At least one of the values is greater than 100"

                else:
                    dice_list = []
                    for num in range(0, number_of_rolls):
                        dice_list.append(random.randrange(1, number_of_sides + 1))

                    roll_string = "Dice values: " + str(dice_list)[1:-1] + "\nSum: " + str(sum(dice_list)) \
                                  + "\nModifier: " + str(modifier_as_multiplier * modifier) + "\nFinal value: " \
                                  + str(sum(dice_list) + modifier*modifier_as_multiplier)

            await await_message(message=message, content=roll_string)

        else:
            x = 0


@client.event
async def on_message_edit(before, after):
    if not exactly_in("fair", before.content.lower()) and exactly_in("fair", after.content.lower()):
        index = random.randrange(0, len(fair_embeds))
        await await_message(message=after, embed=fair_embeds[index])

@client.event
async def on_member_update(before, after):
    global noah_cooldown
    if before.id == noah:
        if noah_cooldown:
            if before.status != after.status and after.status == discord.Status.online:
                noah_user = client.get_user(noah)
                dm_channel = noah_user.dm_channel
                if dm_channel is None:
                    dm_channel = await noah_user.create_dm()
                await await_channel(channel=dm_channel, embed=noah_morning_embed)
                noah_cooldown = False


@client.event
async def on_reaction_add(reaction, user):
    global expand1
    global expand2
    global expand3
    global expand4
    message = reaction.message
    expand1_id = 459124362075832320
    if expand1 is None:
        expand1 = client.get_emoji(459124362075832320)
        expand2 = client.get_emoji(459124362063118336)
        expand3 = client.get_emoji(459124362004529173)
        expand4 = client.get_emoji(459124361698213890)

    if isinstance(reaction.emoji, str):
        pass

    elif reaction.emoji.id == expand1_id:
        await message.add_reaction(expand1)
        await message.add_reaction(expand2)
        await message.add_reaction(expand3)
        await message.add_reaction(expand4)

    else:
        pass

@client.event
async def on_member_join(member):
    global client
    global mr_dictionary
    if member.id in mr_dictionary.keys():
        roles, nickname = mr_dictionary[member.id]
        await member.edit(nick=nickname, roles=roles)


@client.event
async def on_ready():
    global expand1
    global expand2
    global expand3
    global expand4
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    client.loop.create_task(background_update())
    client.loop.create_task(cooldown())
    expand1 = client.get_emoji(expand1)
    expand2 = client.get_emoji(expand2)
    expand3 = client.get_emoji(expand3)
    expand4 = client.get_emoji(expand4)

client.run(TOKEN)


