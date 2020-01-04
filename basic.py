from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:\\chromedriver\\chromedriver')

driver.get('http://naver.com')
driver.implicitly_wait(3)
driver.get_screenshot_as_file('naver_main.png')

driver.quit()