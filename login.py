from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# Chrome Browser 옵션 사용
options = Options()

# Chrome Browser 숨기기 모드(headless)
options.add_argument('headless')

# chromedriver 위치 지정 및 options 설정
driver = webdriver.Chrome(executable_path='C:\\chromedriver\\chromedriver', options=options)

# 크롤링 전 3초 대기
driver.implicitly_wait(3)

# 대상 Site 지정
driver.get('http://quotes.toscrape.com/')

# login button click
site_login = driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/p/a')
site_login.click()

# login id / pw 지정
login_id = 'ankiwoong'
login_pw = 'ankiwoong'

# id login
id = driver.find_element_by_name('username').send_keys(login_id)
# pw login
pw = driver.find_element_by_name('password').send_keys(login_pw)

# login button click
login_click = driver.find_element_by_xpath('/html/body/div/form/input[2]')
login_click.click()

# 페이지의 elements 모두 가져오기
html = driver.page_source

# BeautifulSoup 사용
soup = BeautifulSoup(html, 'html.parser')

# 명언(# -> id / . -> class)
notices_s = soup.select('div.col-md-8 > div.quote > span.text')
# 위인(# -> id / . -> class
notices_e = soup.select('div.col-md-8 > div.quote > span > small.author')

# 빈 리스트 생성(s_list -> 명언 / e_list -> 위인)
s_list = []
e_list = []

# 명언 가져오기
for i in notices_s:
    s_list.append(i.text.strip())

# 위인 가져오기
for j in notices_e:
    e_list.append(j.text)

# 명언 리스트와 위인 리스트의 길이를 비교하여 길이가 같으면 파일 생성
if len(s_list) == len(e_list):
    # encoding -> utf-8
    f = open('print.txt', 'w', encoding='utf-8')
    # 범위는 무엇으로 정해도 두개의 값은 같으므로 range(len(리스트))
    for a in range(len(s_list)):
        # 문자 사이에 by 를 붙이고 행간지정
        data = s_list[a] + ' by ' + e_list[a] + '\n'
        f.write(data)
    f.close()
else:
    # 두개의 길이가 틀릴시 Error 출력
    print('Error')

# driver 종료(메모리 초기화)
driver.quit()

# 파일 출력
f = open('print.txt', 'r', encoding='utf-8')
lines = f.readlines()
for line in lines:
    print(line.strip('\n'))
f.close()