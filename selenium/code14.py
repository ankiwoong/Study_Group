from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome(executable_path='/chromedriver/chromedriver.exe')
driver.implicitly_wait(3)

# 일회용 로그인 페이지
driver.get('https://nid.naver.com/nidlogin.login?mode=number')

elem_login = driver.find_element_by_id("disposable_num")
elem_login.clear()

# 네이버 앱 실행 -> 왼쪽 상단 삼선 -> 오른쪽 상단 설정 아이콘 -> 네이버 계정 정보 -> 1회용 로그인 번호 받기
elem_login.send_keys('27963290')
driver.find_element_by_xpath(
    '//*[@id="frmNIDLogin"]/fieldset/span/input').click()

# Naver 페이 들어가기
driver.get('https://order.pay.naver.com/home')
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
notices = soup.find_all('a', {'class': 'goods'})

for n in notices:
    print(n.text.strip())
