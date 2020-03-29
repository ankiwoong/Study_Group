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
votes = 투표
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
    # 투표 추출
    vote = container.find('span', attrs={'name': 'nv'})['data-value']
    votes.append(vote)
    # 총 수입 추출
    gross = container.find('span', attrs={'name': 'nv'}).findNext(
        'span').findNext('span').findNext('span').text

    if len(gross) > 3:
        us_gross.append(gross)
    else:
        us_gross.append(np.nan)

# 추출 데이터 출력
# print(titles)
# print(years)
# print(time)
# print(imdb_ratings)
# print(metascores)
# print(votes)
# print(us_gross)

# DataFrame 생성
movies = pd.DataFrame({
    'movie': titles,
    'year': years,
    'timeMin': time,
    'imdb': imdb_ratings,
    'metascore': metascores,
    'votes': votes,
    'us_grossMillions': us_gross,
})

# DataFrame 확인
# print(movies)

# DataFrame 타입 확인
# print(movies.dtypes)

# 전처리 과정 - 년도
movies['year'] = movies['year'].str.extract('(\d+)').astype(int)
# print(movies['year'])

# 전처리 과정 - 상영 시간
movies['timeMin'] = movies['timeMin'].str.extract('(\d+)').astype(int)
# print(movies['timeMin'])

# 전처리 과정 - 메타스코어
movies['metascore'] = movies['metascore'].astype(int)
# print(movies['metascore'])

# 전처리 과정 - 투표
movies['votes'] = movies['votes'].astype(int)
# print(movies['votes'])

# 전처리 과정 - 총 수입
movies['us_grossMillions'] = movies['us_grossMillions'].astype(str)
movies['us_grossMillions'] = movies['us_grossMillions'].map(
    lambda x: x.lstrip('$').rstrip('M'))
movies['us_grossMillions'] = pd.to_numeric(
    movies['us_grossMillions'], errors='coerce')
# print(movies['us_grossMillions'])

# 전처리 후 DataFrame 확인
print(movies)

# 전처리 후 DataFrame 타입 확인
print(movies.dtypes)

# CSV 저장
movies.to_csv('movies.csv')
