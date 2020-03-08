from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import clipboard
import time

id = ''
pw = ''

driver = webdriver.Chrome(executable_path='C:\\chromedriver\\chromedriver')
driver.implicitly_wait(3)

driver.get(
    'https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com')

clipboard.copy(id)
driver.find_element_by_xpath('//*[@id="id"]').click()
ActionChains(driver).key_down(Keys.CONTROL).send_keys(
    'v').key_up(Keys.CONTROL).perform()
time.sleep(1)

clipboard.copy(pw)
driver.find_element_by_xpath('//*[@id="pw"]').click()
ActionChains(driver).key_down(Keys.CONTROL).send_keys(
    'v').key_up(Keys.CONTROL).perform()
time.sleep(1)

driver.find_element_by_xpath('//*[@id="log.login"]').click()
time.sleep(1)

driver.get('https://mail.naver.com/')

titles = driver.find_elements_by_css_selector("strong.mail_title")

for title in titles:
    print(title.text)

driver.quit()
