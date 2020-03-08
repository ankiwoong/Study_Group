from selenium import webdriver
import clipboard

driver = webdriver.Chrome(executable_path='C:\\chromedriver\\chromedriver')
driver.implicitly_wait(3)

# 일회용 로그인 페이지
driver.get('https://nid.naver.com/nidlogin.login?mode=number')

elem_login = driver.find_element_by_id("disposable_num")
elem_login.clear()

# 네이버 앱 실행 -> 왼쪽 상단 삼선 -> 오른쪽 상단 설정 아이콘 -> 네이버 계정 정보 -> 1회용 로그인 번호 받기
elem_login.send_keys('77936221')
driver.find_element_by_xpath(
    '//*[@id="frmNIDLogin"]/fieldset/span/input').click()
driver.get('http://mail.naver.com/')

titles = driver.find_elements_by_css_selector("strong.mail_title")

for title in titles:
    print(title.text)

driver.quit()
