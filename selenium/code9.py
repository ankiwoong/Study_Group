# selenium 임포트
from selenium import webdriver

# webdriver 설정(Chrome, Firefox 등)
driver = webdriver.Chrome('/chromedriver/chromedriver.exe')

# 크롬 브라우저 내부 대기
driver.implicitly_wait(3)

# 브라우저 사이즈
driver.set_window_size(1366, 768)  # maximize_window(), minimize_window()

# 페이지 이동
driver.get('https://www.naver.com')

# 검색창 input 선택
element = driver.find_element_by_id("query")

# 검색어 입력
element.send_keys('펭수')

# 검색(Form Submit)
element.submit()
