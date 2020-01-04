from selenium import webdriver

driver = webdriver.Chrome('/chromedriver/chromedriver.exe')
driver.implicitly_wait(3)
driver.get('http://ankiwoong.pythonanywhere.com/')

driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/button').click()

driver.find_element_by_name('username').send_keys('test2')
driver.find_element_by_name('password').send_keys('test2')
driver.find_element_by_xpath('/html/body/div/div[3]/div/form/button').click()

driver.find_element_by_xpath('/html/body/div/div[3]/div/button').click()
