from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(executable_path='C:\\chromedriver\\chromedriver', options=options)
driver.get('http://pythonscraping.com/pages/files/form.html')

firstnameField = driver.find_element_by_name('firstname')
lastnameField = driver.find_element_by_name('lastname')
submitButton = driver.find_element_by_id('submit')

actions = ActionChains(driver)\
    .click(firstnameField).send_keys('An')\
    .click(lastnameField).send_keys('Kiwoong')\
    .send_keys(Keys.RETURN)

actions.perform()

print(driver.find_element_by_tag_name('body').text)

driver.quit()