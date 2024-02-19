from selenium import webdriver
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import requests
import asyncio

def getSongs(name):
    global urls
    urls = []
    global index
    index = -1
    global songs
    songs = []

    def printUrl():
        global index
        global songs
        index += 1
        tempIndex = index
        # print(songs[index])
        data = requests.get(f"https://www.youtube.com/results?search_query={songs[index]['name']}+by+{songs[index]['artist'].replace(' ', '+')}+lyric+video")
        while len(data.text.split("/watch?v=")[1].split('"')[0]) > 500: #Makes sure the URL isn't malformed for some reason, indicated by extremly long urls. 
            time.sleep(1)
            data = requests.get(f"https://www.youtube.com/results?search_query={songs[index]['name']}+by+{songs[index]['artist'].replace(' ', '+')}+lyric+video")
        # urls.append(data.text.split("/watch?v=")[1].split('"')[0] + "\n" * 2)
        songs[tempIndex]['url'] = data.text.split("/watch?v=")[1].split('"')[0]
        # print(songs[tempIndex])
        # print()

    browserOptions = Options()
    browserOptions.add_extension("adguard.crx")

    browser = webdriver.Chrome(options=browserOptions)
    browser.minimize_window()
    # browser.set_window_position(-2000,0)
    actions = ActionChains(browser)

    time.sleep(3)
    # browser.minimize_window()
    browser.get(f"https://open.spotify.com/search/{name}")
    browser.switch_to.window(browser.window_handles[0]) 
    # time.sleep(30)
    if not 'No results found for "' in browser.page_source:
            
        browser.minimize_window()

        # browser.get("https://open.spotify.com/artist/6s22t5Y3prQHyaHWUN1R1C")
        # browser.execute_script("window.open('');")
        browser.switch_to.window(browser.window_handles[0])
        print("Switched to tab 0")

        # print(browser.page_source.split('href="/artist/')[1].split('"')[0]) # spotify ID of the artist
        # print(browser.page_source.split('href="/artist/')[1].split("<")) # name of the artist

        # browser.get("https://open.spotify.com/artist/6s22t5Y3prQHyaHWUN1R1C")
        time.sleep(3)

        storage = open("htmlStorage.txt", "w")
        for char in browser.page_source:
            try:
                storage.write(char)
            except UnicodeEncodeError:
                pass
        storage.close()
        print("Stored html")

        data = ""
        storage = open("htmlStorage.txt", "r")
        for line in storage:
            data += line.strip()
        storage.close()

        artistRadio = data.split(' Radio" class')[1].split('href="/playlist/')[1].split('"')[0]
        browser.get("https://open.spotify.com/playlist/" + artistRadio)
        time.sleep(2)
        storage = open("htmlStorage2.txt", "w")
        for char in browser.page_source:
            try:
                storage.write(char)
            except UnicodeEncodeError:
                pass
        storage.close()
        print("Stored html")
        print(browser.find_element(By.XPATH, r'/html/body/div[3]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div[1]/section/div[1]').text)

        totalSongs = 3
        i = 0


        actions.move_to_element(browser.find_elements(By.CLASS_NAME, "iCQtmPqY0QvkumAOuCjr")[23]).perform()
        time.sleep(0.5)
        actions.move_to_element(browser.find_elements(By.CLASS_NAME, "iCQtmPqY0QvkumAOuCjr")[25]).perform()
        time.sleep(0.5)
        actions.move_to_element(browser.find_elements(By.CLASS_NAME, "iCQtmPqY0QvkumAOuCjr")[28]).perform()

        for songElement in browser.find_elements(By.CLASS_NAME, "iCQtmPqY0QvkumAOuCjr"):
            # print(songElement.find_element(By.XPATH, "..").text.split("\n")[0] + " by " + songElement.find_element(By.XPATH, "..").text.split("\n")[-1]) #Works!
            # print(songElement.find_elements(By.TAG_NAME, "div")[4].text)
            # print(float(songElement.find_element(By.XPATH, "../..").text.split("\n")[-1].replace(":", ".")))
            # print(int(float(songElement.find_element(By.XPATH, "../..").text.split("\n")[-1].split(":")[0])) * 60 + int(float(songElement.find_element(By.XPATH, "../..").text.split("\n")[-1].split(":")[1])))
            song = {}
            song["name"] = songElement.find_element(By.XPATH, "..").text.split("\n")[0]
            song["artist"] = songElement.find_element(By.XPATH, "..").text.split("\n")[-1]
            #  ../.. gets grandfather element, we get all of the text contained by that div, then we take the last element it prints, which is the length of the song, convert it into an int representing seconds. 
            song["lengthInSeconds"] = int(float(songElement.find_element(By.XPATH, "../..").text.split("\n")[-1].split(":")[0])) * 60 + int(float(songElement.find_element(By.XPATH, "../..").text.split("\n")[-1].split(":")[1]))
            song["url"] = "!PlaceHolder!"
            songs.append(song)

        # browser.get("https://www.youtube.com/")
        # time.sleep(2)
        # searchBar = browser.find_element(By.XPATH, r'/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/form/div[1]/div[1]/input')
        # searchBar.click()
        # time.sleep(2)
        # searchBar.send_keys(f'{songs[0]["name"]} by {songs[0]["artist"]} lyric video')
        # searchBar.send_keys(Keys.RETURN)
        # print(songs)

        async def getArtistsAsync():
            start_time = time.time()


            await asyncio.gather(*(asyncio.to_thread(printUrl) for i in range(50)))
        


            print("--- %s seconds ---" % (time.time() - start_time))




        # if __name__ == "__main__":
        asyncio.run(getArtistsAsync())

        # time.sleep(20)
    return songs
    print(songs)
    # time.sleep(180)

    # browser.get(f"https://www.youtube.com/watch?v={songs[0]['url']}")
    # # browser.find_element(By.TAG_NAME, "body").send_keys("k")
    # # time.sleep(songs[i]["lengthInSeconds"])
    # time.sleep(5)
    # for i in range(1, len(songs)):
    #     browser.get(f"https://www.youtube.com/watch?v={songs[i]['url']}")
    #     # browser.find_element(By.TAG_NAME, "body").send_keys("k")
    #     # time.sleep(songs[i]["lengthInSeconds"])
    #     time.sleep(5)

    # for songHolder in browser.find_elements(By.CLASS_NAME, "iCQtmPqY0QvkumAOuCjr"):
    #     print(f"{songHolder.find_element(By.CSS_SELECTOR, 'div').text, songHolder.find_element(By.CSS_SELECTOR, 'div').find_element(By.CLASS_NAME, 'Type__TypeElement-sc-goli3j-0 bGROfl').find_element(By.CSS_SELECTOR, 'a').text}")

    # aria-rowindex="

    while(True):
        pass
    time.sleep(5)
    expandable = browser.find_element(By.CLASS_NAME, "Button-sc-1dqy6lx-0 dAlRsJ")
    expandable.click()
