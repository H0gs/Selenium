import requests
import asyncio
import time

# songs = [{'name': 'Bang!', 'artist': 'AJR'}, {'name': 'All My Favorite Songs (feat. AJR)', 'artist': 'Weezer, AJR'}, {'name': 'The Lotto', 'artist': 'Ingrid Michaelson, AJR'}, {'name': 'Record Player', 'artist': 'Daisy the Great, AJR'}, {'name': "I'm Born To Run", 'artist': 'American Authors'}, {'name': 'Karma', 'artist': 'AJR'}, {'name': 'The Fall', 'artist': 'half alive'}, {'name': "It's Alright", 'artist': 'Mother Mother'}, {'name': 'Celebrate', 'artist': 'Ingrid Michaelson, AJR'}, {'name': 'Only Human', 'artist': 'Ryan Mack'}, {'name': 'Burn the House Down', 'artist': 'AJR'}, {'name': 'The Good In Me', 'artist': 'Jon Bellion'}, {'name': 'Tear in My Heart', 'artist': 'Twenty One Pilots'}, {'name': 'Boy In The Bubble', 'artist': 'Alec Benjamin'}, {'name': 'Your New Boyfriend', 'artist': 'Wilbur Soot'}, {'name': "Don't Throw Out My Legos", 'artist': 'AJR'}, {'name': 'Overwhelmed (Ryan Mack Remix)', 'artist': 'Ryan Mack'}, {'name': 'Blur', 'artist': 'Stellar'}, {'name': 'Talk Too Much', 'artist': 'COIN'}, {'name': 'Kingdom Come', 'artist': 'Jon Bellion'}, {'name': "Yes I'm A Mess", 'artist': 'AJR'}, {'name': 'Everybody Talks', 'artist': 'Neon Trees'}, {'name': 'Do My Own Thing', 'artist': 'American Authors'}, {'name': 'Bad Dream', 'artist': 'Stellar'}, {'name': 'killer queen', 'artist': 'Mad Tsai'}, {'name': '100 Bad Days', 'artist': 'AJR'}, {'name': 'sail away', 'artist': 'lovelytheband'}, {'name': 'Wish You the Worst', 'artist': 'Ryan Mack'}, {'name': 'Happy Pills', 'artist': 'Weathers'}, {'name': 'Fvck Somebody', 'artist': 'The Wrecks'}, {'name': 'Thirsty', 'artist': 'AJR'}, {'name': 'Ghost', 'artist': 'Confetti'}, {'name': 'A Good Song Never Dies', 'artist': 'Saint Motel'}, {'name': 'We Happy Dont Worry', 'artist': 'American Authors'}, {'name': "C'est la vie", 'artist': 'Weathers'}, {'name': "World's Smallest Violin", 'artist': 'AJR'}, {'name': 'creature', 'artist': 'half alive'}, {'name': 'Right Now', 'artist': 'Confetti'}, {'name': 'Casita', 'artist': 'The Astronomers'}, {'name': 'SAD (Clap Your Hands)', 'artist': 'Young Rising Sons'}, {'name': 'Bud Like You', 'artist': 'AJR'}, {'name': 'Morning In America', 'artist': 'Jon Bellion'}, {'name': 'El Dorado', 'artist': 'Stellar'}, {'name': 'Girl', 'artist': 'Jukebox The Ghost'}, {'name': 'Numb Little Bug', 'artist': 'Em Beihold'}, {'name': 'OK Overture', 'artist': 'AJR'}, {'name': 'Infinitely Ordinary', 'artist': 'The Wrecks'}, {'name': 'Elephant In The Room', 'artist': 'Confetti'}, {'name': 'Pocket Full Of Gold', 'artist': 'American Authors'}, {'name': 'Victorious', 'artist': 'Panic! At The Disco'}]
songs = [{'name': 'Bang!', 'artist': 'AJR'}, {'name': 'The Good In Me', 'artist': 'Jon Bellion'}, {'name': 'Record Player', 'artist': 'Daisy the Great, AJR'}, {'name': 'Celebrate', 'artist': 'Ingrid Michaelson, AJR'}, {'name': 'The Fall', 'artist': 'half alive'}, {'name': '100 Bad Days', 'artist': 'AJR'}, {'name': 'All My Favorite Songs (feat. AJR)', 'artist': 'Weezer, AJR'}, {'name': 'Wish You the Worst', 'artist': 'Ryan Mack'}, {'name': "I'm Born To Run", 'artist': 'American Authors'}, {'name': 'The Lotto', 'artist': 'Ingrid Michaelson, AJR'}, {'name': 'Bummerland', 'artist': 'AJR'}, {'name': 'Casita', 'artist': 'The Astronomers'}, {'name': 'Talk Too Much', 'artist': 'COIN'}, {'name': 'Only Human', 'artist': 'Ryan Mack'}, {'name': 'Kingdom Come', 'artist': 'Jon Bellion'}, {'name': "Don't Throw Out My Legos", 'artist': 'AJR'}, {'name': 'Everybody Talks', 'artist': 'Neon Trees'}, {'name': 'Boy In The Bubble', 'artist': 'Alec Benjamin'}, {'name': "It's Alright", 'artist': 'Mother Mother'}, {'name': 'Happy Pills', 'artist': 'Weathers'}, {'name': 'Humpty Dumpty', 'artist': 'AJR'}, {'name': 'Bad Dream', 'artist': 'Stellar'}, {'name': 'Fvck Somebody', 'artist': 'The Wrecks'}, {'name': 'Revolution', 'artist': 'The Score'}, {'name': 'Morning In America', 'artist': 'Jon Bellion'}, {'name': 'Break My Face', 'artist': 'AJR'}, {'name': 'Your New Boyfriend', 'artist': 'Wilbur Soot'}, {'name': 'El Dorado', 'artist': 'Stellar'}, {'name': 'Tear in My Heart', 'artist': 'Twenty One Pilots'}, {'name': 'creature', 'artist': 'half alive'}, {'name': 'Way Less Sad', 'artist': 'AJR'}, {'name': 'Overwhelmed (Ryan Mack Remix)', 'artist': 'Ryan Mack'}, {'name': 'Do My Own Thing', 'artist': 'American Authors'}, {'name': 'Boys Will Be Bugs', 'artist': 'Cavetown'}, {'name': 'Dear God', 'artist': 'Confetti'}, {'name': 'Birthday Party', 'artist': 'AJR'}, {'name': 'Subliminal', 'artist': 'half alive'}, {'name': 'Achey Bones', 'artist': 'The Happy Fits'}, {'name': 'We Happy Dont Worry', 'artist': 'American Authors'}, {'name': 'killer queen', 'artist': 'Mad Tsai'}, {'name': 'Touchy Feely Fool', 'artist': 'AJR'}, {'name': 'SAD (Clap Your Hands)', 'artist': 'Young Rising Sons'}, {'name': 'Skywalking', 'artist': 'The Astronomers, Zach Paradis'}, {'name': 'She Wants Me (To Be Loved)', 'artist': 'The Happy Fits'}, {'name': 'sail away', 'artist': 'lovelytheband'}, {'name': "Finale (Can't Wait To See What You Do Next)", 'artist': 'AJR'}, {'name': 'Infinitely Ordinary', 'artist': 'The Wrecks'}, {'name': 'Pocket Full Of Gold', 'artist': 'American Authors'}, {'name': 'Right Now', 'artist': 'Confetti'}, {'name': 'For Elise', 'artist': 'Saint Motel'}]

data = requests.get("https://www.youtube.com/results?search_query=Bang!+by+AJR+lyric+video")
dataStorage = open("htmlStorage.txt", "w")

htmlStorage = open("dataStorage2.txt", "w")
for line in data.text:
    try:
        htmlStorage.write(line)
    except UnicodeEncodeError:
        pass
htmlStorage.close()

index = 0

def printUrl():
    global index
    data = requests.get(f"https://www.youtube.com/results?search_query={songs[index]['name']}+by+{songs[index]['artist'].replace(' ', '+')}+lyric+video")
    while len(data.text.split("/watch?v=")[1].split('"')[0]) > 500: #Makes sure the URL isn't malformed for some reason, indicated by extremly long urls. 
        time.sleep(1)
        data = requests.get(f"https://www.youtube.com/results?search_query={songs[index]['name']}+by+{songs[index]['artist'].replace(' ', '+')}+lyric+video")
    # print(data.text.split("/watch?v=")[1].split('"')[0])
    dataStorage.write(songs[index]["name"] + " by " + songs[index]["artist"] + " ")
    dataStorage.write(data.text.split('}},"simpleText":"')[1].split('"')[0] + " ")
    dataStorage.write(data.text.split("/watch?v=")[1].split('"')[0] + "\n" * 2)
    index += 1

async def e():
    start_time = time.time()


    await asyncio.gather(*(asyncio.to_thread(printUrl) for i in range(50)))
   


    print("--- %s seconds ---" % (time.time() - start_time))




# if __name__ == "__main__":
asyncio.run(e())

dataStorage.close()

# style-scope ytd-thumbnail-overlay-time-status-renderer