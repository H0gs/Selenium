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

browserOptions = Options()
browserOptions.add_extension("adguard.crx")

browser = webdriver.Chrome(options=browserOptions)
actions = ActionChains(browser)

browser.get("https://www.youtube.com/")
browser.switch_to.window(browser.window_handles[0]) 
print("Switched to tab 0")

time.sleep(2)
searchBar = browser.find_element(By.XPATH, r'/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/form/div[1]/div[1]/input')
# searchBar.click()
time.sleep(2)
searchBar.send_keys("hello")
searchBar.send_keys(Keys.RETURN)

while True:
    pass