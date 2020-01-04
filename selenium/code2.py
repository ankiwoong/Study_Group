# selenium 임포트
from selenium import webdriver

# webdriver 설정(Chrome, Firefox 등)
driver = webdriver.Chrome('/chromedriver/chromedriver.exe')

# 속성 확인
print(dir(driver))
