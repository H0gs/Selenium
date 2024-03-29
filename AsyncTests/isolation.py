import asyncio
from concurrent.futures import ThreadPoolExecutor
import urllib.request
import os
import requests
import time

from selenium import webdriver
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

imgUrls = []

things = [['AJR', 'Artist', [{'[name': 'Bang!', 'artist': 'AJR', 'lengthInSeconds': 170, 'url': '9e2buqBpSBU\\\\u0026pp=ygUYQmFuZyEgYnkgQUpSIGx5cmljIHZpZGVv'}, {'name': 'All My Favorite Songs (feat. AJR)', 'artist': 'Weezer, AJR', 'lengthInSeconds': 170, 'url': 'm_dUrmlpE_8\\\\u0026pp=ygU8QWxsIE15IEZhdm9yaXRlIFNvbmdzIChmZWF0LiBBSlIpIGJ5IFdlZXplciwgQUpSIGx5cmljIHZpZGVv'}, {'name': 'The Lotto', 'artist': 'Ingrid Michaelson, AJR', 'lengthInSeconds': 193, 'url': 'FLsYE5MoE3M\\\\u0026pp=ygUvVGhlIExvdHRvIGJ5IEluZ3JpZCBNaWNoYWVsc29uLCBBSlIgbHlyaWMgdmlkZW8%3D'}, {'name': 'Record Player', 'artist': 'Daisy the Great, AJR', 'lengthInSeconds': 149, 'url': 'GQzzxRYrPNU\\\\u0026pp=ygUxUmVjb3JkIFBsYXllciBieSBEYWlzeSB0aGUgR3JlYXQsIEFKUiBseXJpYyB2aWRlbw%3D%3D'}, {'name': 'broken', 'artist': 'lovelytheband', 'lengthInSeconds': 204, 'url': '2R4EOfZNykY\\\\u0026pp=ygUjYnJva2VuIGJ5IGxvdmVseXRoZWJhbmQgbHlyaWMgdmlkZW8%3D'}, {'name': 'Im Not Famous', 'artist': 'AJR', 'lengthInSeconds': 220, 'url': 'Oz2q2CVl0x4\\\\u0026pp=ygUhSSdtIE5vdCBGYW1vdXMgYnkgQUpSIGx5cmljIHZpZGVv'}, {'name': 'House of Memories', 'artist': 'Panic! At The Disco', 'lengthInSeconds': 208, 'url': 'OOtTeOkfV8A\\\\u0026pp=ygU0SG91c2Ugb2YgTWVtb3JpZXMgYnkgUGFuaWMhIEF0IFRoZSBEaXNjbyBseXJpYyB2aWRlbw%3D%3D'}, {'name': 'Tear in My Heart', 'artist': 'Twenty One Pilots', 'lengthInSeconds': 188, 'url': 'wB1ceH9yYq0\\\\u0026pp=ygUxVGVhciBpbiBNeSBIZWFydCBieSBUd2VudHkgT25lIFBpbG90cyBseXJpYyB2aWRlbw%3D%3D'}, {'name': 'Celebrate', 'artist': 'Ingrid Michaelson, AJR', 'lengthInSeconds': 197, 'url': 'ZccnQWL7E9s\\\\u0026pp=ygUvQ2VsZWJyYXRlIGJ5IEluZ3JpZCBNaWNoYWVsc29uLCBBSlIgbHlyaWMgdmlkZW8%3D'}, {'name': 'Best Day Of My Life', 'artist': 'American Authors', 'lengthInSeconds': 194, 'url': 'tTsmVFbR100\\\\u0026pp=ygUzQmVzdCBEYXkgT2YgTXkgTGlmZSBieSBBbWVyaWNhbiBBdXRob3JzIGx5cmljIHZpZGVv'}, {'name': 'Worlds Smallest Violin', 'artist': 'AJR', 'lengthInSeconds': 180, 'url': 's9g8jgZwXHg\\\\u0026pp=YAHIAQHwAQG6AwIYAqIGFQHV2fo7J-oOe5ADL5Bg1eaR_tNQtw%3D%3D'}, {'name': 'Boy In The Bubble', 'artist': 'Alec Benjamin', 'lengthInSeconds': 181, 'url': '_PBlykN4KIY\\\\u0026pp=ygUkVW5zdG9wcGFibGUgYnkgVGhlIFNjb3JlIGx5cmljIHZpZGVv'}, {'name': 'Talk Too Much', 'artist': 'COIN', 'lengthInSeconds': 187, 'url': 'YmInQy4TZyk\\\\u0026pp=ygUhVGFsayBUb28gTXVjaCBieSBDT0lOIGx5cmljIHZpZGVv'}, {'name': 'Everybody Talks', 'artist': 'Neon Trees', 'lengthInSeconds': 177, 'url': '1tMsHwlcHp4\\\\u0026pp=ygUpRXZlcnlib2R5IFRhbGtzIGJ5IE5lb24gVHJlZXMgbHlyaWMgdmlkZW8%3D'}, {'name': 'The Good In Me', 'artist': 'Jon Bellion', 'lengthInSeconds': 223, 'url': '2KEsC1Jt2Y8\\\\u0026pp=ygUpVGhlIEdvb2QgSW4gTWUgYnkgSm9uIEJlbGxpb24gbHlyaWMgdmlkZW8%3D'}, {'name': '100 Bad Days', 'artist': 'AJR', 'lengthInSeconds': 210, 'url': 'fOUXlz3kcHQ\\\\u0026pp=ygUfMTAwIEJhZCBEYXlzIGJ5IEFKUiBseXJpYyB2aWRlbw%3D%3D'}, {'name': 'Hey Look Ma, I Made It', 'artist': 'Panic! At The Disco', 'lengthInSeconds': 169, 'url': 'I5VtJwuNWGY\\\\u0026pp=ygU5SGV5IExvb2sgTWEsIEkgTWFkZSBJdCBieSBQYW5pYyEgQXQgVGhlIERpc2NvIGx5cmljIHZpZGVv'}, {'name': 'Im Born To Run', 'artist': 'American Authors', 'lengthInSeconds': 206, 'url': 'UtvE2S26yBM\\\\u0026pp=ygUvSSdtIEJvcm4gVG8gUnVuIGJ5IEFtZXJpY2FuIEF1dGhvcnMgbHlyaWMgdmlkZW8%3D'}, {'name': 'Its Alright', 'artist': 'Mother Mother', 'lengthInSeconds': 175, 'url': 'c_5JCHMhztM\\\\u0026pp=ygUpSXQncyBBbHJpZ2h0IGJ5IE1vdGhlciBNb3RoZXIgbHlyaWMgdmlkZW8%3D'}, {'name': 'Happy Pills', 'artist': 'Weathers', 'lengthInSeconds': 203, 'url': 'RWiJk11NGUE\\\\u0026pp=ygUjSGFwcHkgUGlsbHMgYnkgV2VhdGhlcnMgbHlyaWMgdmlkZW8%3D'}, {'name': 'Way Less Sad', 'artist': 'AJR', 'lengthInSeconds': 207, 'url': '1O34wAxJnwU\\\\u0026pp=ygUfV2F5IExlc3MgU2FkIGJ5IEFKUiBseXJpYyB2aWRlbw%3D%3D'}, {'name': 'Revolution', 'artist': 'The Score', 'lengthInSeconds': 231, 'url': 'AT519AgIrdI\\\\u0026pp=ygUjUmV2b2x1dGlvbiBieSBUaGUgU2NvcmUgbHlyaWMgdmlkZW8%3D'}, {'name': 'All Time Low', 'artist': 'Jon Bellion', 'lengthInSeconds': 217, 'url': 'rnhBElHzHb0\\\\u0026pp=ygUnQWxsIFRpbWUgTG93IGJ5IEpvbiBCZWxsaW9uIGx5cmljIHZpZGVv'}, {'name': 'Numb Little Bug', 'artist': 'Em Beihold', 'lengthInSeconds': 169, 'url': '9mVXPLlnSu4\\\\u0026pp=ygUpTnVtYiBMaXR0bGUgQnVnIGJ5IEVtIEJlaWhvbGQgbHlyaWMgdmlkZW8%3D'}, {'name': 'Ghost', 'artist': 'Confetti', 'lengthInSeconds': 169, 'url': 'PylEm8FkBkg\\\\u0026pp=ygUdR2hvc3QgYnkgQ29uZmV0dGkgbHlyaWMgdmlkZW8%3D'}, {'name': 'The Entertainments Here', 'artist': 'AJR', 'lengthInSeconds': 187, 'url': 'OVdqlQ0Ogus\\\\u0026pp=ygUrVGhlIEVudGVydGFpbm1lbnQncyBIZXJlIGJ5IEFKUiBseXJpYyB2aWRlbw%3D%3D'}, {'name': 'Pretender (feat. Lil Yachty & AJR)', 'artist': 'Steve Aoki, Lil Yachty, AJR', 'lengthInSeconds': 188, 'url': 'FkZlBznlUew\\\\u0026pp=ygUcUHJldGVuZGVyIChmZWF0LiBMaWwgWWFjaHR5IA%3D%3D'}, {'name': 'Born For This', 'artist': 'The Score', 'lengthInSeconds': 237, 'url': 'ccEWf_2H0EY\\\\u0026pp=ygUmQm9ybiBGb3IgVGhpcyBieSBUaGUgU2NvcmUgbHlyaWMgdmlkZW8%3D'}, {'name': 'Damn It Feels Good To Be Me', 'artist': 'Andy Grammer', 'lengthInSeconds': 138, 'url': 'FAo0mWGQNG8\\\\u0026pp=ygU3RGFtbiBJdCBGZWVscyBHb29kIFRvIEJlIE1lIGJ5IEFuZHkgR3JhbW1lciBseXJpYyB2aWRlbw%3D%3D'}, {'name': 'The Fall', 'artist': 'half�alive', 'lengthInSeconds': 186, 'url': 'rT7rklLp1Fk\\\\u0026pp=ygUkVGhlIEZhbGwgYnkgaGFsZuKAomFsaXZlIGx5cmljIHZpZGVv'}, {'name': 'I Wont', 'artist': 'AJR', 'lengthInSeconds': 168, 'url': 'vqcWOgcmxhw\\\\u0026pp=ygUaSSBXb24ndCBieSBBSlIgbHlyaWMgdmlkZW8%3D'}, {'name': 'Morning In America', 'artist': 'Jon Bellion', 'lengthInSeconds': 265, 'url': 'nbYHynUvQ3Y\\\\u0026pp=ygUtTW9ybmluZyBJbiBBbWVyaWNhIGJ5IEpvbiBCZWxsaW9uIGx5cmljIHZpZGVv'}, {'name': 'Ashes', 'artist': 'Stellar', 'lengthInSeconds': 166, 'url': 'wH3JmLBOnMU\\\\u0026pp=ygUcQXNoZXMgYnkgU3RlbGxhciBseXJpYyB2aWRlbw%3D%3D'}, {'name': 'Unstoppable', 'artist': 'The Score', 'lengthInSeconds': 192, 'url': '_PBlykN4KIY\\\\u0026pp=ygUkVW5zdG9wcGFibGUgYnkgVGhlIFNjb3JlIGx5cmljIHZpZGVv'}, {'name': 'Victorious', 'artist': 'Panic! At The Disco', 'lengthInSeconds': 178, 'url': 'tKsBddrGqdI\\\\u0026pp=ygUtVmljdG9yaW91cyBieSBQYW5pYyEgQXQgVGhlIERpc2NvIGx5cmljIHZpZGVv'}, {'name': 'Joe', 'artist': 'AJR', 'lengthInSeconds': 212, 'url': 'BDFmsVANBKI\\\\u0026pp=ygUWSm9lIGJ5IEFKUiBseXJpYyB2aWRlbw%3D%3D'}, {'name': 'still feel.', 'artist': 'half�alive', 'lengthInSeconds': 247, 'url': 'C2RA8cRiInk\\\\u0026pp=ygUnc3RpbGwgZmVlbC4gYnkgaGFsZuKAomFsaXZlIGx5cmljIHZpZGVv'}, {'name': 'Do My Own Thing', 'artist': 'American Authors', 'lengthInSeconds': 196, 'url': 'N3tZhBBduuk\\\\u0026pp=ygUvRG8gTXkgT3duIFRoaW5nIGJ5IEFtZXJpY2FuIEF1dGhvcnMgbHlyaWMgdmlkZW8%3D'}, {'name': 'Boys Will Be Bugs', 'artist': 'Cavetown', 'lengthInSeconds': 329, 'url': 'js_3XGedVqQ\\\\u0026pp=ygUpQm95cyBXaWxsIEJlIEJ1Z3MgYnkgQ2F2ZXRvd24gbHlyaWMgdmlkZW8%3D'}, {'name': 'If I Killed Someone For You', 'artist': 'Alec Benjamin', 'lengthInSeconds': 185, 'url': 'GLHAcAkdB8M\\\\u0026pp=ygU4SWYgSSBLaWxsZWQgU29tZW9uZSBGb3IgWW91IGJ5IEFsZWMgQmVuamFtaW4gbHlyaWMgdmlkZW8%3D'}, {'name': 'Karma', 'artist': 'AJR', 'lengthInSeconds': 245, 'url': '9jxvXP3cW44\\\\u0026pp=ygUYS2FybWEgYnkgQUpSIGx5cmljIHZpZGVv'}, {'name': 'High Hopes', 'artist': 'Panic! At The Disco', 'lengthInSeconds': 190, 'url': 'fH_OnJk6QqU\\\\u0026pp=ygUtSGlnaCBIb3BlcyBieSBQYW5pYyEgQXQgVGhlIERpc2NvIGx5cmljIHZpZGVv'}, {'name': 'creature', 'artist': 'half�alive', 'lengthInSeconds': 335, 'url': 'GJ5nWR_vRcs\\\\u0026pp=ygUkY3JlYXR1cmUgYnkgaGFsZuKAomFsaXZlIGx5cmljIHZpZGVv'}, {'name': 'Someone To You', 'artist': 'BANNERS', 'lengthInSeconds': 219, 'url': 'U2H1LInYPXE\\\\u0026pp=ygUlU29tZW9uZSBUbyBZb3UgYnkgQkFOTkVSUyBseXJpYyB2aWRlbw%3D%3D'}, {'name': 'AOK', 'artist': 'Tai Verdes', 'lengthInSeconds': 173, 'url': 'hdX3aK2Gelo\\\\u0026pp=ygUdQU9LIGJ5IFRhaSBWZXJkZXMgbHlyaWMgdmlkZW8%3D'}, {'name': 'Weak', 'artist': 'AJR', 'lengthInSeconds': 201, 'url': 'tgnNJsG4O8M\\\\u0026pp=ygUXV2VhayBieSBBSlIgbHlyaWMgdmlkZW8%3D'}, {'name': 'Overwhelmed (Ryan Mack Remix)', 'artist': 'Ryan Mack', 'lengthInSeconds': 103, 'url': 'USfrgQXGzqY\\\\u0026pp=ygU2T3ZlcndoZWxtZWQgKFJ5YW4gTWFjayBSZW1peCkgYnkgUnlhbiBNYWNrIGx5cmljIHZpZGVv'}, {'name': 'Dont Threaten Me with a Good Time', 'artist': 'Panic! At The Disco', 'lengthInSeconds': 213, 'url': 'QHqGPsYxcNM\\\\u0026pp=ygVFRG9uJ3QgVGhyZWF0ZW4gTWUgd2l0aCBhIEdvb2QgVGltZSBieSBQYW5pYyEgQXQgVGhlIERpc2NvIGx5cmljIHZpZGVv'}, {'name': 'Dear God', 'artist': 'Confetti', 'lengthInSeconds': 202, 'url': 'ubcHmC1w5H4\\\\u0026pp=ygUgRGVhciBHb2QgYnkgQ29uZmV0dGkgbHlyaWMgdmlkZW8%3D'}, {'name': 'Sinner', 'artist': 'Andy Grammer', 'lengthInSeconds': 220, 'url': 'h8ixK74M8yo\\\\u0026pp=ygUiU2lubmVyIGJ5IEFuZHkgR3JhbW1lciBseXJpYyB2aWRlbw%3D%3D'}]]]
things2 = [["AJR", "Artist"], ["U2", "Artist"], ["Cosmo Shelldrake", "Artist"], ["VOJ", "Artist"], ["Narvent", "Artist"], ["Imase", "Artist"]]

# executor = ThreadPoolExecutor(10)

# asyncio.get_event_loop().run_in_executor(executor, thing)

# async def imageDownloader(imgList):
#     os.chdir("Icons")
#     await asyncio.gather(*(downloadImage(imgList[i], i) for i in range(len(imgList))))
#     os.chdir("..")

# async def downloadImage(url, index):
#     urllib.request.urlretrieve(url, f"{index}.png")

async def downloadImages(playlists):
    artistsList = []
    for playlist in playlists:
        if(playlist[1] == "Artist"):
            artistsList.append(playlist[0])
        print(playlist[0])

    eventExecutor = ThreadPoolExecutor(len(artistsList))
    loop = asyncio.get_event_loop()

    async def in_thread(func):
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(eventExecutor, func)

    async def getUrlAsync():
        await asyncio.gather(*[in_thread(getUrl(artistsList[i], i)) for i in range(10)])

    # async def getUrlAsync():
    #     for i in range(len(artistsList)):
    #         loop.run_in_executor(eventExecutor, getUrl(artistsList[i], i))
    
    
    loop.run_until_complete(getUrlAsync())

    # await asyncio.gather(*(getUrl(artistsList[i], i) for i in range(len(artistsList))))
    # os.chdir("Icons")
    # await asyncio.gather(*(downloadImage(imgUrls[i][0], imgUrls[i][1]) for i in range(len(imgUrls))))
    # os.chdir("..")
    
    # for img in os.listdir("Icons"):
    #     os.remove(f"Icons/{img}")

    # asyncio.run(imageDownloader(["https://th.bing.com/th/id/R.e52bd428d0e821fed4d58ab6988d44c8?rik=93pJt4Ys7Aw7bg&riu=http%3a%2f%2flofrev.net%2fwp-content%2fphotos%2f2016%2f08%2frandom_logo_1.png&ehk=4Su0HMlE75LqSpA67oF3OzYp%2bdhGI8eAsSe%2bCC9Qy1E%3d&risl=&pid=ImgRaw&r=0", "https://th.bing.com/th/id/R.4d732c2c9f99d81862e0823de0e98c46?rik=ozBlq92KSnC2Eg&riu=http%3a%2f%2fclipart-library.com%2fdata_images%2f6167.png&ehk=UGR0HzFbnpBVLHWmBjfH1rKDVMxMjUwoYH9%2bSf4shHQ%3d&risl=&pid=ImgRaw&r=0", "https://vignette.wikia.nocookie.net/new-fantendo/images/b/b8/Champi%C3%B1on_Random.png/revision/latest?cb=20170329164317&path-prefix=es"]))
    # asyncio.run(imageDownloader(imgList))

async def getUrl(name, index):
    browser = webdriver.Chrome()
    browser.get(f"https://open.spotify.com/search/{name}")
    time.sleep(3)
    mainSong = browser.find_element(By.XPATH, r"/html/body/div[3]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div[2]/div/div/section[1]/div[2]/div/div/div/div[2]/a")
    mainSong.click()
    time.sleep(3)
    # print(browser.page_source.split('"track-artist-link-card"><div class="')[1].split('></div><div')[0].split(', ')[1].split(' ')[0])
    imgUrls.append([browser.page_source.split('"track-artist-link-card"><div class="')[1].split('></div><div')[0].split(', ')[1].split(' ')[0], index])
    # print(browser.find_element(By.XPATH, r"/html/body/div[3]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/section/div[4]/div[1]/div/div[2]/div/div/div/div/div[1]/img").get_attribute("href"))

    # while True:
    #     pass

# getUrl("AJR")
asyncio.run(downloadImages(things2))
# urllib.request.urlretrieve("https://i.scdn.co/image/ab6761610000f178e65fa0329c232ac6f5040f80", "AJR.png")