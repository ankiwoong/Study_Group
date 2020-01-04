from selenium import webdriver

driver = webdriver.Chrome('/chromedriver/chromedriver.exe')

driver.implicitly_wait(3)

driver.get('http://www.naver.com')
