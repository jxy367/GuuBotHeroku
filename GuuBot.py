import asyncio
import os
import random
import re
import time
import urllib
import json
import base64
from datetime import datetime
from itertools import permutations
from multiprocessing.dummy import Pool
# from time import sleep
from urllib import parse
from urllib import request

import discord
import requests
from bs4 import BeautifulSoup
from discord.ext import commands
from pytz import timezone

# Own class
from RPS import *

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options

API_KEY = os.environ.get('API_KEY')
TOKEN = os.environ.get('TOKEN')

# GOOGLE_CHROME_BIN = os.environ.get('GOOGLE_CHROM_BIN')
# CHROMEDRIVER_PATH = os.environ.get('CHROMEDRIVER_PATH')

client = commands.Bot(command_prefix="guubot ", case_insensitive=True)

# Configure Chromedriver
# chrome_options = Options()
# chrome_options.binary_location = GOOGLE_CHROME_BIN
# chrome_options.add_argument('--disable-gpu')
# chrome_options.add_argument('--no-sandbox')
# driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, options=chrome_options)

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
malt_shop = "To the malt shop!!"
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
wu_embed2.set_image(
    url='https://scontent.fbkl1-1.fna.fbcdn.net/v/t31.0-8/23004588_1807971082834301_9153680533274895689_o.jpg?_nc_cat=0&_nc_eui2=v1%3AAeGbnqhaXMf0xOFb0HZWvNxBvC9lIuEiS6m55S2E46FofIaAOfmLtipA3BDKkom43pF3sG8tDppkxbPQ5ICnJu_ABx2iC2JuDxzjYFpDUMKj3A&oh=5b4fc35b2c43bea5283ad315def59e64&oe=5B68987A')

wu_embed3 = discord.Embed()
wu_embed3.set_image(
    url='https://scontent.fbkl1-1.fna.fbcdn.net/v/t1.0-9/16711577_1691924731105604_448770579254912570_n.jpg?_nc_cat=0&_nc_eui2=v1%3AAeGNWyFqGgPHbBoPqljpVJZlyTSNI298EMfHoR3p_m7g94Apj4VqpCoN_Ya7vh7sz8V1o4K4Vr6nudMcUWW9DRnv1NxHWYTAXpEoFTYworEGKQ&oh=383f61bc9566164c2aad0d0a64cb5d83&oe=5B6712C6')

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
malt_shop_embed.set_image(
    url='https://media.discordapp.net/attachments/216304922025525248/450292196562960395/latest.png')

fire_embed = discord.Embed()
fire_embed.set_image(url='https://media.giphy.com/media/5a6Y7Fe0TT50Q/giphy.gif')

sheik_embed = discord.Embed()
sheik_embed.set_image(url='https://i.imgur.com/kL7DF.gif')

powerful_embed = discord.Embed()
powerful_embed.set_image(url="https://i.ytimg.com/vi/4DFsaVdQstE/maxresdefault.jpg")

almost_like_embed = discord.Embed()
almost_like_embed.set_image(
    url="http://memeshappen.com/media/created/omg-its-almost-like--i-don39t-even-care-meme-18321.jpg")

ye_embed = discord.Embed()
ye_embed.set_image(url="https://i.ytimg.com/vi/-HXcxGnmiSI/maxresdefault.jpg")

something_something_embed = discord.Embed()
something_something_embed.set_image(
    url="https://vignette.wikia.nocookie.net/familyguy/images/8/89/Bscap0524.jpg/revision/latest?cb=20100110115057")

bad_embed = discord.Embed()
bad_embed.set_image(url="https://cdn.shopify.com/s/files/1/0018/7639/4036/products/12_1200x1200.jpg?v=1524333747")

coded_embed = discord.Embed()
coded_embed.set_image(url="https://upload.wikimedia.org/wikipedia/en/8/8e/Kingdom_Hearts_coded_logo.png")

vc_embed = discord.Embed()
vc_embed.set_image(url="https://cdn.discordapp.com/attachments/216304922025525248/501182690524135435/unknown.png")

you_died_embed = discord.Embed()
you_died_embed.set_image(
    url="https://boygeniusreport.files.wordpress.com/2016/04/dark_souls_you_died.jpg?quality=98&strip=all&w=782")
# "https://vignette.wikia.nocookie.net/darksouls/images/6/63/You-Died.jpg/revision/latest?cb=20130515050459"

faker_embed = discord.Embed()
faker_embed.set_image(url="https://cdn.discordapp.com/attachments/443065453896531968/535562120817803268/image.jpg")

fair_embeds = []
fair_urls = [
    'http://www.pensacolafair.com/wp-content/themes/wp-responsive110/scripts/timthumb.php?src=http://www.pensacolafair.com/wp-content/uploads/2012/11/midway-night-600x400.jpg&w=600&h=400&zc=1',
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

for url in fair_urls:
    new_embed = discord.Embed()
    new_embed.set_image(url=url)
    fair_embeds.append(new_embed)

take_embeds = []
take_urls = ['https://i.ytimg.com/vi/xvXh2NDE6iM/maxresdefault.jpg',  # hot shake
             'http://cdn-webimages.wimages.net/05154eed87de00290048db240e69fe77b94fda-wm.jpg?v=3',  # hot ache
             'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTxTB9Jz6gSPri9l7bJ23fjCE6AYU9vOtqnuAlaY99uLuV-6okU',
             # hot bake
             'https://i.ytimg.com/vi/7-kcnEPhJGY/maxresdefault.jpg',  # hot blake
             'http://carphotos.cardomain.com/story_images/1/1955/3521/4886760001_large.jpg',  # hot break
             'http://www.hummingbrew.com/uploads/7/6/4/7/7647871/5739699_orig.jpg',  # hot break
             'https://www.japanesecooking101.com/wp-content/uploads/2017/08/DSC00083-copy.jpg',  # hot cake
             'https://i.pinimg.com/originals/32/a0/c2/32a0c2830e93f3d57cb302884e096288.jpg',  # hot drake
             'https://i5.walmartimages.com/asr/1d23e86b-dda0-47c6-8995-b5cdb076f1c7_1.1fb0c60d61b11936725881f4b94eb799.jpeg?odnHeight=560&odnWidth=560&odnBg=FFFFFF',
             # hot flake
             'https://www.bascofinefoods.com/spanish-recipes-wpfiles/wp-content/uploads/2014/09/crispy_hake_with_piquillo_peppers-e1505676037705.jpg',
             # hot hake
             'https://i.ytimg.com/vi/NeW6MQ0bIRQ/maxresdefault.jpg',  # hot jake
             'https://i.ytimg.com/vi/3qGxG5P1-Ro/maxresdefault.jpg',  # hot lake
             'http://www.sciencemag.org/sites/default/files/styles/article_main_large/public/images/sn-seismicH.jpg?itok=I-6a0Sri',
             # hot quake
             'http://www.doityourselfrv.com/wp-content/uploads/2013/07/campfire-hotdogs-rake.jpg',  # hot rake
             'https://images.reverb.com/image/upload/s--up0dQ8AK--/a_exif,c_limit,e_unsharp_mask:80,f_auto,fl_progressive,g_south,h_620,q_90,w_620/v1490375727/tzc0ozcn2pmkcwyii6qj.jpg',
             # hot sake
             'https://www.detectiveconanworld.com/wiki/images/thumb/2/20/EP106_Case.jpg/290px-EP106_Case.jpg',
             # hot slake
             'https://subpop-img.s3.amazonaws.com/asset/artist_images/attachments/000/007/225/max_960/hotsnakes-2017-promo-02-courtesyoftheartist-2667x1500-300.jpg?1516298549',
             # hot snake
             'http://1000awesomethings.com/wp-content/uploads/2009/11/grilled-steak.jpg',  # hot steak
             ]

for url in take_urls:
    new_embed = discord.Embed()
    new_embed.set_image(url=url)
    take_embeds.append(new_embed)

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

# Servers
TS = 405046053809946644
EnergylessZone = 528382529502314521

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
mark = 213097197456064512
miguel = 385306442439065601

# RPS Data
rps_game = None

# Quiz Data
quiz_data = {}
quiz_roles = []
with open("QuizData.txt", 'r') as f:
    mod = 5
    count = 0
    question_data = {}
    for line in f:
        if count == 0:
            question_data["role"] = line.strip()
            quiz_roles.append(line.strip())
        elif count == 1:
            question_data["question"] = line.strip()[3:]
        elif count == 2:
            question_data["hint"] = line.strip()[3:]
        elif count == 3:
            question_data["answer"] = line.strip()[3:]
        else:
            quiz_data[question_data["role"]] = question_data
            question_data = {}
        count += 1
        count = count % mod

quiz_roles.append("Winner")

magic_8ball_responses = []
magic_guuball_responses = []

with open("Magic8BallResponses",'r') as f:
    for line in f:
        magic_8ball_responses.append(line.strip())

with open("MagicGuuBallResponses",'r') as f:
    for line in f:
        magic_guuball_responses.append(line.strip())

# Voice stuff
# discord.opus.load_opus('libopus-0.dll')
# with youtube_dl.YoutubeDL() as ydl:
#    ydl.download()


def make_mention(user_id: int):
    return "<@" + str(user_id) + ">"


def find_amiami(string):
    urls = []
    while string.find("https://www.amiami.com/eng/detail") != -1:
        start = string.find("https://www.amiami.com/eng/detail")
        string = string[start:]
        end = string.find(" ")
        if end == -1:
            ur = string
        else:
            ur = string[:end]
        urls.append(ur)
        string = string[end:]
    if len(urls) > 0:
        print("Found amiami:", urls)
    return urls


def make_amiami_image(url):
    global image_url
    begin = time.time()
    headers = \
        [{
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'},
            {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36'},
            {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'},
            {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'},
            {
                'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)'},
            {
                'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.2; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; wbx 1.0.0)'},
            {
                'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'},
            {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0'},
            {
                'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:7.0.1) Gecko/20100101 Firefox/7.0.1'},
            {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15'},
            {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1 Safari/605.1.15'},
            {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Safari/605.1.15'},
            {
                'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_1 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Version/11.0 Mobile/15C153 Safari/604.1'},
            {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'},
            {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36'},
            {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36'},
            {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36'},
        ]

    start = url.find("=")
    item_code = url[start + 1:]

    base_code = item_code
    alt_code = item_code.rsplit("-", 1)[0]
    check_code = alt_code.rsplit("-", 1)
    if len(check_code) == 2:
        check_code = check_code[1].isnumeric()
    else:
        check_code = False

    base_suffix = "/" + base_code + ".jpg"
    alt_suffix = "/" + alt_code + ".jpg"
    prefix = "https://img.amiami.com/images/product/main/"
    url_list = []
    header_list = []
    max_check = 400
    mid_value = max_check//2
    nums = []
    for offset in range(1, max_check - mid_value):
        nums.append(mid_value - offset)
        nums.append(mid_value + offset)

    for num in nums:
        if 10 <= num < 100:
            part_url = prefix + "0" + str(num)
        elif num < 10:
            part_url = prefix + "00" + str(num)
        else:
            part_url = prefix + str(num)

        test_url = part_url + base_suffix
        url_list.append(test_url)
        header_list.append(random.choice(headers))

        if check_code:
            alt_test_url = part_url + alt_suffix
            url_list.append(alt_test_url)
            header_list.append(random.choice(headers))

    print("Urls made")
    image_url = -1

    # make the Pool of workers
    print("Pool started")
    num_threads = len(url_list) // 2 if check_code else len(url_list)
    num_threads = 100
    pool = Pool(num_threads)

    # Callback function that checks results and kills the pool
    def check_result(result):
        global image_url
        if result.status_code == 200:
            print("Image found")
            pool.terminate()
            print("Time taken: ", (time.time() - begin), " seconds")
            print("amiami image: ", result.url)
            print("")
            image_url = result.url

    # Start up all of the processes
    for i in range(len(url_list)):
        pool.apply_async(make_request, args=[url_list[i], header_list[i]], callback=check_result)

    # close pool and wait for the work to finish
    pool.close()
    pool.join()

    if image_url != -1:
        return image_url

    return "Image was not found."


def make_request(request_url, header):
    return requests.get(request_url, headers=header)


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
        if str2[index + len_str1].isalnum():
            return False

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
        return exactly_in(str2, str3[index + len_str1:])


def alnum_only(str1):
    new_str = ""
    for char in str1:
        if char.isalnum():
            new_str += char
    return new_str


def timestring_to_sec(str):
    return 0

def get_cooldown_key(message_or_channel):
    global on_cooldown
    try:
        key = message_or_channel.guild
    except AttributeError:
        if isinstance(message_or_channel, discord.Message):
            key = message_or_channel.channel.id
        elif isinstance(message_or_channel, discord.TextChannel):
            key = message_or_channel.id
        else:
            key = "unforunate"
    if key not in on_cooldown:
        on_cooldown[key] = 0
    return key


def get_current_cooldown(message_or_channel):
    key = get_cooldown_key(message_or_channel)
    return on_cooldown[key]


def reset_cooldown(message_or_channel):
    global on_cooldown
    global cooldown_time
    key = get_cooldown_key(message_or_channel)
    on_cooldown[key] = cooldown_time


def request_youtube_video(keyword: str):
    print("Youtube video requested: ", keyword)
    keyword = keyword.strip()
    query = urllib.parse.quote(keyword)
    url = "https://www.youtube.com/results?search_query=" + query
    response = urllib.request.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')

    for vid in soup.findAll(attrs={'class': 'yt-uix-tile-link'}):
        video_url = 'https://www.youtube.com' + vid['href']
        find_index = video_url.find('https://www.youtube.com/watch')
        if find_index == 0:
            print(video_url)
            return video_url

    print("Returning despacito")
    return despacito


def request_google_vision(url):
    print("Starting request")

    descriptions = ""
    image_types = ['jpg', 'jpeg', 'png', 'gif', 'application', 'html']

    test_response = requests.post(url)

    try:
        content_type = test_response.headers['Content-Type']
    except KeyError:
        return ""
    print(content_type)
    if any(ext in content_type for ext in image_types):
        print("requesting")

        image_data = base64.b64encode(requests.get(url).content).decode('UTF-8')

        content_json_obj = {'content': image_data}

        feature_json_obj = [
            {
                'type': 'WEB_DETECTION',
                'maxResults': 10,
            }
        ]

        request_list = [
            {
                'features': feature_json_obj,
                'image': content_json_obj,
            }
        ]

        with open('hold.txt', 'w') as hold:
            json.dump({'requests': request_list}, hold)
        data = open('hold.txt', 'rb').read()
        # print("post")
        response = requests.post(url='https://vision.googleapis.com/v1/images:annotate?key=' + API_KEY,
                                 data=data,
                                 headers={'Content-Type': 'application/json'})
        print("received data")
        response_data = json.loads(response.text)
        # print(response_data)
        descriptions = ""
        try:
            for webEntity in response_data['responses'][0]['webDetection']['webEntities']:
                if 'description' in webEntity.keys():
                    descriptions = descriptions + webEntity['description'] + " "
        except KeyError:
            descriptions = ""
    print(descriptions)
    return descriptions


def regex_fair(message: str):
    list_of_fairs = ["".join(p) for p in permutations("fair")]
    for word in list_of_fairs:
        # if generic_regex(message, word):
        # return True
        if exactly_in(word, message):
            return True
    return False


def generic_regex(message: str, phrase: str):
    ending = '[^a-zA-Z0-9]*'
    start = '[^a-zA-Z0-9]*'
    regex = ''
    for character in phrase:
        regex += start
        regex += character
    regex += ending
    compiler = re.compile(regex)
    result = compiler.search(message)
    return result is not None


# Roll function designed for command usage
def roll_function(message: str, roll_type: str):
    message = message.strip()
    danny_roll = (roll_type == 'dannyroll')
    roll_string = "Input was not acceptable"
    modifier_matching = re.compile('\d+d\d+ *[-+] *\d* *', re.IGNORECASE)
    modifier_match = modifier_matching.match(message)
    find_digits = re.compile('\d+')
    if modifier_match is None:
        # Try basic matching
        basic_matching = re.compile('\d+d\d+ *', re.IGNORECASE)
        basic_match = basic_matching.match(message)
        if basic_match is None:
            x = 0

        elif basic_match.end() != len(message):
            print(str(basic_match.end()) + "," + str(len(message)))

        else:
            # continue with basic matching
            numeric_values = find_digits.findall(message)
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
                    if danny_roll:
                        if number_of_sides == 1:
                            dice_list.append(1 - 2)
                        else:
                            new_number_of_sides = (number_of_sides // 3) if (number_of_sides // 3) > 0 else 1
                            dice_list.append(random.randrange(1, new_number_of_sides + 1))

                    else:
                        dice_list.append(random.randrange(1, number_of_sides + 1))

                roll_string = "Dice values: " + str(dice_list)[1:-1] + "\nSum: " + str(sum(dice_list))

    elif modifier_match.end() != len(message):
        print(str(modifier_match.end()) + "," + str(len(message)))

    else:
        # continue with modifier matching
        assert "+" in message or "-" in message

        modifier_symbol = "+" in message
        modifier_as_multiplier = 2 * int(modifier_symbol) - 1

        numeric_values = find_digits.findall(message)
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
                if danny_roll:
                    if number_of_sides == 1:
                        dice_list.append(1 - 2)
                    else:
                        new_number_of_sides = (number_of_sides // 3) if (number_of_sides // 3) > 0 else 1
                        dice_list.append(random.randrange(1, new_number_of_sides + 1))
                else:
                    dice_list.append(random.randrange(1, number_of_sides + 1))

            roll_string = "Dice values: " + str(dice_list)[1:-1] + "\nSum: " + str(sum(dice_list)) \
                          + "\nModifier: " + str(modifier_as_multiplier * modifier) + "\nFinal value: " \
                          + str(sum(dice_list) + modifier * modifier_as_multiplier)

    return roll_string


def convert_to_emoji_list(num):
    jackpot = ("777", num.find("777"))
    # twenty_one_a = num.find("21")
    # twenty_one_b = -1
    # if twenty_one_a >= 0:
    #    twenty_one_b = num[twenty_one_a + 2:].find("21")
    #    if twenty_one_b >= 0:
    #        twenty_one_b += twenty_one_a + 2 + 1
    # twenty_one_a = ("21", twenty_one_a)
    # twenty_one_b = ("21", twenty_one_b)
    hundred = num.find("100")
    ten = num.find("10")
    if ten == hundred:
        ten = num[hundred + 3:].find("10")
        if ten >= 0:
            ten += hundred + 3
    hundred = ("100", hundred)
    ten = ("10", ten)

    chars = list(num)
    # for tup in [jackpot, twenty_one_a, twenty_one_b, hundred, ten]:
    for tup in [jackpot, hundred, ten]:
        v, i = tup
        if i >= 0:
            chars[i] = v
            for j in range(i + 1, i + len(v)):
                chars[j] = "-"

    chars = [value for value in chars if value != "-"]

    return chars


def check_emojis(emoji_list, emoji_nums):
    emoji_keys = emoji_nums.keys()

    emoji_count = {}
    for key in emoji_keys:
        emoji_count[key] = 0

    emoji_check = True

    for i in range(0, len(emoji_list)):
        e = emoji_list[i]
        if not emoji_check:
            break

        if e in emoji_keys:
            if emoji_count[e] < emoji_nums[e]:
                emoji_list[i] = (e, emoji_count[e])
                emoji_count[e] += 1
            else:
                emoji_check = False
                break
        else:
            print("Unknown value")
            return [-1]

    if not emoji_check:
        return [-1]

    return emoji_list


# Creates a new RPSData object
def create_rps_data(user_id: int, channel: discord.TextChannel, num_rounds: int):
    return RPSData(user_id=user_id, channel=channel, num_rounds=num_rounds)


# Randomly selects a result (lose, draw, win)
def select_rps_result():
    return random.choice([-1, 0, 1])


# Calculate Guubot's input from user input and result
def calculate_guubot_rps_input(user_input, result: int):
    return RPSChoices((user_input + result) % 3).name.lower()


# Returns quiz info dependent on the info_type
def get_quiz_info(member, info_type:str):
    quiz_info = None

    # Get member role name which is also question name
    role = get_member_role(member)
    if role is None:
        return None
    question_name = role.name

    # Get question info if possible
    if question_name is not None:
        quiz_info = quiz_data[question_name][info_type]

    return quiz_info


# Return the quiz role of member
def get_member_role(member):
    for role in member.roles:
        if role.name in quiz_data:
            return role
    return None


# Check for in-n-out in message
async def in_n_out_check(msg):
    content = msg.content
    if "in-n-out" in content.lower():
        return True

    all_descriptions = ""

    for a in msg.attachments:
        descriptions = request_google_vision(a.proxy_url)
        all_descriptions = all_descriptions + descriptions + " "

    for e in msg.embeds:
        descriptions = request_google_vision(e.url)
        all_descriptions = all_descriptions + descriptions + " "

    if "in-n-out" in all_descriptions.lower():
        return True

    return


# Get information of message
async def get_message_data(msg):
    # Get string content
    content = msg.content

    # Get all file objects
    files = []
    for attachment in msg.attachments:
        f = open(attachment.filename, mode='w+b')
        await attachment.save(f)
        file = discord.File(f, attachment.filename)
        files.append(file)

    return content, files


async def get_dm_channel(user_id):
    user = client.get_user(user_id)
    user_dm = user.dm_channel
    if user_dm is None:
        await user.create_dm()
        user_dm = user.dm_channel
    return user_dm

# Functions run in loop


# reset display name loop
async def reset_display_name():
    await client.wait_until_ready()
    while not client.is_closed():
        for changed_guild in client.guilds:
            if changed_guild.me.display_name != "GuuBot":
                print(changed_guild.name)
                print(changed_guild.me.display_name)
                print("---")
                await changed_guild.me.edit(nick=None)
        await asyncio.sleep(60)


# cooldown loop
async def cooldown():
    global on_cooldown
    await client.wait_until_ready()
    while not client.is_closed():
        for guild in on_cooldown:
            on_cooldown[guild] = on_cooldown[guild] - 1
            if on_cooldown[guild] < 0:
                on_cooldown[guild] = 0
        await asyncio.sleep(1)


# RPS loop
async def rps_loop():
    global rps_game
    await client.wait_until_ready()
    while not client.is_closed():
        if rps_game is not None:
            # Reset input and early statuses
            rps_game.refuse_input()
            rps_game.set_early()
            rps_game.reset_early_shot()
            rps_game.reset_user_input()

            # Get game data
            data = rps_game.get_game_data()
            channel = data["channel"]

            # Make intro score text
            user_mention = make_mention(data["opponent id"])
            basic_score_text = \
                user_mention + "\n " + "The current score is :" \
                + "\nMe: " + str(data["bot score"]) \
                + "\nYou: " + str(data["opponent score"])

            # Send intro score text
            await channel.send(content=basic_score_text)

            # Pause
            await asyncio.sleep(0.5)

            # Send start round text
            await channel.send(content="Let's begin a round")

            # Begin accepting input
            rps_game.accept_input()

            for game_text in ["Rock!", "Paper!", "Scissors!", "Shoot!"]:
                # Pause
                await asyncio.sleep(0.75)

                # output game text
                await channel.send(content=game_text)

            # Change early status to false
            rps_game.set_not_early()

            # Wait until user input is received
            for i in range(0, 50):
                if rps_game.get_user_input() is None:
                    await asyncio.sleep(0.1)
                else:
                    break

            user_input = rps_game.get_user_input()

            # Choose result
            if user_input is None:
                result = 1
            elif user_input is RPSChoices.GUN:
                result = 1
            else:
                result = select_rps_result()

            # update game score
            if result == 1:
                rps_game.bot_won()

            if result == -1:
                rps_game.opponent_won()

            # Figure out end of round text
            if user_input is None:
                round_text = "You did not show your hand. I automatically win the round"
            elif user_input is RPSChoices.GUN:
                round_text = "I activate Mirror Force! I win this round."
            else:
                guubot_input = calculate_guubot_rps_input(user_input, result)
                round_text = "I select " + guubot_input

            # Output Guubot's choice and round result (if necessary)
            await channel.send(content=round_text)

            # Output early shot text if necesary
            if rps_game.is_early_shooter():
                early_shot_text = "I don't appreciate it when you shoot before I say to"
                await channel.send(content=early_shot_text)

            # Output overall score/result if game is finished
            if rps_game.is_game_over():
                data = rps_game.get_game_data()
                end_of_game_text = \
                    data["winner"] + " Win!" \
                    + "\nMe: " + str(data["bot score"]) \
                    + "\nYou :" + str(data["opponent score"])

                await channel.send(content=end_of_game_text)

                # Check whether or not to send invitation
                # Guubot must win a best of 5
                if data["winner"] == "I" and data["max rounds"] == 5:
                    if client.get_guild(EnergylessZone).get_member(data["opponent id"]) is None:
                        loser_dm = await get_dm_channel(data["opponent id"])
                        ez_announcements_channel = discord.utils.get(client.get_guild(EnergylessZone).text_channels, name="announcements")
                        new_invite = await ez_announcements_channel.create_invite(max_uses=1)
                        await loser_dm.send(content="Welcome")
                        await loser_dm.send(content=new_invite)

                rps_game = None

        await asyncio.sleep(1)


# On successful question answering, user moves on to next question
async def increase_quiz_role(member):
    current_role = get_member_role(member)
    current_role_name = current_role.name
    if current_role_name == "Winner":
        return

    cr_index = quiz_roles.index(current_role_name)
    new_index = cr_index + 1
    new_role_name = quiz_roles[new_index]
    for role in member.guild.roles:
        if role.name == new_role_name:
            await member.remove_roles(current_role)
            await member.add_roles(role)
            break

    # Congratulate players who finished the game
    if new_role_name == "Winner":
        await member.edit(nick="")
        announcement_channel = discord.utils.get(member.guild.text_channels, name='announcements')
        await announcement_channel.send(make_mention(member.id) + " answered all the questions!")

    return


# Delete all quiz roles
async def remove_quiz_roles(member):
    new_roles = [role for role in member.roles if role.name not in quiz_roles]
    await member.edit(roles=new_roles)


# Various awaited responses
async def await_message(message: discord.Message, content=None, embed=None):
    if content is None:
        await message.channel.send(embed=embed)
    elif embed is None:
        await message.channel.send(content=content)
    else:
        await message.channel.send(content=content, embed=embed)

    reset_cooldown(message)


async def await_channel(channel: discord.TextChannel, content=None, embed=None):
    if channel is not None:
        if content is None:
            await channel.send(embed=embed)
        elif embed is None:
            await channel.send(content=content)
        else:
            await channel.send(content=content, embed=embed)

    reset_cooldown(channel)


async def await_ctx(ctx: discord.ext.commands.Context, content=None, embed=None):
    if content is None:
        await ctx.send(embed=embed)
    elif embed is None:
        await ctx.send(content=content)
    else:
        await ctx.send(content=content, embed=embed)

    reset_cooldown(ctx.channel)


# Used for on reaction add
async def await_fetch_message(channel, author_channel, content=None, files=None):
    await author_channel.send(content=content, files=files)

    reset_cooldown(channel)


# Used for guubot fetching
async def await_fetch(ctx: discord.ext.commands.Context, author_dm_channel, content=None, files=None):
    await author_dm_channel.send(content=content, files=files)
    reset_cooldown(ctx.channel)


@client.command()
async def roll(ctx, *, value):
    await await_ctx(ctx, roll_function(value, "roll"))


@client.command()
async def dannyroll(ctx, *, value):
    await await_ctx(ctx, roll_function(value, "dannyroll"))


@client.command()
async def play(ctx: discord.ext.commands.Context, *, value):
    value = value.strip()
    video = request_youtube_video(value)
    await await_ctx(ctx, content=video)


@client.command()
async def echo(ctx, *, phrase):
    await ctx.send(phrase)


@client.command()
async def fetch(ctx):
    previous_message = await ctx.channel.history(limit=1, before=ctx.message).flatten()

    # Weird situation where there is no previous message
    if len(previous_message) == 0:
        await await_ctx(ctx, "Message could not be found")
        return

    # Get previous message
    previous_message = previous_message[0]

    # Don't send a message to another bot
    author = previous_message.author
    if author.bot:
        await await_ctx(ctx, "Author is bot")
        return

    content, files = await get_message_data(previous_message)

    # Get dm_channel with author
    author_dm = await get_dm_channel(author.id)

    # Delete message being fetched
    await previous_message.delete()

    # Deliver message back to owner
    try:
        await await_fetch(ctx, author_dm, content, files)
    except discord.HTTPException:
        pass

    # Delete the command
    await ctx.message.delete()


@client.command()
async def upvote(ctx, phrase):
    previous_message = await ctx.channel.history(limit=1, before=ctx.message).flatten()
    # Weird situation where there is no previous message
    if len(previous_message) == 0:
        await await_ctx(ctx, "Message could not be found")
        return

    # Get previous message
    previous_message = previous_message[0]

    # Don't send a message to another bot
    author = previous_message.author
    if author.bot:
        await await_ctx(ctx, "Author is bot")
        return

    up_arrow = u"\U00002B06"

    num = phrase
    emoji_dict = {
        "0": ["0\u20e3", '\N{Regional Indicator Symbol Letter O}', '\N{Negative Squared Latin Capital Letter O}'
            , '\N{Heavy Large Circle}', '\N{Black Circle for Record}'],
        "1": ["1\u20e3", '\N{Regional Indicator Symbol Letter O}', '\N{First Place Medal}'],
        "2": ["2\u20e3", '\N{Second Place Medal}'],
        "3": ["3\u20e3", '\N{Third Place Medal}'],
        "4": ["4\u20e3"],
        "5": ["5\u20e3"],
        "6": ["6\u20e3"],
        "7": ["7\u20e3"],
        "8": ["8\u20e3", '\N{Billiards}'],
        "9": ["9\u20e3"],
        "10": ['\N{Keycap Ten}'],
        "100": ['\N{Hundred Points Symbol}'],
        # "21": [u"\U0001F4C5", u"\U0001F4C6"],
        "777": ['\N{Slot Machine}']
    }

    emoji_nums = {}
    for em in emoji_dict.keys():
        emoji_nums[em] = len(emoji_dict[em])

    if not num.isnumeric():
        await await_ctx(ctx, content="Value must be number")
        return

    else:
        emoji_list = convert_to_emoji_list(num)
        if len(emoji_list) > 19:
            await await_ctx(ctx, content="Too long to convert into emojis")
            return

        emoji_list = check_emojis(emoji_list, emoji_nums)
        if emoji_list[0] == -1:
            # await message
            await await_ctx(ctx, content="Not enough emojis to make value")
            return
        else:
            for tup in emoji_list:
                k, i = tup
                emoji_to_use = emoji_dict[k][i]
                await previous_message.add_reaction(emoji_to_use)
            await previous_message.add_reaction(up_arrow)


@client.command()
async def downvote(ctx, phrase):
    previous_message = await ctx.channel.history(limit=1, before=ctx.message).flatten()
    # Weird situation where there is no previous message
    if len(previous_message) == 0:
        await await_ctx(ctx, "Message could not be found")
        return

    # Get previous message
    previous_message = previous_message[0]

    # Don't send a message to another bot
    author = previous_message.author
    if author.bot:
        await await_ctx(ctx, "Author is bot")
        return

    down_arrow = u"\U00002B07"

    num = phrase
    emoji_dict = {
        "0": ["0\u20e3", '\N{Regional Indicator Symbol Letter O}', '\N{Negative Squared Latin Capital Letter O}'
              , '\N{Heavy Large Circle}', '\N{Black Circle for Record}'],
        "1": ["1\u20e3", '\N{Regional Indicator Symbol Letter O}', '\N{First Place Medal}'],
        "2": ["2\u20e3", '\N{Second Place Medal}'],
        "3": ["3\u20e3", '\N{Third Place Medal}'],
        "4": ["4\u20e3"],
        "5": ["5\u20e3"],
        "6": ["6\u20e3"],
        "7": ["7\u20e3"],
        "8": ["8\u20e3", '\N{Billiards}'],
        "9": ["9\u20e3"],
        "10": ['\N{Keycap Ten}'],
        "100": ['\N{Hundred Points Symbol}'],
        # "21": [u"\U0001F4C5", u"\U0001F4C6"],
        "777": ['\N{Slot Machine}']
    }

    emoji_nums = {}
    for em in emoji_dict.keys():
        emoji_nums[em] = len(emoji_dict[em])

    if not num.isnumeric():
        await await_ctx(ctx, content="Value must be number")
        return

    else:
        emoji_list = convert_to_emoji_list(num)
        if len(emoji_list) > 19:
            await await_ctx(ctx, content="Too long to convert into emojis")
            return

        emoji_list = check_emojis(emoji_list, emoji_nums)
        if emoji_list[0] == -1:
            # await message
            await await_ctx(ctx, content="Not enough emojis to make value")
            return
        else:
            for tup in emoji_list:
                k, i = tup
                emoji_to_use = emoji_dict[k][i]
                await previous_message.add_reaction(emoji_to_use)
            await previous_message.add_reaction(down_arrow)


@client.command()
async def kill(ctx):
    # Only allow me and miguel to use kill command
    if ctx.message.author.id != me and ctx.message.author.id != miguel:
        await await_ctx(ctx, content="You do not have permission to kill")
        return

    # Delete the command
    # await ctx.message.delete()

    # Find previous message
    previous_message = await ctx.channel.history(limit=1, before=ctx.message).flatten()

    # Weird situation where there is no previous message
    if len(previous_message) == 0:
        await await_ctx(ctx, "Message could not be found")
        return

    # Get previous message
    previous_message = previous_message[0]

    # Don't send a message to another bot
    author = previous_message.author
    if author.bot:
        await await_ctx(ctx, "Author is bot")
        return

    # Delete message being fetched
    await previous_message.delete()

    # Get dm_channel with author
    author_dm = await get_dm_channel(author.id)

    # Send a you died screen to user
    await await_channel(author_dm, embed=you_died_embed)


@client.command()
async def rps(ctx, num):
    global rps_game

    if rps_game is not None:
        await await_ctx(ctx=ctx, content="I'm already playing Rock-Paper-Scissors. How many hands do you think I have?")
        return

    check_failed = False
    num_rounds = 0

    # Check conditions of valid input
    try:
        num_rounds = int(num)

        # Actual check
        if (num_rounds <= 0) or (num_rounds >= 20) or (num_rounds % 2 == 0):
            check_failed = True

    except ValueError:
        check_failed = True

    if check_failed:
        await await_ctx(ctx=ctx, content="Please input a positive odd number less than 20")
        return

    rps_game = create_rps_data(user_id=ctx.author.id, channel=ctx.channel, num_rounds=num_rounds)

    #game_data_dict = rps_game.get_game_data()
    #output_text = str(game_data_dict)
    #await await_ctx(ctx=ctx, content=output_text)


@client.command()
async def guuball(ctx, question):
    response_string = ""
    if question[-1] != "?":
        response_string = "Ask a proper question."

    else:
        guuball_index = random.randrange(0,len(magic_guuball_responses))
        if guuball_index == 0: # Special response
            magic_8ball_index = random.randrange(0,len(magic_8ball_responses))
            response_string = magic_guuball_responses[guuball_index] + " '" + magic_8ball_responses[magic_8ball_index] + "'"
        else:
            response_string = magic_guuball_responses[guuball_index]

    await await_ctx(ctx=ctx, content=response_string)


@client.command()
async def question(ctx):
    if ctx.guild.id != EnergylessZone:
        await await_ctx(ctx=ctx, content="Questions are only for the best of 5 losers")
        return

    author = ctx.message.author
    dm_channel = await get_dm_channel(author.id)
    quiz_question = get_quiz_info(author, "question")
    if quiz_question is not None:
        await dm_channel.send(content=quiz_question)
    else:
        await dm_channel.send(content="I don't have any questions for you")


@client.command()
async def hint(ctx):
    if ctx.guild.id != EnergylessZone:
        await await_ctx(ctx=ctx, content="Hints are only for the best of 5 losers")
        return

    author = ctx.message.author
    dm_channel = await get_dm_channel(author.id)
    quiz_hint = get_quiz_info(author, "hint")
    if quiz_hint is not None:
        await dm_channel.send(content=quiz_hint)
    else:
        await dm_channel.send(content="I don't have any hints for you")


client.remove_command('help')


@client.command()
async def help(ctx):
    embed = discord.Embed(title="Guubot", description="List of commands:", color=0xeee657)

    embed.add_field(name="guubot play *phrase* (Ex: 'guubot play barbie doll')", value="Searches for a youtube video",
                    inline=False)
    embed.add_field(name="guubot roll #d# +/- # (Ex: 'guubot roll 4d20 + 4' or 'guubot roll 10d15')",
                    value="Rolls dice with optional modifier", inline=False)
    embed.add_field(name="guubot dannyroll #d# +/- # (Ex: 'guubot dannyroll 4d20 + 4' or 'guubot dannyroll 10d15')",
                    value="Rolls dice with optional modifier as if it were Danny", inline=False)
    embed.add_field(name="guubot echo *phrase*", value="Repeats what you say")
    embed.add_field(name="guubot f#$%*",
                    value="For when someone sends something really dumb or NSFL and you want them to be on the receiving end instead",
                    inline=False)
    embed.add_field(name="guubot f#$%*",
                    value="For when someone sends something really dumb or NSFL and you want them to be on the receiving end instead",
                    inline=False)
    embed.add_field(name="guubot upvote [number]", value="Attempts to upvote the previous message to [number] upvotes",
                    inline=False)
    embed.add_field(name="guubot downvote [number]",
                    value="Attempts to downvote the previous message to [number] downvotes",
                    inline=False)
    embed.add_field(name="guubot kill",
                    value="A requested command that causes no ill effects other than death",
                    inline=False)
    embed.add_field(name="guubot rps [odd number]", value="Challenge Guubot to some rock-paper-scissors", inline=False)
    embed.add_field(name="guubot question", value="Guubot may have a question for you", inline=False)
    embed.add_field(name="guubot hint", value="Guubot may have a hint for you", inline=False)
    embed.add_field(name="guubot help", value="Gives this message", inline=False)

    await ctx.send(embed=embed)


@client.event
async def on_message(message):
    global mr_dictionary

    cd = get_current_cooldown(message)

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

    if isinstance(message.channel, discord.TextChannel) and (message.channel.guild.id == EnergylessZone):  # Serious Mode Guubot
        # Guubot responds to only 2 commands
        if message.content.lower() == "guubot question" or message.content.lower() == "guubot hint":
            await client.process_commands(message)

        # Guubot checks responses

        # Get expected answer
        expected_answer = get_quiz_info(message.author, "answer")

        # Do nothing if user is not being quizzed (Applicable to Winners and Bots)
        if expected_answer is None:
            return

        # Check if answer is correct
        if expected_answer.lower() == message.content.lower():
            author_dm_channel = await get_dm_channel(message.author.id)
            await author_dm_channel.send(content="That's correct. woo....")
            # Move user to next question
            await increase_quiz_role(message.author)

        # Delete any message if the author is not me or a bot
        messages = await message.channel.history(limit=20).flatten()
        for m in messages:
            await m.delete()
        return

    try:
        mr_dictionary[message.author.id] = (message.author.roles, message.author.nick)

    except AttributeError:
        pass

    if rps_game is not None:
        if message.author.id == rps_game.get_opponent() and message.channel == rps_game.get_channel() \
                and rps_game.get_input_status() and rps_game.get_user_input() is None:

            # Remove special characters
            shortened_text = alnum_only(message.content.lower())

            # Set user input to appropriate value
            if shortened_text == "rock" or shortened_text == "r":
                rps_game.set_user_input(RPSChoices.ROCK)

            if shortened_text == "paper" or shortened_text == "p":
                rps_game.set_user_input(RPSChoices.PAPER)

            if shortened_text == "scissors" or shortened_text == "s":
                rps_game.set_user_input(RPSChoices.SCISSORS)

            if shortened_text == "gun":
                rps_game.set_user_input(RPSChoices.GUN)

            # If user made an input and early status is true ==> early shot.
            if rps_game.get_user_input() is not None and rps_game.get_early_status():
                rps_game.early_input()

    guild_cooldown = cd <= 0
    if not guild_cooldown:
        return

    if message.channel.id == venting_channel:
        return

    # Figure out if version of "let's go" is in the message
    lets_go_found = False
    for lets in ["let's", "lets", "let" + u"\u2019" + "s"]:
        if not lets_go_found:
            if str1_star_str2(lets, "go", message.content.lower()):
                lets_go_found = True

    # Check if "fair" appears in message
    exact_fair = regex_fair(message.content.lower())

    # Check if "amiami.com" in message
    urls = find_amiami(message.content)

    # Check if "in-n-out" appears in message
    #in_n_out = await in_n_out_check(message)

    if "awoo" in message.content.lower():

        awoo_select = random.randrange(0, 4)

        if awoo_select == 0:
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

    #elif in_n_out:
    #    await await_message(message=message, content="A reminder that Ryan is a terrible friend sometimes.")

    elif "pasta" in message.content.lower():
        if message.author.id == kolson:
            new_invite = await message.channel.create_invite(max_uses=1)
            user = client.get_user(message.author.id)
            await user.send(content=new_invite)
            await await_message(message=message, content='He said "pasta"! SWING THE BAN HAMMER!')
            await message.guild.kick(message.author)
            await await_message(message=message, content='Fine. Just the kick hammer...')

    elif "concrete revolutio" in message.content.lower():
        if message.author.id == mark:
            new_invite = await message.channel.create_invite(max_uses=1)
            user = client.get_user(message.author.id)
            await user.send(content=new_invite)
            await await_message(message=message, content="I'm sorry.")
            await message.guild.kick(message.author)
            await await_message(message=message,
                                content='Those are not the lyrics to the title of Konkurīto Reborutio: Chōjin Gensō')
        if message.author.id == me:
            await await_message(message=message,
                                content='Those are not the lyrics to the title of Konkurīto Reborutio: Chōjin Gensō')

    elif "merry christmas" in message.content.lower() or "merry xmas" in message.content.lower():
        if message.author.id != noah:  # Noah isn't allowed to be kicked from the server
            # Create and send an invite to the user
            new_invite = await message.channel.create_invite(max_uses=1)
            user = client.get_user(message.author.id)
            await user.send(content=new_invite)

            # Joke message
            await await_message(message=message, content="Hey, you wanna get someone fired?")

            # Kick user
            await message.guild.kick(message.author)

    elif exactly_in("nico", message.content.lower()):
        await await_message(message=message, content=nico, embed=nico_embed)

    elif "secret" in message.content.lower() and "woman" in message.content.lower():
        await await_message(message=message, content=conan, embed=conan_embed)

    elif lets_go_found:
        await await_message(message=message, content=malt_shop, embed=malt_shop_embed)

    elif "freaked it" in message.content.lower():
        await await_message(message=message, content=fire, embed=fire_embed)

    elif "nora" in message.content.lower():
        et = timezone('US/Eastern')
        today = datetime.now().astimezone(et)
        if today.hour < 12:
            await await_message(message=message, content=morning, embed=nora_morning)

    elif "sad" == message.content.lower() or "sad!" == message.content.lower() or "sad." == message.content.lower():
        if message.author.id == noah:
            await await_message(message=message, content="Smile\nSweet\nSister\nSadistic\nSurprise\nService")

    elif "fake" in message.content.lower():
        if message.author.id == noah:
            await await_message(message=message, embed=faker_embed)

    elif "guubot play" in message.content.lower() and message.content.lower().find("guubot play") > 0:
        annoying = message.content.lower().split("guubot play", 1)
        video = request_youtube_video(annoying[1])
        await await_message(message=message, content=video)

    elif exactly_in("<@438892047039070218> do your thing", message.content.lower()) and (
            message.author.id == julian or message.author.id == me):
        if 0 == random.randrange(0, 2):
            await await_message(message=message, embed=sheik_embed)
        else:
            index = random.randrange(0, len(fair_embeds))
            await await_message(message=message, embed=fair_embeds[index])

    elif exactly_in("hot take", message.content.lower()):
        index = random.randrange(0, len(take_embeds))
        await await_message(message=message, embed=take_embeds[index])

    elif len(urls) > 0:
        for u in urls:
            img = make_amiami_image(u)
            if img !=  "Image was not found.":
                e = discord.Embed()
                e.set_image(url=img)
                await await_message(message, content=u, embed=e)

    elif "it's almost like" in message.content.lower() or "its almost like" in message.content.lower():
        await await_message(message, embed=almost_like_embed)

    elif "f#$%*" in message.content.lower():
        # Deleting Noah's last message

        # Get Noah's last message
        noah_last_message = await message.channel.history().get(author__id=noah)
        print(noah_last_message)
        # Assume we are fetching Noah's last message
        fetch_noah_message = True

        # If Noah's somehow hasn't sent a message to this channel
        if noah_last_message is None:
            fetch_noah_message = False

        if fetch_noah_message:
            try:
                # Get the content and/or files
                noah_content, noah_files = await get_message_data(noah_last_message)
                print(noah_content)
                # Get noah's dm
                noah_dm = await get_dm_channel(noah)

                # send noah his last message
                await await_fetch_message(message.channel, noah_dm, noah_content, noah_files)

                # delete noah's message
                await noah_last_message.delete()

            except discord.HTTPException:
                pass

        await message.delete()

    else:
        previous_messages = await message.channel.history(limit=1, before=message).flatten()
        if len(previous_messages) == 1:

            m1 = previous_messages[0]

            if m1.content.lower() == message.content.lower() and message.content.lower() in ["f", "1"]:
                if not m1.author.bot:
                    await await_message(message, content=message.content)

    if message.content.lower()[:6] == "guubot":
        message.content = "guubot" + message.content[6:]

    if message.content == "Hello? Can anyone hear me?" and message.author.id == me:
        await await_message(message, content="What do you want....?")

    await client.process_commands(message)


@client.event
async def on_message_edit(before, after):
    if before.channel.id == venting_channel:
        return

    if not exactly_in("fair", before.content.lower()) and exactly_in("fair", after.content.lower()):
        index = random.randrange(0, len(fair_embeds))
        await await_message(message=after, embed=fair_embeds[index])


@client.event
async def on_reaction_add(reaction, user):
    global expand1
    global expand2
    global expand3
    global expand4
    message = reaction.message

    cd = get_current_cooldown(message)
    guild_cooldown = cd <= 0
    if not guild_cooldown:
        return

    expand1_id = 459124362075832320
    if expand1 is None:
        expand1 = client.get_emoji(459124362075832320)
        expand2 = client.get_emoji(459124362063118336)
        expand3 = client.get_emoji(459124362004529173)
        expand4 = client.get_emoji(459124361698213890)

    if not isinstance(reaction.emoji, str):
        if reaction.emoji.id == expand1_id:
            await message.add_reaction(expand1)
            await message.add_reaction(expand2)
            await message.add_reaction(expand3)
            await message.add_reaction(expand4)

    elif reaction.emoji == u"\U0001F3BE":
        author = message.author
        if author.bot:
            await message.channel.send("Author is bot")
        else:
            # Get dm_channel with author
            author_user = client.get_user(author.id)
            author_dm = author_user.dm_channel
            if author_dm is None:
                await author_user.create_dm()
                author_dm = author_user.dm_channel

            content, files = await get_message_data(message)

            try:
                # Delete message being fetched
                await message.delete()

                # Deliver message back to owner
                await await_fetch_message(message.channel, author_dm, content, files)
            except discord.errors.Forbidden:
                pass

            except discord.HTTPException:
                pass

    else:
        pass


@client.event
async def on_member_join(member):
    global client
    global mr_dictionary

    # Only for Energyless Zone
    if member.guild.id == EnergylessZone:
        # Give players the first role
        first_role_name = quiz_roles[0]
        for role in member.guild.roles:
            if role.name == first_role_name:
                await member.add_roles(role)
                break

        # Assign each player a random prisoner number
        prisoner_number = str(random.randrange(1, 999))
        prisoner_number = ((3-len(prisoner_number)) * "0") + prisoner_number
        prisoner_name = "Prisoner " + prisoner_number
        await member.edit(nick=prisoner_name)

        # Make an announcement in the announcment channel
        announcement_channel = discord.utils.get(member.guild.text_channels, name='announcements')
        await announcement_channel.send("Welcome " + make_mention(member.id))

        return

    if member.id in mr_dictionary:
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
    client.loop.create_task(reset_display_name())
    client.loop.create_task(cooldown())
    client.loop.create_task(rps_loop())
    expand1 = client.get_emoji(expand1)
    expand2 = client.get_emoji(expand2)
    expand3 = client.get_emoji(expand3)
    expand4 = client.get_emoji(expand4)


client.run(TOKEN)
