from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import TimeoutException
from datetime import datetime
import time
import json
import random

sch = {}
with open('booking_time.txt', encoding='utf8') as f:
    sch = json.load(f)
sch['d'] = datetime.strptime(sch['date'], '%Y-%m-%d %H:00:00')

wd = webdriver.Chrome('./chromedriver')

# 타임보드 페이지 로그인
wd.get("http://nosp.da.naver.com/")
wd.find_element_by_id("userId").send_keys(sch['id'])
wd.find_element_by_id("userPw").send_keys(sch['pw'])
wd.execute_script('doSubmitValidation()')

# 타임보드 신청 화면 이동
while True:
    try:
        wd.find_element_by_link_text("광고관리").click()
    except Exception as e:
        time.sleep(0.1)
    else:
        break
while True:
    try:
        wd.find_element_by_link_text("타임보드 토큰 현황 및 신청").click()
    except Exception as e:
        time.sleep(0.1)
    else:
        break

# 광고주 및 브랜드 검색, 입력
while True:
    try:
        wd.execute_script('searchBrand()')
    except Exception as e:
        time.sleep(0.1)
    else:
        break
while True:
    try:
        wd.find_element_by_id("searchSponsorValue").send_keys(sch['adv'])
    except Exception as e:
        time.sleep(0.1)
    else:
        break
while True:
    try:
        wd.find_element_by_link_text("검색").click()
    except Exception as e:
        time.sleep(0.1)
    else:
        break

# 광고주 검색 ajax가 끝날 때 까지 대기
while True:
    try:
        wd.find_element_by_xpath(
            "//table[@id='tblSponsorOnSerarchBrand']//td[.='{}']/..".format(sch['adv'])).click()
    except Exception as e:
        print('Waiting tblSponsorOnSerarchBrand')
        time.sleep(0.1)
    else:
        break

# 브랜드 검색 ajax가 끝날 때 까지 대기
while True:
    try:
        wd.find_element_by_xpath(
            "//table[@id='tblBrandOnSearchBrand']//td[.='{}']/..".format(sch['brd'])).click()
    except Exception as e:
        print('Waiting tblBrandOnSearchBrand')
        time.sleep(0.1)
    else:
        break

wd.find_element_by_link_text("선택완료").click()

while True:
    try:
        btn = wd.find_element_by_id('btnLastWeek')
    except Exception as e:
        print('Waiting btnLastWeek')
        time.sleep(0.1)
    else:
        break

token_time = int(sch['d'].timestamp() / 3600) + 702585
td_id = 'td{}'.format(token_time)
script_func = 'createToken({})'.format(token_time)

print('Token Time: {}'.format(token_time))

# 마지막주 확인
while True:
    # 토큰 창 열기
    try:
        wd.find_element_by_id('btnLastWeek').click()
        wd.find_element_by_id(td_id)
        wd.execute_script(script_func)
    except Exception as e:
        print('Token is not opened')
        now = datetime.now()
        if now.hour == 10 and now.min == 59 and now.second == 58:
            time.sleep(random.randint(10, 20)/100)
        elif now.hour == 10 and now.min == 59 and now.second == 59:
            time.sleep(random.randint(0, 9)/100)
        else:
            time.sleep(1)
        continue
    else:
        # 토큰 창 열렸음
        time.sleep(0.5)
        try:
            wd.switch_to.alert.accept()
        except Exception as e:
            # alert창 없으므로 break
            print(e)
            break
        # 다시 창을 열자

# 토큰 창 열림
while True:
    try:
        token_box = wd.find_element_by_id('ccValueOnCreateTokenDialog')
    except Exception as e:
        print('Waiting TokenDialog')
        time.sleep(0.1)
    else:
        break

# 캡차 팝업에서 입력 박스 선택
while True:
    try:
        wd.find_element_by_id("ccValueOnCreateTokenDialog").send_keys('')
    except Exception as e:
        print(e)
        time.sleep(0.1)
    else:
        break
