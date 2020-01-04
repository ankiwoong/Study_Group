from selenium import webdriver

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(executable_path='C:\\chromedriver\\chromedriver')
driver.get('http://pythonscraping.com/pages/files/form.html')

firstnameField = driver.find_element_by_name('firstname')
lastnameField = driver.find_element_by_name('lastname')
submitButton = driver.find_element_by_id('submit')

firstnameField.send_keys('an')
lastnameField.send_keys('kiwoong')
submitButton.click()