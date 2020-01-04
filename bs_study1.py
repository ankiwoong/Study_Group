from bs4 import BeautifulSoup
import requests

req = requests.get('https://kuckjwi0928.github.io/pythoncodingprogram/')
html = req.text
soup = BeautifulSoup(html, 'html.parser')

# 출력문 빈 리스트
list_j = []

# h1 ~ h6 태그 가져오기
for i in range(1, 7):       # h1 ~ h6이므로 범위는 1, 7
    # format 메서드를 사용하여 i에 번호를 하나씩 더하여 h1 ~ h6 태그 가져오기
    soup_selet = soup.select('div#main_content_wrap > section#main_content > h{}'.format(i))
    # 중간 확인
    # print(soup_selet)
    # 가공
    for j in soup_selet:
        # text 파일만 추출하여 출력문 빈 리스트에 추가
        list_j.append(j.text)

# print(list_j)

# 결과값 출력
for l in range(5, -1, -1):      # 범위는 range(시작, 끝, 스탭)이므로 5, 4, 3, 2, 1, 0 이므로 -
    print(list_j[l])            # 출력문 리스트에서 하나씩 l 인덱스로 가져오기