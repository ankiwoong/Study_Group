from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome("./chromedriver.exe")
browser.get("https://naver.com")

elem = browser.find_element_by_class_name("link_login")
# print(
#     elem
# )  # <selenium.webdriver.remote.webelement.WebElement (session="fb601d316d0610f24f2e86ac75485a4b", element="0e8dbb51-11db-4371-a79e-151ca40ae6ad")>
elem.click()
browser.back()
browser.forward()
browser.refresh()
browser.back()

elem = browser.find_element_by_id("query")
elem.send_keys("오늘코딩내일디버깅")
elem.send_keys(Keys.ENTER)

elem = browser.find_elements_by_tag_name("a")
for e in elem:
    print(e.get_attribute("href"))

browser.get("https://www.daum.net")
elem = browser.find_element_by_name("q")
elem.send_keys("오늘코딩내일디버깅")
elem = browser.find_element_by_xpath('//*[@id="daumSearch"]/fieldset/div/div/button[2]')
elem.click()
browser.quit()