import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Whale/2.8.107.16 Safari/537.36"
)

browser = webdriver.Chrome("./chromedriver.exe", options=options)
browser.maximize_window()

url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"
browser.get(url)

detected_value = browser.find_element_by_id("detected_value")
print(detected_value.text)

# headless 사용시 user-agent : Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/86.0.4240.111 Safari/537.36
# user-agent 선언시 : Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Whale/2.8.107.16 Safari/537.36

browser.quit()