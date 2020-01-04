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

# 타이틀 출력
print('Title : {}'.format(driver.title))
