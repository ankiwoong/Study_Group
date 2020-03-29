'''
인터넷 영화 데이터베이스(https://www.imdb.com/)
- https://www.imdb.com/search/title/?groups=top_1000&ref_=adv_prv
? : 리소스 경로 시작의 끝과 매개 변수의 시작
groups=top_1000 : 페이지의 내용
ref_= : 다음 페이지(adv_nxt) 또는 이전 페이지(adv_prv)의 매개 변수 지정
'''

import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from fake_useragent import UserAgent


# usaragnt 생성 및 header 정보 생성
ua = UserAgent(verify_ssl=False)
headers = {'User-Agent': ua.random}

# 사이트
url = 'https://www.imdb.com/search/title/?groups=top_1000&ref_=adv_prv'

# url 응답 요청
req = requests.get(url, headers=headers)

# 응답 값 확인
# print(req)

# HTML 구문 확인
soup = BeautifulSoup(req.text, "html.parser")

# 확인(soup.prettify() - 트리형식으로 출력)
# print(soup.prettify())

# 데이터 추출 리스트 생성
'''
titles = 제목
years = 출시 연도
time = 상영 시간
imdb_ratings = 평점
metascores = 메타스코어
votes = 개표수
us_gross = 총 수입
'''
titles = []
years = []
time = []
imdb_ratings = []
metascores = []
votes = []
us_gross = []

movie_div = soup.find_all('div', class_='lister-item mode-advanced')

for container in movie_div:
    # 제목 추출
    name = container.h3.a.text
    titles.append(name)
    # 출시 년도 추출
    year = container.h3.find('span', class_='lister-item-year').text
    years.append(year)
    # 상영 시간 추출
    runtime = container.find('span', class_='runtime').text
    time.append(runtime)
    # 평점 추출
    imdb = float(container.find('strong').text)
    imdb_ratings.append(imdb)
    # 메타스코어 추출
    metascore = container.find('span', class_='metascore').text
    metascores.append(metascore.strip())
    # 개표수 추출
    vote = container.find('span', attrs={'name': 'nv'})['data-value']
    votes.append(int(vote))
    # 총 수입 추출
    gross = container.find('span', attrs={'name': 'nv'}).findNext(
        'span').findNext('span').findNext('span').text

    if len(gross) > 3:
        us_gross.append(gross)
    else:
        us_gross.append(np.nan)

# 추출 데이터 출력
print(titles)
print(years)
print(time)
print(imdb_ratings)
print(metascores)
print(votes)
print(us_gross)
