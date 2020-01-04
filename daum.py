from selenium import webdriver

id = 'strongpink'
pw = '0109reset'

# 다음 로그인
driver = webdriver.Chrome(executable_path='C:\\chromedriver\\chromedriver')
driver.implicitly_wait(3)
driver.get('https://logins.daum.net/accounts/toploginform.do')
driver.find_element_by_id('id').send_keys(id)
driver.find_element_by_id('inputPwd').send_keys(pw)
driver.find_element_by_xpath('//*[@id="loginSubmit"]').click()

driver.find_element_by_xpath('//*[@id="mArticle"]/div[1]/div[2]/ul/li[1]/em/a').click()

titles = driver.find_elements_by_css_selector("strong.tit_subject")

for title in titles:
    print(title.text)

driver.quit()