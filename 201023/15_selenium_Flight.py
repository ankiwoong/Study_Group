from selenium import webdriver

browser = webdriver.Chrome("./chromedriver.exe")
browser.maximize_window()  # 창 최대화

url = "https://flight.naver.com/flights"
browser.get(url)  # url로 이동

# 가는 날 선택
browser.find_element_by_link_text("가는날 선택").click()

# 이번달 27일, 28일 선택
# browser.find_elements_by_link_text("27")[0].click()  # [0] -> 이번달
# browser.find_elements_by_link_text("28")[0].click()  # [0] -> 이번달

# 다음달 27일, 28일 선택
# browser.find_elements_by_link_text("27")[1].click()  # [1] -> 다음달
# browser.find_elements_by_link_text("28")[1].click()  # [1] -> 다음달

# 이번달 27일, 다음달 28일 선택
browser.find_elements_by_link_text("27")[0].click()  # [0] -> 이번달
browser.find_elements_by_link_text("28")[1].click()  # [1] -> 다음달

# 제주도 선택
browser.find_element_by_xpath('//*[@id="recommendationList"]/ul/li[1]').click()

# 항공권 검색
browser.find_element_by_link_text("항공권 검색").click()

# 첫번째 결과 출력
elem = browser.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[4]/ul/li[1]')
print(elem.text)