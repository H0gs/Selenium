from selenium import webdriver
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import os
from selenium.webdriver.chrome.options import Options


browserOptions = Options()
browserOptions.add_extension("adguard.crx")

browser = webdriver.Chrome(options=browserOptions)
browser.get("https://www.youtube.com/watch?v=KW0eUrUiyxo")

# print(browser.title)

# search.send_keys(Keys.RETURN)

# browser.minimize_window()

# time.sleep(5)
# browser.execute_script("window.open('');")
browser.switch_to.window(browser.window_handles[0]) 
print("done")
browser.find_element(By.TAG_NAME, "body").send_keys("k")
while(True):
    pass

