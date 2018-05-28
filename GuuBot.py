import discord
import asyncio
import random
from datetime import datetime
from pytz import timezone
#import urllib as ul
#import base64
#from google.cloud import vision
#from google.cloud.vision import types


TOKEN = 'NDM4ODkyMDQ3MDM5MDcwMjE4.DcLNng.AbGD6jAOyNo5JIgadsgR3rI_3Wc'

client = discord.Client()

# Guu Messages #
woo = 'Woo'
my_woo = 'Woo.. Woo.. Woo.. Nom.'
multi_woo = 'Woo.. Woo.. Woo..'
wu = "Wu"
awoo = "Awoo.. Awoo.. Awoo.."
woop = "Woop Woop, pull over that ass is too fat"
nico = "Nico Nico No"
boop = "Boop"
morning = "It's morning!"
conan = "At least the ice will melt..."
malt_shop = "To the malt shop."

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

nora_urls = ['http://i.imgur.com/sHlntIg.gif',
             'https://orig00.deviantart.net/15ae/f/2016/184/8/c/rwby_chibi_episode_8_nora_s_inflation_by_bittyheart-da8mail.gif',
             'https://media1.tenor.com/images/a4e275e68373678a11b0ba56a47ce9d9/tenor.gif?itemid=7880758',
             'https://i.imgur.com/sizNJ7o.gif',
             'https://78.media.tumblr.com/d5fffbbbd9e9d0cf0e8ef425aea5a50a/tumblr_mvyn1hGPhJ1sjxjt0o1_500.gif']

nora_embeds = []
for nora_url in nora_urls:
    nora_embed = discord.Embed()
    nora_embed.set_image(url=nora_url)
    nora_embeds.append(nora_embed)

nora_morning = discord.Embed()
nora_morning.set_image(url='https://media1.tenor.com/images/bbb22e19dd5fbdf57982bf6efe026f32/tenor.gif')

conan_embed = discord.Embed()
conan_embed.set_image(url='https://i.imgur.com/bFE5wR9.jpg')

malt_shop_embed = discord.Embed()
malt_shop_embed.set_image(url='https://media.discordapp.net/attachments/216304922025525248/450292196562960395/latest.png')

mr_dictionary = {}


def exactly_in(str1: str, str2: str):  # str1 exactly in str2
    index = str2.find(str1)
    len_str1 = len(str1)
    #print(str(index) + "," + str(len_str1))
    if index < 0:
        return False

    if index + len_str1 < len(str2):
        next_char = str2[index + len_str1]
        if next_char.isalnum():
            #return exactly_in(str1, str2[:index] + str2[index+len_str1:])
            return False

    if index > 0:
        past_char = str2[index - 1]
        if past_char.isalnum():
            #return exactly_in(str1, str2[:index] + str2[index + len_str1:])
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
    #print(str1)
    #print(str(exactly_in(str1, str3)) + "," + str(at_end_of(str2, str3)))
    if not exactly_in(str1, str3) or not at_end_of(str2, str3):
        return False
    else:
        index = str2.find(str1)
        len_str1 = len(str1)
        return exactly_in(str2, str3[index+len_str1:])


async def reset_display_name():
    for changed_guild in client.guilds:
        if changed_guild.me.display_name != "GuuBot":
            print(changed_guild.name)
            print(changed_guild.me.display_name)
            print("---")
            await changed_guild.me.edit(nick=None)


async def background_update():
    await client.wait_until_ready()
    while not client.is_closed():
        await reset_display_name()
        await asyncio.sleep(60)


@client.event
async def on_message(message):
    global mr_dictionary
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.author.bot:
        if message.author.id == 439346446697889792:  # Nicer Completion Bot | Nicer Completion Bot Winning
            if "And then everyone important died." in message.content:
                members = message.guild.members
                print(members)
                for member in members:
                    if not member.bot:
                        mr_dictionary[member.id] = (member.roles, member.nick)
                        await message.guild.kick(message.author)
                await message.channel.send(content="Have Fun Noah")
                print(mr_dictionary)
            else:
                return
        else:
            return

    mr_dictionary[message.author.id] = (message.author.roles, message.author.nick)

    #url = message.image
    #google_vision_request(url)

    if "awoo" in message.content.lower():
        awoo_select = random.randrange(0, 4)
        if awoo_select < 3:
            await message.channel.send(content=awoo, embed=awoo_embed1)
        elif awoo_select == 4:
            await message.channel.send(content=awoo, embed=awoo_embed2)
        else:
            await message.channel.send(content=awoo, embed=awoo_embed1)

    elif "woo" in message.content.lower():

        exact_woo = exactly_in("woo", message.content.lower())

        if exact_woo:
            if message.author.id == 191797757357457408:  # Me
                await message.channel.send(content=my_woo, embed=woo_embed)

            elif message.author.id == 185940933160730624:  # Julian
                wu_option_select = random.randrange(0, 6)
                if wu_option_select == 0:
                    await  message.channel.send(content=wu, embed=wu_embed1)
                elif wu_option_select == 1:
                    await  message.channel.send(content=wu, embed=wu_embed2)
                elif wu_option_select == 2:
                    await  message.channel.send(content=wu, embed=wu_embed3)
                else:
                    await  message.channel.send(content=multi_woo, embed=woo_embed)

            elif message.author.id == 165481032043331584:  # noah
                noah_select = random.randrange(0, 10)
                user = client.get_user(message.author.id)
                if noah_select == 0:
                    msg = "You said it was okay"
                    for num in range(0, 20):
                        await user.send(content=msg)

                elif noah_select == 1:
                    await user.send(content="I have Mercy, for now. (McCree took a day off)")

                elif noah_select == 2:
                    await user.send(content="In case you haven't noticed, I changed the likelihood of getting spammed")

                elif noah_select == 3:
                    await user.send(content="In case you haven't noticed, I changed the likelihood of getting spammed")
                    for num in range(0, 10):
                        await user.send(content="spammed")

                else:
                    await message.channel.send(content=multi_woo, embed=woo_embed)

            elif message.author.id == 115589615603286024:  # Kaius
                kaius_select = random.randrange(0, 2)
                if kaius_select == 0:
                    await message.channel.send(content=woop, embed=woop_embed)
                else:
                    await message.channel.send(content=multi_woo, embed=woo_embed)

            elif message.author.id == 306997179367555074:  # Riley
                riley_select = random.randrange(0, 2)
                if riley_select == 0:
                    await message.channel.send(content=woop, embed=woop_embed)
                else:
                    await message.channel.send(content=multi_woo, embed=woo_embed)

            else:
                await message.channel.send(content=multi_woo, embed=woo_embed)

        else:
            await message.channel.send(content=woo, embed=woo_embed)

    else:
        x = 0

    if "pasta" in message.content.lower():
        if message.author.id == 316041338862829569:  # Kolson
            new_invite = await message.channel.create_invite(max_uses=1)
            user = client.get_user(message.author.id)
            await user.send(content=new_invite)
            ban_msg = 'He said "pasta"! SWING THE BAN HAMMER!'
            await message.channel.send(ban_msg)
            await message.guild.kick(message.author)
            kick_msg = 'Fine. Just the kick hammer...'
            await message.channel.send(kick_msg)

        #if message.author.id == 191797757357457408:  # Me
        #    await message.channel.send("pasta")
        #    new_invite = await message.channel.create_invite(max_uses=1)
        #    user = client.get_user(message.author.id)
        #    await user.send(content=new_invite)

    if "nico" in message.content.lower():
        await message.channel.send(content=nico, embed=nico_embed)

    if "nora" in message.content.lower():
        est = timezone('EST')
        today = datetime.now().astimezone(est)
        if today.hour < 12:
            await message.channel.send(content=morning, embed=nora_morning)
        else:
            nora_select = random.randrange(0, len(nora_embeds))
            if nora_select == len(nora_embeds):
                nora_select = nora_select - 1
            await message.channel.send(content=boop, embed=nora_embeds[nora_select])

    if "secret" in message.content.lower() and "woman" in message.content.lower():
        await message.channel.send(content=conan, embed=conan_embed)

    #if at_end_of("let's go", message.content.lower()) or at_end_of("lets go", message.content.lower()) \
    #        or at_end_of("let" + u"\u2019" + "s go", message.content.lower()):
    #    await message.channel.send(content=malt_shop, embed=malt_shop_embed)

    lets_go_found = False
    for lets in ["let's", "lets", "let" + u"\u2019" + "s"]:
        if not lets_go_found:
            if str1_star_str2(lets, "go", message.content.lower()):
                await message.channel.send(content=malt_shop, embed=malt_shop_embed)
                lets_go_found = True

#def google_vision_request(url: str):
    # Instantiates a client
#    google_client = vision.ImageAnnotatorClient()

    # Get image_url data and encode
#    contents = ul.urlopen(url).read()

    # Prepare data for detection
#    data = base64.b64encode(contents)
#    image = types.Image(content=data)

    # Performs label detection on the image file
#    response = google_client.web_entity_detection(image=image)
#    entities = response.web_entity_annotations
#    return entities


@client.event
async def on_member_join(member):
    global client
    global mr_dictionary
    if member.id in mr_dictionary.keys():
        roles, nickname = mr_dictionary[member.id]
        await member.edit(nick=nickname, roles=roles)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    client.loop.create_task(background_update())

client.run(TOKEN)
