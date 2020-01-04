from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='C:\\chromedriver\\chromedriver')
driver.implicitly_wait(3)

id = 'ankiwoongtest'
pw = '0109reset'

# gmail.com 자동 로그인
driver.get('https://accounts.google.com/ServiceLogin/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=AddSession')
driver.find_element_by_name('identifier').send_keys(id)
driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
driver.find_element_by_name('password').send_keys(pw)
driver.find_element_by_xpath('//*[@id="passwordNext"]').send_keys(Keys.ENTER)